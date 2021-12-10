"""
Este es un programa que permite mover un texto en pantalla.
"""
from typing import NewType
import pygame as pg

from draw_module import NEGRO

pg.init()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

PI = 3.141592653
rotar_texto_grados = 0

dimensiones = [400, 500]

pantalla = pg.display.set_mode(dimensiones)

pg.display.set_caption("Rotar texto")

hecho = False

reloj = pg.time.Clock()

while not hecho:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            hecho = True

    pantalla.fill(BLANCO)

    pg.draw.line(pantalla, NEGRO, [100,50], [250,50])
    pg.draw.line(pantalla, NEGRO, [100,50], [100,200])
    pg.draw.line(pantalla, NEGRO, [100,200], [250,200])
    pg.draw.line(pantalla, NEGRO, [250,50], [250,200])

    fuente = pg.font.SysFont('Calibri', 25, True, False)

    # Texto de lado
    texto = fuente.render("Texto de lado", True, AZUL)
    texto = pg.transform.rotate(texto, 90)
    pantalla.blit(texto, [0,0])
    
    # Texto de cabeza
    texto = fuente.render("Texto de cabeza", True, VERDE)
    texto = pg.transform.rotate(texto, 180)
    pantalla.blit(texto, [30,0])
    
    # Texto de cabeza y de lado
    texto = fuente.render("Texto de cabeza y de lado", True, ROJO)
    texto = pg.transform.flip(texto, False, True)
    pantalla.blit(texto, [30,20])

    # Rotación en movimiento
    texto = fuente.render("Texto rotado", True, NEGRO)
    texto = pg.transform.rotate(texto, rotar_texto_grados)
    rotar_texto_grados += 2
    pantalla.blit(texto, [100,50])

    pg.display.flip()

    reloj.tick(60) 

pg.quit()   