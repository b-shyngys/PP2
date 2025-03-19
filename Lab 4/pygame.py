import pygame
pygame.init()

pygame.display.set_mode((800, 600))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

pygame.quit()