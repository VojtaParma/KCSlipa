import pygame

pygame.init()
screen = pygame.display.set_mode((400, 200))
font = pygame.font.Font(None, 40)

count = 0
button = pygame.Rect(100, 50, 200, 60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                count += 1

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 150, 255), button)
    screen.blit(font.render("Klikni", True, (255, 255, 255)), (160, 65))

    screen.blit(font.render(str(count), True, (255, 255, 255)), (190, 140))

    pygame.display.flip()

pygame.quit()
