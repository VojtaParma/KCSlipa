import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill((255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # náhodná pozice
    x = random.randint(30, 570)
    y = random.randint(30, 370)

    # náhodná barva
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # nakreslí kruh, aniž by vymazal obrazovku
    pygame.draw.circle(screen, color, (x, y), 30)

    pygame.display.flip()
    pygame.time.delay(500)  # čekání půl sekundy

pygame.quit()
