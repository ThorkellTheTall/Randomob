import pygame

from pygame.locals import *



WHITE = (0, 0, 0) #couleur du remplissage
COLOR = (WHITE)


##image = pygame.image.load("interface combat.png") #image affichée initialement


pygame.init()

pygame.mouse.set_visible(1)

screen = pygame.display.set_mode((800, 512)) #taille de la fenêtre pygame

stop = False

clickable_area1 = pygame.Rect((80, 200), (250, 15)) #on créé un bouton 1

clickable_area2 = pygame.Rect((75, 225), (250, 15))

clickable_area3 = pygame.Rect((75, 250), (250, 15))

clickable_area4 = pygame.Rect((75, 275), (250, 15))


rect_surf1 = pygame.Surface(clickable_area1.size) #on donne une surface au bouton 1

rect_surf2 = pygame.Surface(clickable_area2.size)

rect_surf3 = pygame.Surface(clickable_area3.size)

rect_surf4 = pygame.Surface(clickable_area4.size)


rect_surf1.fill(COLOR) #on donne une couleur au bouton 1

rect_surf2.fill(COLOR)

rect_surf3.fill(COLOR)

rect_surf4.fill(COLOR)

##pygame.draw.rect(0, 0, 0)

while not stop:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            stop = True


        elif event.type == MOUSEBUTTONUP: #quand je relache le bouton

            if event.button == 1: #1= clique gauche

                if clickable_area1.collidepoint(event.pos): #si on appuie sur le bouton 1

                    image = pygame.image.load("world.png")


                elif clickable_area2.collidepoint(event.pos):

                    image = pygame.image.load("smiley.jpg")


                elif clickable_area3.collidepoint(event.pos):

                    image = pygame.image.load("world2.png")


                elif clickable_area4.collidepoint(event.pos):

                    image = pygame.image.load("homer.png")


    screen.fill(0) #on efface tout l'écran


    screen.blit(rect_surf1, clickable_area1)  #affiche le bouton 1

    screen.blit(rect_surf2, clickable_area2)

    screen.blit(rect_surf3, clickable_area3)

    screen.blit(rect_surf4, clickable_area4)


    #screen.blit(image, (150, 75)) #on affiche l'image qui est dans la variable "image"


    pygame.display.flip()


pygame.quit()