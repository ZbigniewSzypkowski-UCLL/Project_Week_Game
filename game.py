import pygame

pygame.init()

screen = pygame.display.set_mode((1290, 810))

pygame.display.set_caption("Game Title")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            running = False