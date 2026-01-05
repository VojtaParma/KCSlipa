import pygame

# Spuštění pygame
pygame.init()

# Vytvoření okna 300x300 pixelů
okno = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Piškvorky 3x3")

# Barvy
BILA = (255, 255, 255)
CERNA = (255, 255, 255)
MODRA = (0, 0, 0)
CERVENA = (0, 0, 0)

# Hrací pole - na začátku všude 0 (prázdné)
# 0 = prázdné, 1 = X, 2 = O
pole = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

# Kdo je na tahu (1 = X, 2 = O)
hrac = 1

# Hra běží?
hra_bezi = True

# Je konec hry? (0 = hra pokračuje, 1 = vyhrál X, 2 = vyhrál O)
konec = 0


# Funkce pro vykreslení mřížky
def vykresli_mrizku():
    okno.fill(BILA)  # Vybarví pozadí na bílo
    
    # Nakreslí 2 svislé čáry
    pygame.draw.line(okno, CERNA, (100, 0), (100, 300), 3)
    pygame.draw.line(okno, CERNA, (200, 0), (200, 300), 3)
    
    # Nakreslí 2 vodorovné čáry
    pygame.draw.line(okno, CERNA, (0, 100), (300, 100), 3)
    pygame.draw.line(okno, CERNA, (0, 200), (300, 200), 3)


# Funkce pro vykreslení X a O na hrací ploše
def vykresli_symboly():
    pismo = pygame.font.Font(None, 100)  # Velikost písma
    
    # Projde všechna políčka (řádek po řádku)
    for radek in range(3):
        for sloupec in range(3):
            
            # Spočítá střed políčka
            x = sloupec * 100 + 50
            y = radek * 100 + 50
            
            # Pokud je tam X (1), nakreslí modré X
            if pole[radek][sloupec] == 1:
                text = pismo.render("X", True, MODRA)
                okno.blit(text, text.get_rect(center=(x, y)))
            
            # Pokud je tam O (2), nakreslí červené O
            elif pole[radek][sloupec] == 2:
                text = pismo.render("X", True, CERVENA)
                okno.blit(text, text.get_rect(center=(x, y)))


# Funkce pro kontrolu, jestli někdo vyhrál
def zkontroluj_vyhru():
    
    # Kontrola všech 3 řádků
    for radek in range(3):
        if pole[radek][0] == pole[radek][1] == pole[radek][2] != 0:
            return pole[radek][0]  # Vrátí 1 nebo 2 (kdo vyhrál)
    
    # Kontrola všech 3 sloupců
    for sloupec in range(3):
        if pole[0][sloupec] == pole[1][sloupec] == pole[2][sloupec] != 0:
            return pole[0][sloupec]
    
    # Kontrola diagonály zleva doprava (\)
    if pole[0][0] == pole[1][1] == pole[2][2] != 0:
        return pole[0][0]
    
    # Kontrola diagonály zprava doleva (/)
    if pole[0][2] == pole[1][1] == pole[2][0] != 0:
        return pole[0][2]
    
    return 0  # Nikdo nevyhrál


# Funkce pro restart hry
def restart_hry():
    global pole, hrac, konec
    
    # Všechna políčka zase prázdná
    pole = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    
    # Začíná X
    hrac = 1
    
    # Hra pokračuje
    konec = 0


# Hlavní herní smyčka (opakuje se dokola)
while hra_bezi:
    
    # Projde všechny události (kliknutí myší, stisknutí klávesy...)
    for udalost in pygame.event.get():
        
        # Pokud zavřu okno, hra skončí
        if udalost.type == pygame.QUIT:
            hra_bezi = False
        
        # Pokud kliknu myší a hra ještě neskončila
        if udalost.type == pygame.MOUSEBUTTONDOWN and konec == 0:
            
            # Zjistím, kam jsem klikl
            x, y = udalost.pos
            sloupec = x // 100  # Vydělím 100 (velikost políčka)
            radek = y // 100
            
            # Pokud je políčko prázdné, udělám tah
            if pole[radek][sloupec] == 0:
                pole[radek][sloupec] = hrac  # Umístím X nebo O
                
                # Zkontroluju, jestli jsem nevyhrál
                konec = zkontroluj_vyhru()
                
                # Pokud nikdo nevyhrál, přepnu hráče
                if konec == 0:
                    if hrac == 1:
                        hrac = 2  # Z X na O
                    else:
                        hrac = 1  # Z O na X
        
        # Pokud stisknu MEZERNÍK po konci hry, restartuji
        if udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_SPACE and konec != 0:
                restart_hry()
    
    # Vykreslení všeho na obrazovku
    vykresli_mrizku()  # Nakreslí mřížku
    vykresli_symboly()  # Nakreslí X a O
    
    # Pokud někdo vyhrál, zobrazí se hlášení
    if konec != 0:
        pismo = pygame.font.Font(None, 50)
        
        # Text podle toho, kdo vyhrál
        if konec == 1:
            zprava = "Vyhrál X! (MEZERNÍK = restart)"
        else:
            zprava = "Vyhrál O! (MEZERNÍK = restart)"
        
        text = pismo.render(zprava, True, CERNA)
        okno.blit(text, text.get_rect(center=(150, 150)))
    
    # Aktualizuje obrazovku (zobrazí změny)
    pygame.display.flip()

# Ukončí pygame
pygame.quit()