import pygame

from pygame.locals import *


# parties des mobs (dans l'ordre : (1 = tete, 2 = corps, 3 = pieds), (1 = squelette, 2 = archer, 3 = barbare) ex : 23 = corps barbare)

skull = []
arc = []
war = []

 # tetes
tete_skull = pygame.Rect((600, 87), (165, 40))
tete_arc = pygame.Rect((600, 87), (165, 40))
tete_war = pygame.Rect((600, 87), (165, 40))

 # corps
corps_skull = pygame.Rect((600, 127), (165, 70))
corps_arc = pygame.Rect((600, 127), (165, 70))
corps_war = pygame.Rect((600, 127), (165, 70))

 # pieds
pieds_skull = pygame.Rect((600, 197), (165, 30))
pieds_arc = pygame.Rect((600, 197), (165, 30))
pieds_war = pygame.Rect((600, 197), (165, 30))

 # surf
rect_surf11 = pygame.Surface(tete_skull.size)
rect_surf12 = pygame.Surface(tete_arc.size)
rect_surf13 = pygame.Surface(tete_war.size)


rect_surf21 = pygame.Surface(corps_skull.size)
rect_surf22 = pygame.Surface(corps_arc.size)
rect_surf23 = pygame.Surface(corps_war.size)


rect_surf31 = pygame.Surface(pieds_skull.size)
rect_surf32 = pygame.Surface(pieds_arc.size)
rect_surf33 = pygame.Surface(pieds_war.size)

 #couleurs
couleur_squelette = (100, 100, 100)
couleur_archer = (0, 100, 100)
couleur_war = (100, 0, 100)

rect_surf11.fill(couleur_squelette)
rect_surf21.fill(couleur_squelette)
rect_surf31.fill(couleur_squelette)


rect_surf12.fill(couleur_archer)
rect_surf22.fill(couleur_archer)
rect_surf32.fill(couleur_archer)


rect_surf13.fill(couleur_war)
rect_surf23.fill(couleur_war)
rect_surf33.fill(couleur_war)

 # on mes les parties dans des listes [rect tete, surface tete, rect corps...]

#squelette
skull.append(tete_skull)
skull.append(rect_surf11)
skull.append(corps_skull)
skull.append(rect_surf21)
skull.append(pieds_skull)
skull.append(rect_surf31)

#archer
arc.append(tete_arc)
arc.append(rect_surf12)
arc.append(corps_arc)
arc.append(rect_surf22)
arc.append(pieds_arc)
arc.append(rect_surf32)

#barbare
war.append(tete_war)
war.append(rect_surf13)
war.append(corps_war)
war.append(rect_surf23)
war.append(pieds_war)
war.append(rect_surf33)