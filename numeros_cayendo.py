import pygame as pg
import random

pg.init()

numbers = [0, 1, 2 ,3, 4, 5, 6, 7, 8, 9]
x, y = 0, 0
pantalla = pg.display.set_mode((500, 500))
hecho = True
reloj = pg.time.Clock()

lista_posiciones = []
 
# Iteramos 50 veces y añadimos un copo de nieve en una ubicación (x,y) aleatoria.
for i in range(50):
    x = random.randrange(0, 400)
    lista_posiciones.append(x)

while hecho:   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            hecho = False
    
    pantalla.fill((255, 255, 255))
    
    numero_aleatorio = random.choice(numbers)
    x = random.randint(0, 400)
    myfont = pg.font.SysFont("monospace", 25)
    texto = myfont.render(f"{numero_aleatorio}", 4, (255,0,0))
    for i in range(1, 500):
        pantalla.blit(texto, (x, i))

    # for i in range(len(lista_posiciones)):
    
    #     # Dibujamos el copo de nieve
    #     numero_aleatorio = random.choice(numbers)
    #     myfont = pg.font.SysFont("monospace", 15)
    #     texto = myfont.render(f"{numero_aleatorio}", 2, (255,0,0))
    #     pantalla.blit(texto, x, y)
    #     # pg.draw.circle(pantalla, BLANCO, lista_nieve[i], 2)
         
    #     # Desplazamos un píxel hacia abajo el copo de nieve.
    #     lista_posiciones[i][1] += 1
         
    #     # Si el copo se escapa del fondo de la pantalla.
    #     if lista_posiciones[i][1] > 400:
    #         # Lo movemos justo encima del todo
    #         y = random.randrange(-50, -10)
    #         lista_posiciones[i][1] = y
    #         # Le damos una nueva ubicación x
    #         x = random.randrange(0, 400)
    #         lista_posiciones[i][0] = x
    
    reloj.tick(1)
    pg.display.flip()