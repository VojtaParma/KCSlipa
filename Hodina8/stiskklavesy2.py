import pygame

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Keyboard Display")

font = pygame.font.Font(None, 72)
text = ""

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            text = pygame.key.name(event.key)  # název klávesy

    screen.fill((30, 30, 30))

    render = font.render(text, True, (255, 255, 255))
    screen.blit(render, (250 - render.get_width() // 2, 150 - render.get_height() // 2))

    pygame.display.flip()

pygame.quit()
