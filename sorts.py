from Personnage import *


def dégats(sort, vita, resifixe, resi): #calcule les dégats infligés en fonction des points de vie, resistances (fixes et normales), et des dégats du sort puis renvoie la vie restante


    sort = ((sort / 100) - resi) * 100 #on applique d'abords les résistances normales (%)

    sort = sort - resifixe #ensuite les résistances fixes


    if sort < 0: #cette commande sert a éviter de soigner si il y a trop de resistances fixes

        sort = 0


    vita = vita - sort


    if vita < 0:

        vita = 0


    return vita


def stasis(sort, resfixe, res, vita): #4ème type de sort, spécial (en fonction des résistances et du meilleur sort)


    stas = []

    liste = []


    liste.append(dégats(sort[0], vita, resfixe[0], res[0]))

    liste.append(dégats(sort[1], vita, resfixe[1], res[1]))

    liste.append(dégats(sort[2], vita, resfixe[2], res[2]))


    stas.append(min(liste))

    stas = stas[0]


    return stas


vie = 1000



lresfixe = []


resfixe1 = 10 #résistance fixe de type 1 --> resfixe=10 réduit les dégats de 10

resfixe2 = 10

resfixe3 = 10


lresfixe.append(resfixe1)

lresfixe.append(resfixe2)

lresfixe.append(resfixe3)



lres = []


res1 = 0.1 #résistance normale de type 1 --> res = 0.1 réduit les dégats de 10%

res2 = 0.1

res3 = 0.1


lres.append(res1)

lres.append(res2)

lres.append(res3)