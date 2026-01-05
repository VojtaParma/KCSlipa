import pygame

# --- základní nastavení ---
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Piškvorky")

POCET = 25                 # 25 × 25 polí
VELIKOST = 500 // POCET   # velikost jednoho pole

# 0 = prázdné, 1 = kolečko, 2 = křížek
pole = []
for r in range(POCET):
    radek = []
    for c in range(POCET):
        radek.append(0)
    pole.append(radek)

hrac = 1  # začíná kolečko

# --- hlavní smyčka ---
bezi = True
while bezi:

    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False

        # klik myší
        if udalost.type == pygame.MOUSEBUTTONDOWN:
            x, y = udalost.pos
            sloupec = x // VELIKOST
            radek = y // VELIKOST

            if pole[radek][sloupec] == 0:
                pole[radek][sloupec] = hrac

                # přepnutí hráče
                if hrac == 1:
                    hrac = 2
                else:
                    hrac = 1

    # --- vykreslení ---
    screen.fill((30, 30, 30))

    for r in range(POCET):
        for c in range(POCET):
            x = c * VELIKOST
            y = r * VELIKOST

            # mřížka
            pygame.draw.rect(screen, (80, 80, 80), (x, y, VELIKOST, VELIKOST), 1)

            # kolečko
            if pole[r][c] == 1:
                pygame.draw.circle(
                    screen,
                    (200, 200, 200),
                    (x + VELIKOST // 2, y + VELIKOST // 2),
                    VELIKOST // 3,
                    2
                )

            # křížek
            if pole[r][c] == 2:
                pygame.draw.line(
                    screen, (200, 200, 200),
                    (x + 5, y + 5),
                    (x + VELIKOST - 5, y + VELIKOST - 5),
                    2
                )
                pygame.draw.line(
                    screen, (200, 200, 200),
                    (x + VELIKOST - 5, y + 5),
                    (x + 5, y + VELIKOST - 5),
                    2
                )

    pygame.display.flip()

pygame.quit()
