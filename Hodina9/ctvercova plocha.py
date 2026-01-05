import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

ROWS = 25
COLS = 25
GAP_RATIO = 0.08

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)

    width, height = screen.get_size()

    cell_w = width / COLS
    cell_h = height / ROWS
    cell_size = min(cell_w, cell_h)

    gap = int(cell_size * GAP_RATIO)
    draw_size = int(cell_size - gap)

    screen.fill((30, 30, 30))

    for r in range(ROWS):
        for c in range(COLS):
            x = int(c * cell_size + gap / 2)
            y = int(r * cell_size + gap / 2)
            pygame.draw.rect(screen, (200, 200, 200), (x, y, draw_size, draw_size))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
