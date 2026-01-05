import pygame as p 
p.init()
screen = p.display.set_mode((800, 600))
p.display.set_caption("Ukázka textu")

font = p.font.Font(None, 64)
pozdrav = font.render("Ahoj", True, (255, 0, 0))
radek = font.render("Radek", True, (0, 255, 0))


running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    screen.blit (pozdrav, (10, 10))
    screen.blit (radek, (600, 500))
    p.display.flip()
p.quit()
