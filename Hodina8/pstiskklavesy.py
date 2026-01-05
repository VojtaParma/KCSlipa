import pygame as p 
p.init()
screen = p.display.set_mode((500, 300))
p.display.set_caption("stisk klavesy")
font = p.font.Font(None, 72)
text = ""

running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

        if event.type == p.KEYDOWN:
            text = p.key.name(event.key)
    screen.fill((30, 30, 30))
    render = font.render(text, True, (255, 255, 255))
    screen.blit(render, (100,100))
    
    p.display.flip()   
p.quit()