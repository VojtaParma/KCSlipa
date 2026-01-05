import pygame
import socket
import pickle
import sys

# Spuštění pygame
pygame.init()
okno = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Piškvorky KLIENT - Ty jsi O")
hodiny = pygame.time.Clock()  # Pro řízení FPS

# Barvy
BILA = (255, 255, 255)
CERNA = (0, 0, 0)
MODRA = (0, 0, 255)
CERVENA = (255, 0, 0)

# Hrací pole
pole = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

hrac = 1  # Kdo je na tahu (1 = X/server, 2 = O/klient)
muj_symbol = 2  # Klient je vždy O
hra_bezi = True
konec = 0
pripojeno = False

# --- SÍŤOVÁ ČÁST ---
# ZMĚŇ "localhost" na IP adresu serveru, pokud není na stejném PC!
# Zjistíš to na serveru příkazem: ipconfig (Windows) nebo ifconfig (Linux/Mac)
print("Připojuji se k serveru...")

try:
    klient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    klient.connect(("localhost", 5555))  # Připojí se k serveru
    klient.setblocking(False)  # Neblokující režim
    pripojeno = True
    print("Připojeno k serveru!")
except ConnectionRefusedError:
    print("CHYBA: Server neběží nebo je nedostupný!")
    print("Ujisti se, že:")
    print("1. Server je spuštěný")
    print("2. IP adresa je správná")
    print("3. Oba počítače jsou na stejné síti")
    pygame.quit()
    sys.exit()
except Exception as e:
    print(f"Chyba při připojování: {e}")
    pygame.quit()
    sys.exit()

# Funkce pro vykreslení
def vykresli_vse():
    okno.fill(BILA)
    
    # Mřížka
    pygame.draw.line(okno, CERNA, (100, 0), (100, 300), 3)
    pygame.draw.line(okno, CERNA, (200, 0), (200, 300), 3)
    pygame.draw.line(okno, CERNA, (0, 100), (300, 100), 3)
    pygame.draw.line(okno, CERNA, (0, 200), (300, 200), 3)
    
    # Symboly
    pismo = pygame.font.Font(None, 100)
    for r in range(3):
        for s in range(3):
            x = s * 100 + 50
            y = r * 100 + 50
            if pole[r][s] == 1:
                text = pismo.render("X", True, MODRA)
                okno.blit(text, text.get_rect(center=(x, y)))
            elif pole[r][s] == 2:
                text = pismo.render("O", True, CERVENA)
                okno.blit(text, text.get_rect(center=(x, y)))
    
    # Hlášky
    maly_pismo = pygame.font.Font(None, 30)
    if not pripojeno:
        text = maly_pismo.render("Odpojeno od serveru!", True, CERVENA)
        okno.blit(text, (40, 130))
    elif konec != 0:
        if konec == muj_symbol:
            text = maly_pismo.render("VYHRÁL JSI!", True, CERVENA)
        else:
            text = maly_pismo.render("PROHRÁL JSI!", True, MODRA)
        okno.blit(text, (70, 130))
    elif hrac == muj_symbol:
        text = maly_pismo.render("Tvůj tah", True, CERVENA)
        okno.blit(text, (100, 10))
    else:
        text = maly_pismo.render("Čekej...", True, MODRA)
        okno.blit(text, (110, 10))

# Hlavní smyčka
while hra_bezi:
    
    # Příjem dat od serveru
    if pripojeno:
        try:
            data = klient.recv(4096)
            if data:
                stav = pickle.loads(data)
                pole = stav["pole"]
                konec = stav["konec"]
                if konec == 0:
                    hrac = muj_symbol  # Přepne na klienta
        except BlockingIOError:
            pass  # Žádná data k přečtení, ignoruj
        except ConnectionResetError:
            print("Server se odpojil")
            pripojeno = False
        except EOFError:
            print("Server ukončil spojení")
            pripojeno = False
        except Exception as e:
            print(f"Chyba při příjmu dat: {e}")
    
    # Události
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            hra_bezi = False
        
        # Můj tah
        if udalost.type == pygame.MOUSEBUTTONDOWN and pripojeno and hrac == muj_symbol and konec == 0:
            x, y = udalost.pos
            s = x // 100
            r = y // 100
            
            if 0 <= r < 3 and 0 <= s < 3 and pole[r][s] == 0:
                pole[r][s] = muj_symbol  # Umístí O lokálně
                
                # Pošle tah serveru
                try:
                    klient.send(pickle.dumps([r, s]))
                    hrac = 1  # Přepne na server
                except BrokenPipeError:
                    print("Spojení přerušeno")
                    pripojeno = False
                except Exception as e:
                    print(f"Chyba při posílání tahu: {e}")
                    pripojeno = False
    
    vykresli_vse()
    pygame.display.flip()
    hodiny.tick(100)  # 100 FPS

# Ukončení
if pripojeno:
    try:
        klient.close()
    except:
        pass
pygame.quit()
print("Klient ukončen")