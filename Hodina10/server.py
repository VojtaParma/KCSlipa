import pygame
import socket
import pickle

# Spuštění pygame
pygame.init()
okno = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Piškvorky SERVER - Ty jsi X")

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
muj_symbol = 1  # Server je vždy X
hra_bezi = True
konec = 0

# --- SÍŤOVÁ ČÁST ---
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))  # Naslouchá na portu 5555
server.listen(1)
server.setblocking(False)  # Neblokující režim

print("Čekám na připojení klienta...")
klient = None
pripojeno = False

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
        text = maly_pismo.render("Čekám na hráče...", True, CERNA)
        okno.blit(text, (50, 10))
    elif konec != 0:
        if konec == muj_symbol:
            text = maly_pismo.render("VYHRÁL JSI!", True, MODRA)
        else:
            text = maly_pismo.render("PROHRÁL JSI!", True, CERVENA)
        okno.blit(text, (70, 130))
    elif hrac == muj_symbol:
        text = maly_pismo.render("Tvůj tah", True, MODRA)
        okno.blit(text, (100, 10))
    else:
        text = maly_pismo.render("Čekej...", True, CERVENA)
        okno.blit(text, (110, 10))

# Kontrola výhry
def zkontroluj_vyhru():
    for r in range(3):
        if pole[r][0] == pole[r][1] == pole[r][2] != 0:
            return pole[r][0]
    for s in range(3):
        if pole[0][s] == pole[1][s] == pole[2][s] != 0:
            return pole[0][s]
    if pole[0][0] == pole[1][1] == pole[2][2] != 0:
        return pole[0][0]
    if pole[0][2] == pole[1][1] == pole[2][0] != 0:
        return pole[0][2]
    return 0

# Hlavní smyčka
while hra_bezi:
    
    # Pokus o připojení klienta
    if not pripojeno:
        try:
            klient, adresa = server.accept()
            klient.setblocking(False)
            pripojeno = True
            print(f"Klient připojen: {adresa}")
        except:
            pass
    
    # Příjem dat od klienta
    if pripojeno and hrac != muj_symbol and konec == 0:
        try:
            data = klient.recv(4096)
            if data:
                tah = pickle.loads(data)  # Dostane [radek, sloupec]
                pole[tah[0]][tah[1]] = 2  # Umístí O
                konec = zkontroluj_vyhru()
                if konec == 0:
                    hrac = muj_symbol  # Přepne na serveru
                # Pošle zpět aktuální stav
                klient.send(pickle.dumps({"pole": pole, "konec": konec}))
        except:
            pass
    
    # Události
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            hra_bezi = False
        
        # Můj tah
        if udalost.type == pygame.MOUSEBUTTONDOWN and pripojeno and hrac == muj_symbol and konec == 0:
            x, y = udalost.pos
            s = x // 100
            r = y // 100
            
            if pole[r][s] == 0:
                pole[r][s] = muj_symbol  # Umístí X
                konec = zkontroluj_vyhru()
                
                # Pošle stav klientovi
                klient.send(pickle.dumps({"pole": pole, "konec": konec}))
                
                if konec == 0:
                    hrac = 2  # Přepne na klienta
    
    vykresli_vse()
    pygame.display.flip()

# Ukončení
if klient:
    klient.close()
server.close()
pygame.quit()