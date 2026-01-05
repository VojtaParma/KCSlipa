import pygame
import socket
import pickle

# Nastavení okna (stejné jako u serveru pro konzistenci, ale bez terminálu)
pygame.init()
okno = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Piškvorky KLIENT - Ty jsi O")
hodiny = pygame.time.Clock()

# Barvy
BILA = (255, 255, 255)
CERNA = (0, 0, 0)
MODRA = (0, 0, 255)
CERVENA = (255, 0, 0)

# Herní proměnné
pole = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
hrac = 0
muj_symbol = 2 # Klient je vždy O
konec = 0
pripojeno = False

# --- SÍŤOVÁ ČÁST ---
klient_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # IP adresa "127.0.0.1" znamená, že klient běží na stejném PC jako server
    klient_socket.connect(("127.0.0.1", 5555))
    klient_socket.setblocking(False)
    pripojeno = True
    print("Připojeno k serveru!")
except Exception as e:
    print(f"Nepodařilo se připojit: {e}")

def vykresli_vse():
    okno.fill(BILA)
    for i in range(1, 3):
        pygame.draw.line(okno, CERNA, (100 * i, 0), (100 * i, 300), 3)
        pygame.draw.line(okno, CERNA, (0, 100 * i), (300, 100 * i), 3)
    
    pismo = pygame.font.Font(None, 100)
    for r in range(3):
        for s in range(3):
            x, y = s * 100 + 50, r * 100 + 50
            if pole[r][s] == 1:
                text = pismo.render("X", True, MODRA)
                okno.blit(text, text.get_rect(center=(x, y)))
            elif pole[r][s] == 2:
                text = pismo.render("O", True, CERVENA)
                okno.blit(text, text.get_rect(center=(x, y)))

    # Stavové hlášky
    maly_pismo = pygame.font.Font(None, 30)
    if konec != 0:
        msg = "REMIZA!" if konec == 3 else ("VYHRÁL JSI!" if konec == muj_symbol else "PROHRÁL JSI!")
        text = maly_pismo.render(msg, True, CERNA)
        okno.blit(text, (10, 10))
    elif hrac == muj_symbol:
        text = maly_pismo.render("Tvůj tah (O)", True, CERVENA)
        okno.blit(text, (10, 10))
    else:
        text = maly_pismo.render("Čekej na server...", True, MODRA)
        okno.blit(text, (10, 10))

# Hlavní smyčka klienta
bezi = True
while bezi:
    # 1. Příjem dat ze serveru (Stav pole, kdo je na tahu, konec)
    if pripojeno:
        try:
            data = klient_socket.recv(4096)
            if data:
                stav = pickle.loads(data)
                pole = stav["pole"]
                konec = stav["konec"]
                hrac = stav["hrac"]
        except (BlockingIOError, EOFError): pass
        except Exception as e:
            print(f"Ztráta spojení: {e}")
            pripojeno = False

    # 2. Události
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False
        
        # Ošetření tahu klienta
        if udalost.type == pygame.MOUSEBUTTONDOWN and pripojeno and hrac == muj_symbol and konec == 0:
            x, y = udalost.pos
            r, s = y // 100, x // 100
            
            if 0 <= r < 3 and 0 <= s < 3 and pole[r][s] == 0:
                try:
                    # 1. ODESLAT TAH
                    klient_socket.send(pickle.dumps([r, s]))
                    
                    # 2. LOKÁLNÍ ZÁMEK (Zabrání dvojkliku)
                    # Nastavíme hrac na 0, což není ani náš symbol, ani symbol soupeře
                    # Tím se zablokuje podmínka "hrac == muj_symbol" pro další kliky
                    hrac = 0 
                    
                    # 3. VOLITELNÉ: Můžeš si i lokálně dočasně vykreslit symbol, 
                    # aby hra působila plynule, ale jistější je počkat na server.
                    # pole[r][s] = muj_symbol 
                    
                except Exception as e:
                    print(f"Chyba při odesílání: {e}")

    vykresli_vse()
    pygame.display.flip()
    hodiny.tick(1000)

pygame.quit()