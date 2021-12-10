# https://openwebinars.net/blog/como-hacer-un-juego-con-pygame-en-10-minutos/
# https://realpython.com/pygame-a-primer/

import pygame as pg

pg.init()
# Colors = (R, G, B)
# Constantes
FONDO = (255,255,255)
ROJO = (255,0,0)
AZUL = (0,0,255)
AMARILLO = (255,255,0)
VERDE = (0,255,0)
MORADO = (128,0,128)
CAFE = (139,69,19)

#Variables
x, y = 350, 250
dimen_cuad = 50
x_derecha = (800 - dimen_cuad - 10) 
x_izquierda, y_arriba = 10
y_abajo = (600 - dimen_cuad - 10)

pantalla = pg.display.set_mode((800,600))

ejecuta = True

while ejecuta:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            ejecuta = False
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_LEFT:
                x = x - 5
            if evento.key == pg.K_RIGHT:
                x = x + 5
            if evento.key == pg.K_UP:
                y = y - 5
            if evento.key == pg.K_DOWN:
                y = y + 5
        pg.draw.rect(pantalla,MORADO,(x,y,100,100))

    pantalla.fill(FONDO)
    
    

    pg.draw.rect(pantalla,MORADO,(x,y,dimen_cuad,dimen_cuad))
    pg.draw.rect(pantalla,ROJO,(x_derecha,y_abajo,dimen_cuad,dimen_cuad))
    pg.draw.rect(pantalla,AZUL,(x_izquierda,y_abajo,dimen_cuad,dimen_cuad))
    pg.draw.rect(pantalla,AMARILLO,(x_izquierda,y_arriba,dimen_cuad,dimen_cuad))
    pg.draw.rect(pantalla,VERDE,(x_derecha,y_arriba,dimen_cuad,dimen_cuad))
    pg.display.flip()

pg.quit()

