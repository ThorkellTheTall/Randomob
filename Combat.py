import pygame

from pygame.locals import *

from sorts import *

from Personnage import *

from mobs import *

from Barre_de_vie import *

from level import *

from afficheur import *


image = pygame.image.load("interface combat.png")


pygame.init()


pygame.mouse.set_visible(1)

global screen
screen = pygame.display.set_mode((800, 512))


stop = False

def affichage_tete(part1, part2, part3, key):


    if pos_clef(key) == 0:

        screen.blit(part1[1], part1[0])

    elif pos_clef(key) == 1:

        screen.blit(part2[1], part2[0])

    elif pos_clef(key) == 2:

        screen.blit(part3[1], part3[0])
""

def affichage_corps(part1, part2, part3, key):


    if pos_clef(key) == 0:

        screen.blit(part1[3], part1[2])

    elif pos_clef(key) == 1:

        screen.blit(part2[3], part2[2])

    elif pos_clef(key) == 2:

        screen.blit(part3[3], part3[2])


""

def affichage_pieds(part1, part2, part3, key):


    if pos_clef(key) == 0:

        screen.blit(part1[5], part1[4])

    elif pos_clef(key) == 1:

        screen.blit(part2[5], part2[4])

    elif pos_clef(key) == 2:

        screen.blit(part3[5], part3[4])


""

#boutons


COULEUR = (200, 191, 231) #couleur du remplissage

COLOR = (COULEUR)


bouton1 = pygame.Rect((253, 366), (271, 65)) #on créé un bouton 1

bouton2 = pygame.Rect((526, 366), (271, 65))

bouton3 = pygame.Rect((253, 432), (271, 65))

bouton4 = pygame.Rect((526, 432), (271, 65))


rect_surf1 = pygame.Surface(bouton1.size) #on donne une surface au bouton 1

rect_surf2 = pygame.Surface(bouton2.size)

rect_surf3 = pygame.Surface(bouton3.size)

rect_surf4 = pygame.Surface(bouton4.size)


rect_surf1.fill(COLOR) #on donne une couleur au bouton 1

rect_surf2.fill(COLOR)

rect_surf3.fill(COLOR)

rect_surf4.fill(COLOR)




print(randomob)


hp_randomob = vie(level, randomob[1])

print(hp_randomob)


hp1 = 400 #hp max du perso

hp2 = 1000 #hp max du monstre

vie = 1000


while not stop:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            stop = True

        elif event.type == MOUSEBUTTONUP: #quand je relache le bouton

            if event.button == 1: #1= clique gauche

                if bouton1.collidepoint(event.pos): #si on appuie sur le bouton 1


                    vie = dégats(lsorts[0], vie, lresfixe[0], lres[0])


                    ratio2 = pertepv(hp2, vie) #on obtient un ratio de pv perdus

                    width2 = ratio2*183 #on modifie la largeur de la barre en fonction des pv perdus

                    width2 = round(width2) #arrondi (car smoothscale prend que des int)


                    rect_surf7 = pygame.transform.smoothscale(rect_surf7, (width2, 11)) #on applique la modif


                elif bouton2.collidepoint(event.pos):


                    vie = dégats(lsorts[1], vie, lresfixe[1], lres[1])


                    ratio2 = pertepv(hp2, vie)

                    width2 = ratio2*183

                    width2 = round(width2)


                    rect_surf7 = pygame.transform.smoothscale(rect_surf7, (width2, 11))


                elif bouton3.collidepoint(event.pos):


                    vie = dégats(lsorts[2], vie, lresfixe[2], lres[2])


                    ratio2 = pertepv(hp2, vie)

                    width2 = ratio2*183

                    width2 = round(width2)


                    rect_surf7 = pygame.transform.smoothscale(rect_surf7, (width2, 11))


                elif bouton4.collidepoint(event.pos):


                    vie = stasis(lsorts, lresfixe, lres, vie)


                    hperso = hperso/100

                    hperso = hperso - (hperso*0.1)

                    hperso = hperso * 100


                    ratio1 = pertepv(hp1, hperso)

                    ratio2 = pertepv(hp2, vie)

                    width1 = ratio1*183

                    width1 = round(width1)

                    width2 = ratio2*183

                    width2 = round(width2)


                    rect_surf6 = pygame.transform.smoothscale(rect_surf6, (width1, 11))

                    rect_surf7 = pygame.transform.smoothscale(rect_surf7, (width2, 11))





    # affiche les boutons

    screen.blit(rect_surf1, bouton1)

    screen.blit(rect_surf2, bouton2)

    screen.blit(rect_surf3, bouton3)

    screen.blit(rect_surf4, bouton4)

    # affiche le fond

    screen.blit(image, (0, 0))

    # affiche les barres de vie

    screen.blit(rect_surf6, barre1)

    screen.blit(rect_surf7, barre2)

    # affiche le monstre

    affichage_tete(skull, arc, war, clefs_tetes)

    affichage_corps(skull, arc, war, clefs_corps)

    affichage_pieds(skull, arc, war, clefs_pieds)


    pygame.display.flip()


pygame.quit()