import pygame
import lib as lib

pygame.init()
players = lib.create_players(100)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    lib.screen.fill([0,0,0])
    lib.draw_players(players)

    clock.tick(60)
    pygame.display.update()
pygame.quit()
