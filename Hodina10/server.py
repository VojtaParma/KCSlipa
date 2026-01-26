import pygame
import socket
import pickle
import random

# --- NASTAVENÍ OKNA ---
pygame.init()
SIRKA_HRY = 300
SIRKA_TERMINALU = 250
okno = pygame.display.set_mode((SIRKA_HRY + SIRKA_TERMINALU, 300))
pygame.display.set_caption("Piškvorky SERVER - Security Update")
hodiny = pygame.time.Clock()

# Barvy
BILA, CERNA, ZELENA = (255, 255, 255), (10, 10, 10), (57, 255, 20)
MODRA, CERVENA = (0, 100, 255), (220, 20, 60)

# Logika a logování
logy = ["--- SECURITY SERVER READY ---"]
def pridej_log(text, error=False):
    logy.append(text)
    if len(logy) > 13: logy.pop(0)

def reset_hry():
    global pole, hrac, konec
    pole = [[0, 0, 0] for _ in range(3)]
    konec = 0 
    hrac = random.choice([1, 2])
    pridej_log(f"Starter: {'SERVER' if hrac == 1 else 'CLIENT'}")

reset_hry()
muj_symbol = 1
pripojeno = False

# Síť
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0", 5555))
server.listen(1)
server.setblocking(False)
klient = None

def zkontroluj_stav():
    for i in range(3):
        if pole[i][0] == pole[i][1] == pole[i][2] != 0: return pole[i][0]
        if pole[0][i] == pole[1][i] == pole[2][i] != 0: return pole[0][i]
    if pole[0][0] == pole[1][1] == pole[2][2] != 0: return pole[0][0]
    if pole[0][2] == pole[1][1] == pole[2][0] != 0: return pole[0][2]
    if all(pole[r][s] != 0 for r in range(3) for s in range(3)): return 3
    return 0

def odesli_stav():
    if pripojeno and klient:
        try:
            klient.send(pickle.dumps({"pole": pole, "konec": konec, "hrac": hrac}))
        except: pass

# --- HLAVNÍ SMYČKA ---
running = True
while running:
    if not pripojeno:
        try:
            klient, adresa = server.accept()
            klient.setblocking(False)
            pripojeno = True
            pridej_log(f"Connected: {adresa[0]}")
            odesli_stav()
        except: pass

    # --- OPRAVENÝ PŘÍJEM DAT (VALIDACE) ---
    if pripojeno:
        try:
            data = klient.recv(4096)
            if data:
                tah = pickle.loads(data)
                
                # 1. Kontrola, zda je klient na tahu
                if hrac != 2:
                    pridej_log("WARN: Client tried out of turn!", True)
                # 2. Kontrola, zda je pole volné
                elif pole[tah[0]][tah[1]] != 0:
                    pridej_log("WARN: Field already taken!", True)
                # 3. Kontrola, zda hra už neskončila
                elif konec != 0:
                    pridej_log("WARN: Game already ended!", True)
                else:
                    # Pokud je vše OK, proveď tah
                    pole[tah[0]][tah[1]] = 2
                    pridej_log(f"Client move: {tah}")
                    konec = zkontroluj_stav()
                    hrac = 1 if konec == 0 else hrac
                
                # V každém případě pošli aktuální pravdivý stav (tím klienta "opravíš")
                odesli_stav()
        except (BlockingIOError, EOFError): pass
        except: pripojeno = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_hry()
            odesli_stav()

        if event.type == pygame.MOUSEBUTTONDOWN and pripojeno and hrac == 1 and konec == 0:
            mx, my = event.pos
            if mx < 300:
                r, s = my // 100, mx // 100
                if pole[r][s] == 0:
                    pole[r][s] = 1
                    pridej_log(f"Server move: [{r},{s}]")
                    konec = zkontroluj_stav()
                    hrac = 2 if konec == 0 else hrac
                    odesli_stav()

    # Vykreslení
    okno.fill(BILA)
    for i in range(1, 3):
        pygame.draw.line(okno, CERNA, (100*i, 0), (100*i, 300), 2)
        pygame.draw.line(okno, CERNA, (0, 100*i), (300, 100*i), 2)
    
    # Symboly a terminál (zkráceno pro přehlednost)
    font = pygame.font.Font(None, 100)
    for r in range(3):
        for s in range(3):
            if pole[r][s] != 0:
                txt = font.render("X" if pole[r][s]==1 else "O", True, MODRA if pole[r][s]==1 else CERVENA)
                okno.blit(txt, txt.get_rect(center=(s*100+50, r*100+50)))

    pygame.draw.rect(okno, CERNA, (300, 0, 250, 300))
    f_term = pygame.font.SysFont("monospace", 14)
    for i, l in enumerate(logy):
        color = CERVENA if "WARN" in l else ZELENA
        okno.blit(f_term.render(f"> {l}", True, color), (310, 10 + i*20))

    pygame.display.flip()
    hodiny.tick(60)
pygame.quit()