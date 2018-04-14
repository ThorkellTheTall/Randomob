from level import *


def vieperso(level, carac): #vie du personnage


    hp = 100 + (level * (carac[0] + carac[1] + carac[2]))


    return hp


def carac(sort, caractéristique): #calcule les dégats des sorts en fonction des caractéristiques et renvoie les dégats des sorts


    sort = ((caractéristique/100) + (sort / 100)) * 100 #on augmente les dégats du sort de carac%


    return sort



lcarac = []

carac1 = 10 #caractéristique type 1
carac2 = 10
carac3 = 10


lcarac.append(carac1)

lcarac.append(carac2)

lcarac.append(carac3)


lsorts = []

sort1 = 30 #Fleche

sort2 = 30 #Patate

sort3 = 30 #Boule de feu


sort1 = carac(sort1, carac1) #on applique l'amélioration des sorts en fonction des caractéristiques

sort2 = carac(sort2, carac2)

sort3 = carac(sort3, carac3)


lsorts.append(sort1)

lsorts.append(sort2)

lsorts.append(sort3)


hperso = vieperso(level, lcarac)


