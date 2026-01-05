import pygame

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Text Example")

font = pygame.font.Font(None, 72)  # velikost textu
text = font.render("Ahoj!", True, (0, 255, 255))  # text + barva

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # černé pozadí
    screen.blit(text, (150, 100))  # pozice textu

    pygame.display.flip()

pygame.quit()
