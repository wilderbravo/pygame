import pygame as pg
import random

from draw_module import AZUL, BLANCO, VERDE

pg.init()

ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)
VERDER = (0, 255, 0)
AZUL = (0, 0, 255)
MORADO = (128, 0, 128)

colors_random = random.randrange(0, 255)

y1 = 5
x1 = 5
color = MORADO

dimensiones = (500, 500)

pantalla = pg.display.set_mode(dimensiones)

pg.display.set_caption("Rotar texto")

hecho = False

reloj = pg.time.Clock()

while not hecho:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            hecho = True

    pantalla.fill(BLANCO)
    # Dibujamos un rectángulo sólido.    
    pg.draw.rect(pantalla, color, [x1, y1, 50, 50])
    
    myfont = pg.font.SysFont("monospace", 15)
    # render text
    label = myfont.render("Coordenadas: " + str(x1) + ":" + str(y1), 1, (255,0,0))
    # label = myfont.render("Hola", 1, (255,0,0))
    pantalla.blit(label, (160, 200))

    if x1 == 5:
        y1 += 1
        color = MORADO
    if y1==445:
        x1 +=1
        color = VERDER
    if x1 == 445:
        y1 -= 1
        color = AZUL
    if y1 == 5:
        x1 -= 1
        color = ROJO


    # pantalla.blit(pantalla, rg)

    # pg.draw.rect(pantalla, ROJO, [150, 10, 50, 20])

    pg.display.flip()
    reloj.tick(30) 

pg.quit()


# (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))