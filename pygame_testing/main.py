import pygame
# initializing
pygame.init()
#        screen making          width  height
screen = pygame.display.set_mode( (700,500) )
#display editing
pygame.display.set_caption("trying to understand pygame")



# thingy that means everything stops after close button is pressed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False