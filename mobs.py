import random

from level import *

import pygame

from pygame.locals import *

from bibliothèque_mobs import *


pygame.init()


def round_2(nombre): #arrondie à 2 chiffres après la virgule


    nombre = round(nombre, 2)


    return nombre


def fragmentation_tete_pieds(monstre): #crée une liste avec les caractéeistiques de la tête et des pieds


    liste = []


    liste.append(round_2((monstre[0])/4))

    liste.append(round_2((monstre[1])/4))

    liste.append(round_2((monstre[2])/4))

    liste.append(round_2((monstre[3])/4))

    liste.append(round_2((monstre[4])/4))

    liste.append(round_2((monstre[5])/4))

    liste.append(round_2((monstre[6])/4))

    liste.append(round_2((monstre[7])/4))


    return liste


def fragmentation_corps(monstre): #crée une liste avec les caractéristiques du corps


    liste = []


    liste.append(round_2((monstre[0])/2))

    liste.append(round_2((monstre[1])/2))

    liste.append(round_2((monstre[2])/2))

    liste.append(round_2((monstre[3])/2))

    liste.append(round_2((monstre[4])/2))

    liste.append(round_2((monstre[5])/2))

    liste.append(round_2((monstre[6])/2))

    liste.append(round_2((monstre[7])/2))


    return liste


def addition_3_listes(liste1, liste2, liste3): # aditionne 3 listes (du type : addition_3_listes([a, b], [c, d], [e, f]) rend [a+c+e, b+d+f]

    liste = []


    element1 = liste1[0] + liste2[0] + liste3[0]

    element2 = liste1[1] + liste2[1] + liste3[1]

    element3 = liste1[2] + liste2[2] + liste3[2]

    element4 = liste1[3] + liste2[3] + liste3[3]

    element5 = liste1[4] + liste2[4] + liste3[4]

    element6 = liste1[5] + liste2[5] + liste3[5]

    element7 = liste1[6] + liste2[6] + liste3[6]

    element8 = liste1[7] + liste2[7] + liste3[7]


    liste.append(element1)

    liste.append(element2)

    liste.append(element3)

    liste.append(element4)

    liste.append(element5)

    liste.append(element6)

    liste.append(element7)

    liste.append(element8)


    return liste


def aleatoire_3(un, deux, trois): #choisie aléatoirement entre 3 éléments (str, liste, etc..)

    element = [un, deux, trois]

    element_ = random.choice(element)

    return element_


def gestion_aleatoire(parts, clefs):

    part =[]


    aleatoire = aleatoire_3(parts[0], parts[1], parts[2])


    if aleatoire == parts[0] :

        part = parts[0]

        clefs[0] = 1


    elif aleatoire == parts[1] :

        part = parts[1]

        clefs[1] = 1


    elif aleatoire == parts[2] :

        part = parts[2]

        clefs[2] = 1

    return part


def generateur_monstre(tetes, corpss, pieds, clef_tete, clef_corps, clef_pieds): #génère un monstre aléatoirement

    monstre = []

    tete = []

    corps = []

    pied = []


    tete = gestion_aleatoire(tetes, clef_tete)

    corps = gestion_aleatoire(corpss, clef_corps)

    pied = gestion_aleatoire(pieds, clef_pieds)


    monstre = addition_3_listes(tete, corps, pied)


    return monstre


def vie(niveau, hp): #calcule les points de vie des monstres en fonction de leur stat vie (liste[1]) et du niveau


    vie = hp * niveau

    vie = round(vie)


    return vie


def pos_clef(clef):

    x = len(clef)

    for i in range(x):

        a = clef[i]

        if a == 1:

            return i


# clefs d'affichage des différentes parties (dans l'ordre squelette archer barbare)

clefs_tetes = [0, 0, 0]

clefs_corps = [0, 0, 0]

clefs_pieds = [0, 0, 0]

# [att, hp, resfixe x 3, res% x 3]

squelette = [15, 15, 10, 10 ,10, 0.05, 0.05, 0.05]

archer = [20, 10, 0, 0, 0, 0.03, 0.03, 0.03]

barbare = [10 ,20, 15, 15, 15, 0.1, 0.1, 0.1]

boss1 = [30, 30, 20, 20, 20, 0.1, 0.1, 0.1]

boss2 = [20, 40, 20, 20, 20, 0.2, 0.2, 0.2]

boss3 = [60, 30, 10, 10, 10, 0.1, 0.1, 0.1]


tete_squelette = fragmentation_tete_pieds(squelette)

corps_squelette = fragmentation_corps(squelette)

pieds_squelette = fragmentation_tete_pieds(squelette)


tete_archer = fragmentation_tete_pieds(archer)

corps_archer = fragmentation_corps(archer)

pieds_archer = fragmentation_tete_pieds(archer)


tete_barbare = fragmentation_tete_pieds(barbare)

corps_barbare = fragmentation_corps(barbare)

pieds_barbare = fragmentation_tete_pieds(barbare)


head = []

head.append(tete_squelette)
head.append(tete_archer)
head.append(tete_barbare)

body = []

body.append(corps_squelette)
body.append(corps_archer)
body.append(corps_barbare)

feet = []

feet.append(pieds_squelette)
feet.append(pieds_archer)
feet.append(pieds_barbare)

randomob = generateur_monstre(head, body, feet, clefs_tetes,  clefs_corps, clefs_pieds)
print(randomob)