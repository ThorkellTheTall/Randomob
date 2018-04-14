import pygame


def pertepv(pvmax, pv):

    ratio = pv/pvmax

    return ratio


COULEUR_hp = (255, 0, 0) #barres de vie


barre1 = pygame.Rect((42, 9), (183, 11))

barre2 = pygame.Rect((573, 10), (183, 11))


rect_surf6 = pygame.Surface(barre1.size)

rect_surf7 = pygame.Surface(barre2.size)


rect_surf6.fill(COULEUR_hp)

rect_surf7.fill(COULEUR_hp)



