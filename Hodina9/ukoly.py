import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circle Color Changer")

circle_color = (255, 255, 255)
square_color = (0, 0, 0)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            circle_color = random_color()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            square_color = random_color()
    
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, circle_color, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 50)
    pygame.draw.rect(screen, square_color, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 50, 50))
    pygame.display.flip()

pygame.quit()