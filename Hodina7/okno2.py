import pygame as pg
import random as r  

p_cervena = r.randint(0, 255)
p_zelena = r.randint(0, 255)
p_modra = r.randint(0, 255)
cervena = r.randint(0, 255)
zelena = r.randint(0, 255)
modra = r.randint(0, 255)


print(f"RGB({cervena}, {zelena}, {modra})")

pg.init()
obrazovka = pg.display.set_mode((600, 600))
pg.display.set_caption("Moje super trupr okno")
bezi = True


obrazovka.fill((p_cervena,p_zelena, p_modra))

while bezi:

    for udalost in pg.event.get():
        if udalost.type == pg.QUIT:
            bezi = False
    pg.draw.circle(obrazovka, (cervena,zelena,modra), (r.randint(0,600),r.randint(0,600)), r.randint(1,30))
    pg.time.delay(100)

    pg.display.flip()
pg.quit()