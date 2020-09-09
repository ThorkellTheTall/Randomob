# Imports

import pygame
from pygame.locals import *
from random import *

# Constantes

defaite = False

victoire = False

niveau = 1

stop = False

# Afficheur

boutons, rect_surfaces = [], []

for elt in [(253, 366), (526, 366), (253, 432), (526, 432)]:
    boutons.append(pygame.Rect(elt, (271, 65)))

    rect_surfaces.append(pygame.Surface(boutons[-1].size))


# Sorts

def epee(attaquant, cible):  # sort du personnage
    degats = max(attaquant["Dommages"] + 20 - cible["Resistances"], 0)  # applique les boost et resistances
    cible["PV"] = max(cible["PV"] - degats, 0)  # applique les degats
    return "Coup d'epee"  # pour pouvoir afficher dans l'historique


def charge(attaquant, cible):  # sort du monstre (meme chose)
    degats = max(attaquant["Dommages"] + 10 - cible["Resistances"], 0)
    cible["PV"] = max(cible["PV"] - degats, 0)
    return "Charge"


def regeneration(attaquant, victime):  # soin
    attaquant["PV"] = min(attaquant["PV"] + 15 + attaquant["Dommages"], attaquant["PV max"])  # rajoute des pvs (+boost)
    attaquant["Dommages"] += 10 + 2 * niveau  # rajoute les dommages
    attaquant["Buffs"].append(["Dommages", 10 + 2 * niveau, 2])  # pour pouvoir l'appliquer sur plusieurs tours
    attaquant["Relances"][attaquant["Sorts"].index(
        regeneration)] = 3  # intervalle de relance (index permet de trouver "regeneration dans la liste de sorts" et retourne la postition (nombre))
    return "Regeneration"


def bouclier(attaquant, cible):
    attaquant["Resistances"] += 5 + 5 * niveau  # rajoute les resistances
    attaquant["Buffs"].append(["Resistances", 5 + 5 * niveau, 2])  # rajoute dans la liste de buffs
    attaquant["Relances"][attaquant["Sorts"].index(bouclier)] = 3
    return "Bouclier"


def blocage(attaquant, cible):
    cible["Tour Annule"] = 3  # nb de tours
    attaquant["Relances"][attaquant["Sorts"].index(blocage)] = 5
    return "Tourmente"


def furie(attaquant, cible):
    degats = max(int(attaquant["Dommages"] * 1.5) + 20 - cible["Resistances"], 0)  # applique les degats
    cible["PV"] = max(cible["PV"] - degats, 0)

    degats_retour = max(int(attaquant["Dommages"] * 0.75) + 10 - attaquant["Resistances"],
                        0)  # applique les degats a lui meme
    attaquant["PV"] = max(attaquant["PV"] - degats, 0)

    attaquant["Relances"][attaquant["Sorts"].index(furie)] = 5  # intervalle de relance
    return "Furie"


# Monstre

def generateur_monstre(liste_monstre, sorts=[charge]):  # genere un monstre aleatoirement

    clefs = [randint(0, len(liste_monstre) - 1) for i in range(3)]

    monstre = []
    for i in range(len(liste_monstre[0])):
        carac_tete = liste_monstre[clefs[0]][i] / 4 * (1 + niveau / 2)
        carac_corps = liste_monstre[clefs[1]][i] / 2 * (1 + niveau / 2)
        carac_pied = liste_monstre[clefs[2]][i] / 4 * (1 + niveau / 2)

        monstre.append(carac_tete + carac_corps + carac_pied)

    monstre = {  # cree le dictionnaire (liste d'objets)
        "PV max": int(monstre[1]),  # conversion en entier
        "PV": int(monstre[1]),
        "Dommages": int(monstre[0]),
        "Resistances": int(monstre[2]),
        "Sorts": sorts,
        "Tour Annule": 0,
        "Buffs": [],
        "Relances": [0 for i in range(len(sorts))]
    }

    return monstre


# Caracteristique des monstres [att, hp, res%]

liste_monstre = [
    [5, 50, 5],  # Equilibre
    [10, 40, 0],  # Attaque
    [3, 80, 10],  # Defense
]
liste_boss = [
    [10, 200, -10],  # Boss 1
]


# Barre de vie

def pertepv(pvmax, pv):
    ratio = pv / pvmax

    return ratio


COULEUR_hp = (255, 200, 5)  # barres de vie

barre1 = pygame.Rect((42, 9), (183, 11))
barre2 = pygame.Rect((573, 10), (183, 11))

rect_surf6 = pygame.Surface(barre1.size)
rect_surf7 = pygame.Surface(barre2.size)

rect_surf6.fill(COULEUR_hp)
rect_surf7.fill(COULEUR_hp)


# Tours

def compteur(temps, tour):
    chrono = []

    if temps == 0:
        tour = tour + 1
        temps = 15

    chrono.append(temps)
    chrono.append(tour)

    return chrono


# Animations

def deplacer_entite(image, x1, x2, frames_tot,
                    type):  # animation d'attaque (image, position initiale, position d'arrivee, nombre de frames voulues, personnage/monstre)

    global degats_monstre, degats_perso, animation_monstre, animation_perso, var_animation  # on importe les variables utiles

    if var_animation < frames_tot // 2:  # aller

        screen.blit(image, (x1 + int((x2 - x1) / (frames_tot // 2) * var_animation), 50))  # deplacement frame par frame
        var_animation += 1

    elif frames_tot > var_animation >= frames_tot // 2:  # retour

        if var_animation == frames_tot // 2:

            if type == "Personnage":
                degats_monstre = True  # si c'est un perso le monstre subit des degats

            else:
                degats_perso = True  # et inversement

        screen.blit(image, (x2 + int((x2 - x1) / (frames_tot // 2) * (frames_tot // 2 - var_animation)), 50))

        var_animation += 1

    else:

        if type == "Personnage":
            animation_perso = False  # si c'est le personnage alors l'animation se termine

        else:
            animation_monstre = False  # et inversement
        screen.blit(image, (x1, 50))  # affiche le perso/monstre a la position initiale
        var_animation = 0


def clignoter_entite(image, duree, periode, frames_tot, x):
    global var_clignotement, degats_perso, degats_monstre

    if var_clignotement < frames_tot:  # lance le clignotement durant le nombre de frames voulu
        var_clignotement += 1  # compte des frames
        condition = False
        condition = 0 <= var_clignotement % periode < duree

        if condition:
            screen.blit(image, (x, 50))

    if var_clignotement >= frames_tot:  # arrete
        degats_perso = False
        degats_monstre = False
        var_clignotement = 0


# Variables d'animation
animation_perso = False
animation_monstre = False
degats_perso = False
degats_monstre = False
var_animation = 0
var_clignotement = 0
i = 0

# Initialisation de pygame et images

pygame.init()
screen = pygame.display.set_mode((800, 512))
pygame.mouse.set_visible(1)
image = pygame.image.load("Interface combat.png")
image_perso = pygame.image.load("perso.png").convert()
image_perso.set_colorkey((255, 255, 255))  # Rend le blanc transparent
image_monstre = pygame.image.load("monstre.png").convert()
image_monstre.set_colorkey((255, 255, 255))
image_defaite = pygame.image.load("defaite.png")
image_victoire = pygame.image.load("victoire.png")

# Variable chrono et tours

clock = pygame.time.Clock()  # initialisation de l'horloge
tours, counter, text, text2 = 0, 10, '0', '0'
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Sylfaen', 15)
font_petit = pygame.font.SysFont('Sylfaen', 15)
historique = []
txt_message_cbt = font.render("Le combat commence !", True, (0, 0, 0))
stop = False
difference_pv = 0
attaque_monstre = False

# Variables personnage et monstre

if niveau % 5 != 0:
    monstre = generateur_monstre(liste_monstre)
else:
    monstre = generateur_monstre(liste_boss, [charge, regeneration, furie, bouclier])

personnage = {  # dictionnaire perso
    "PV max": 100 + niveau * 10,
    "PV": 100 + niveau * 10,
    "Dommages": 5,
    "Resistances": 5,
    "Sorts": [regeneration, bouclier, epee, blocage],
    "Buffs": [],
    "Relances": [0, 0, 0, 0],
    "Tour Annule": 0
}


def up_perso():  # Ameliore les caracteristiques des persos a chaque victoire

    global personnage

    personnage = {
        "PV max": 100 + niveau * 15,
        "PV": 100 + niveau * 15,
        "Dommages": niveau * 5 + 5,
        "Resistances": niveau * 3,
        "Sorts": [regeneration, bouclier, epee, blocage],
        "Buffs": [],
        "Relances": [0, 0, 0, 0],
        "Tour Annule": 0
    }


# Boucle de combat
def mise_a_jour_barres_vie():
    global rect_surf6, rect_surf7, monstre, personnage

    # Personnage
    width = round(pertepv(personnage["PV max"], personnage["PV"]) * 183)
    rect_surf6 = pygame.transform.smoothscale(rect_surf6, (max(0, width), 11))
    # Monstre
    width2 = round(pertepv(monstre["PV max"], monstre["PV"]) * 183)
    rect_surf7 = pygame.transform.smoothscale(rect_surf7, (max(0, width2), 11))


def maj_buffs_et_relances(entite):
    # Pour les relances (diminue de 1 les relances du perso/monstre a chacun de ses tours)
    for i in range(len(entite["Relances"])):
        entite["Relances"][i] = max(entite["Relances"][i] - 1, 0)

    # Pour les buffs
    nouveaux_buffs = []

    for i in range(len(entite["Buffs"])):  # on parcour la liste des buff du perso/monstre

        entite["Buffs"][i][2] = max(entite["Buffs"][i][2] - 1, 0)  # on enleve 1 a la duree a chaque tour

        if entite["Buffs"][i][2] != 0:  # si une relance est pas encore a 1 on la garde
            nouveaux_buffs.append(entite["Buffs"][i])

        else:
            type_buff = entite["Buffs"][i][0]  # sinon on enleve
            entite[type_buff] -= entite["Buffs"][i][1]

    entite["Buffs"] = nouveaux_buffs


def combat():
    global personnage, monstre, rect_surf6, rect_surf7, animation_perso, animation_monstre, text, text2, counter, tours, defaite, victoire, stop, txt_message_cbt, difference_pv, attaque_monstre

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            stop = True

        elif event.type == pygame.USEREVENT:

            if counter == 1:
                attaque_monstre = True

            counter -= 1
            tours = compteur(counter, tours)[1]
            text = str(counter) if counter > 0 else '0'
            text2 = str(tours)
            counter = compteur(counter, tours)[0]

        elif event.type == MOUSEBUTTONUP:  # Quand je relache le bouton

            if event.button == 1:  # 1= clique gauche

                for i in range(4):

                    est_relancable = personnage["Relances"][i] == 0  # verifie si le sort est relancable

                    if boutons[i].collidepoint(
                            event.pos) and var_animation == 0 and var_clignotement == 0 and est_relancable and not attaque_monstre:  # si on appuie sur le bouton i

                        counter = 1
                        pv_avant_attaque = monstre["PV"]
                        nom_sort = personnage["Sorts"][i](personnage, monstre)
                        pv_apres_attaque = monstre["PV"]

                        txt_message_cbt = font.render("Heros (lvl." + str(niveau) + ") lance " + nom_sort, True,
                                                      (0, 0, 0))  # affiche dans la barre du milieu
                        historique.append("Heros (lvl." + str(niveau) + ") lance " + nom_sort)

                        difference_pv = pv_avant_attaque - pv_apres_attaque
                        animation_perso = True
                        historique.append("Monstre : -" + str(difference_pv))

                        if pv_apres_attaque == 0:  # si le monstre a plus de pv
                            victoire = True

                        mise_a_jour_barres_vie()

                        # Une attaque par tour c'est au tour du monstre de jouer

    # Le monstre attaque si c'est a lui d'attaquer

    if attaque_monstre and var_animation == 0 and var_clignotement == 0:

        # Mise a jour des relances / Buffs du personnage

        maj_buffs_et_relances(monstre)

        # Le monstre lance un sort aleatoirement parmi ceux qu'il possede
        # SI le sort n'est pas relancable, alors le monstre (dans ce cas, le boss) passe son tour
        # Si le monstre est tourmente il a 25% de chances de passer son tour

        annulation = False

        if monstre["Tour Annule"] >= 1:
            monstre["Tour Annule"] -= 1  # on actualise le delai de tourmente

            annulation = 0.75 < random()

            txt_message_cbt = font.render("Monstre (lvl." + str(niveau) + ") est tourmente il ne peut pas attaquer !",
                                          True, (0, 0, 0))

        if not annulation:  # le monstre attaque

            pv_avant_attaque = personnage["PV"]
            sorts_possibles = []

            for i in range(len(monstre["Relances"])):

                if monstre["Relances"][i] == 0:  # verifie toutes les relances
                    sorts_possibles.append(i)  # ajoute les sorts qui n'ont pas de relance

            choix_sort = sorts_possibles[randint(0, len(sorts_possibles) - 1)]  # choisit aleatoirement

            nom_sort = monstre["Sorts"][choix_sort](monstre, personnage)  # applique le sort
            txt_message_cbt = font.render("Monstre (lvl." + str(niveau) + ") lance " + nom_sort, True,
                                          (0, 0, 0))  # ecrit
            historique.append("Monstre (lvl." + str(niveau) + ") lance " + nom_sort)  # met dans l'historique
            pv_apres_attaque = personnage["PV"]  # a

            difference_pv = pv_avant_attaque - pv_apres_attaque
            animation_monstre = True
            historique.append("Heros : -" + str(difference_pv))

            if pv_apres_attaque == 0:
                defaite = True

        mise_a_jour_barres_vie()

        maj_buffs_et_relances(personnage)

        attaque_monstre = False

    # affichage les boutons

    for i in range(4):
        screen.blit(rect_surfaces[i], boutons[i])

    # Afficher le fond

    screen.blit(image, (0, 0))

    # Affichage les barres de vie

    screen.blit(rect_surf6, barre1)
    screen.blit(rect_surf7, barre2)

    # Deplacement

    if animation_perso:
        deplacer_entite(image_perso, 40, 100, 30, "Personnage")

    if animation_monstre:
        deplacer_entite(image_monstre, 590, 520, 30, "Monstre")

    # Clignotement

    if degats_monstre:
        clignoter_entite(image_monstre, 6, 16, 30, 590)
        txt_pv_en_moins = font.render("-" + str(difference_pv), True, (255, 0, 0))
        screen.blit(txt_pv_en_moins, (550, 100))

    elif not animation_monstre:
        screen.blit(image_monstre, (590, 50))

    if degats_perso:
        clignoter_entite(image_perso, 6, 16, 30, 40)
        txt_pv_en_moins = font.render("-" + str(difference_pv), True, (255, 0, 0))
        screen.blit(txt_pv_en_moins, (170, 100))

    elif not animation_perso:
        screen.blit(image_perso, (50, 50))

    # affichage chronometre et compteur de tours

    screen.blit(font.render(text, True, (0, 0, 0)), (412, 7))
    screen.blit(font.render(text2, True, (0, 0, 0)), (412, 25))

    # Affichage caractristiques des entites

    txt_pv_joueur = font.render(str(personnage["PV"]) + "/" + str(personnage["PV max"]), True, (0, 0, 0))
    txt_pv_monstre = font.render(str(monstre["PV"]) + "/" + str(monstre["PV max"]), True, (0, 0, 0))

    screen.blit(txt_pv_joueur, (265 - txt_pv_joueur.get_width(), 40))
    screen.blit(txt_pv_monstre, (530, 40))

    txt_res_joueur = font.render(str(personnage["Resistances"]), True, (0, 0, 0))
    txt_res_monstre = font.render(str(monstre["Resistances"]), True, (0, 0, 0))
    txt_atk_joueur = font.render(str(personnage["Dommages"]), True, (0, 0, 0))
    txt_atk_monstre = font.render(str(monstre["Dommages"]), True, (0, 0, 0))

    screen.blit(txt_res_joueur, (310, 30))
    screen.blit(txt_res_monstre, (490 - txt_res_monstre.get_width(), 30))

    screen.blit(txt_atk_joueur, (310, 5))
    screen.blit(txt_atk_monstre, (490 - txt_atk_monstre.get_width(), 5))

    # Affichage des messages de combat (affiche uniquement les 10 derniers)

    screen.blit(txt_message_cbt, (400 - txt_message_cbt.get_width() // 2, 320))

    liste = historique[max(0, len(historique) - 10):]

    for i in range(len(liste)):
        elt = liste[i]
        txt_historique = font_petit.render(elt, True, (0, 0, 0))
        screen.blit(txt_historique, (13, 365 + 14 * i))

    pygame.display.flip()

    clock.tick(60)


# Boucle principale

while not stop:

    if (defaite == False and victoire == False) or var_animation != 0 or var_clignotement != 0:
        combat()

    if defaite and var_animation == 0 and var_clignotement == 0:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                stop = True

        screen.blit(image_defaite, (0, 0))

    elif victoire and var_animation == 0 and var_clignotement == 0:

        screen.blit(image_victoire, (0, 0))

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONUP:

                niveau += 1
                up_perso()

                if niveau % 5 != 0:
                    monstre = generateur_monstre(liste_monstre)
                else:
                    monstre = generateur_monstre(liste_boss, [charge, regeneration, furie, bouclier])

                # Reinitialisation de certains parametres

                clock = pygame.time.Clock()
                tours, counter, text, text2 = 0, 10, '0', '10'
                pygame.time.set_timer(pygame.USEREVENT, 1000)

                rect_surf6 = pygame.Surface(barre1.size)
                rect_surf7 = pygame.Surface(barre2.size)
                rect_surf6.fill(COULEUR_hp)
                rect_surf7.fill(COULEUR_hp)

                mise_a_jour_barres_vie()

                run = True
                victoire = False
                animation_perso = False
                animation_monstre = False
                degats_monstre = False
                degats_perso = False
                var_animation = 0
                txt_message_cbt = font.render("Le combat commence !", True, (0, 0, 0))

                historique = []

                pygame.time.wait(200)

    pygame.display.flip()

pygame.quit()
