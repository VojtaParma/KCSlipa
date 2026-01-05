import pygame
import socket
import pickle
import random

# --- NASTAVENÍ ---
pygame.init()
SIRKA_HRY = 300
SIRKA_TERMINALU = 250
SIRKA_OKNA = SIRKA_HRY + SIRKA_TERMINALU
okno = pygame.display.set_mode((SIRKA_OKNA, 300))
pygame.display.set_caption("Piškvorky SERVER (X)")
hodiny = pygame.time.Clock()

# Barvy
BILA = (255, 255, 255)
CERNA = (10, 10, 10)  # Trochu jemnější černá pro terminál
MODRA = (0, 100, 255)
CERVENA = (220, 20, 60)
ZELENA = (57, 255, 20) # "Matrix" zelená
SEDA = (200, 200, 200)

# --- LOGIKA TERMINÁLU ---
logy = ["--- SYSTEM START ---", "Waiting for connection..."]

def pridej_log(text):
    global logy
    logy.append(text)
    if len(logy) > 13: # Omezení počtu řádků
        logy.pop(0)

# --- LOGIKA HRY ---
def reset_hry():
    global pole, hrac, konec
    pole = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    konec = 0 
    hrac = random.choice([1, 2]) # 1 = Server (X), 2 = Klient (O)
    kdo = "SERVER" if hrac == 1 else "CLIENT"
    pridej_log(f"New Game. Starter: {kdo}")

reset_hry()
muj_symbol = 1
pripojeno = False

# --- SÍŤOVÉ NASTAVENÍ ---
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0", 5555))
server.listen(1)
server.setblocking(False)

klient = None

# --- FUNKCE PRO VYKRESLOVÁNÍ ---
def vykresli_vse():
    okno.fill(BILA)
    
    # 1. Herní pole
    for i in range(1, 3):
        pygame.draw.line(okno, CERNA, (100 * i, 0), (100 * i, 300), 2)
        pygame.draw.line(okno, CERNA, (0, 100 * i), (300, 100 * i), 2)
    
    pismo_symbol = pygame.font.Font(None, 100)
    for r in range(3):
        for s in range(3):
            x, y = s * 100 + 50, r * 100 + 50
            if pole[r][s] == 1:
                img = pismo_symbol.render("X", True, MODRA)
                okno.blit(img, img.get_rect(center=(x, y)))
            elif pole[r][s] == 2:
                img = pismo_symbol.render("O", True, CERVENA)
                okno.blit(img, img.get_rect(center=(x, y)))

    # 2. Terminál (vpravo)
    pygame.draw.rect(okno, CERNA, (SIRKA_HRY, 0, SIRKA_TERMINALU, 300))
    pygame.draw.line(okno, ZELENA, (SIRKA_HRY, 0), (SIRKA_HRY, 300), 2)
    
    font_term = pygame.font.SysFont("monospace", 15)
    for i, radek in enumerate(logy):
        barva = ZELENA if "Error" not in radek else CERVENA
        img = font_term.render(f"> {radek}", True, barva)
        okno.blit(img, (SIRKA_HRY + 10, 10 + i * 20))

    # 3. Stavové hlášky na ploše
    font_stav = pygame.font.Font(None, 24)
    if konec != 0:
        texty = {1: "X WON!", 2: "O WON!", 3: "DRAW!"}
        msg = f"{texty[konec]} [Press R]"
        okno.blit(font_stav.render(msg, True, CERNA), (10, 10))

def zkontroluj_stav():
    # Výherní kombinace
    for i in range(3):
        if pole[i][0] == pole[i][1] == pole[i][2] != 0: return pole[i][0]
        if pole[0][i] == pole[1][i] == pole[2][i] != 0: return pole[0][i]
    if pole[0][0] == pole[1][1] == pole[2][2] != 0: return pole[0][0]
    if pole[0][2] == pole[1][1] == pole[2][0] != 0: return pole[0][2]
    # Remíza
    if all(pole[r][s] != 0 for r in range(3) for s in range(3)): return 3
    return 0

def odesli_data():
    if pripojeno and klient:
        try:
            stav = {"pole": pole, "konec": konec, "hrac": hrac}
            klient.send(pickle.dumps(stav))
        except Exception as e:
            pridej_log(f"Send Error: {e}")

# --- HLAVNÍ SMYČKA ---
running = True
while running:
    # Připojení klienta
    if not pripojeno:
        try:
            klient, adresa = server.accept()
            klient.setblocking(False)
            pripojeno = True
            pridej_log(f"Client: {adresa[0]}")
            odesli_data() # Pošle info, kdo začíná
        except: pass

    # Příjem dat (tah klienta)
    if pripojeno and hrac == 2 and konec == 0:
        try:
            data = klient.recv(4096)
            if data:
                tah = pickle.loads(data)
                pole[tah[0]][tah[1]] = 2
                pridej_log(f"Client Move: [{tah[0]},{tah[1]}]")
                konec = zkontroluj_stav()
                hrac = 1 if konec == 0 else hrac
                if konec != 0: pridej_log(f"Game End: {konec}")
                odesli_data()
        except: pass

    # Eventy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Restart hry
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_hry()
            pridej_log("Game Restarted...")
            odesli_data()

        # Tah serveru
        if event.type == pygame.MOUSEBUTTONDOWN and hrac == 1 and konec == 0 and pripojeno:
            mx, my = event.pos
            if mx < SIRKA_HRY: # Klik jen do pole
                r, s = my // 100, mx // 100
                if pole[r][s] == 0:
                    pole[r][s] = 1
                    pridej_log(f"Server Move: [{r},{s}]")
                    konec = zkontroluj_stav()
                    hrac = 2 if konec == 0 else hrac
                    if konec != 0: pridej_log(f"Game End: {konec}")
                    odesli_data()

    vykresli_vse()
    pygame.display.flip()
    hodiny.tick(60)

pygame.quit()