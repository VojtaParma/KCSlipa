import pygame   
import random

pygame.init()

screen = pygame.display.set_mode((1900, 1080))
font = pygame.font.Font(None, 20)

def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )   

color = random_color()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
            color = random_color()
            print("RGB:", color)

    screen.fill(color)

    text = font.render(f"RGB: {color}", True, (255,255,255))
    screen.blit(text, (20, 20))

    pygame.display.flip()