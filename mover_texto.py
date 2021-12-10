"""
 Sencilla demo grafica
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
# Importamos  la biblioteca de funciones llamada 'pygame'
import pygame
 
# Inicializamos el motor de juegos
pygame.init()
 
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
 
PI = 3.141592653
 
# Establecemos el alto y largo de la pantalla
dimensiones = [400, 500]
pantalla = pygame.display.set_mode(dimensiones)
 
pygame.display.set_caption("Rotar Texto")
 
# Iteramos hasta que el usuario haga click sobre el botón de salida.
hecho = False
reloj = pygame.time.Clock()
 
rotar_texto_grados = 0
 
# Iteramos mientras hecho == False
while not hecho:
 
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            hecho = True
 
    # Todo el código de dibujo ocurre después del bucle for pero
    # dentro del bucle principal while not hecho.
 
    # Limpiamos la pantalla y establecemos el color de fondo
    pantalla.fill(BLANCO)
 
    # Dibujamos algunos bordes
    pygame.draw.line(pantalla, NEGRO, [100,50], [250, 50]) 
    pygame.draw.line(pantalla, NEGRO, [100,50], [100, 200])
    pygame.draw.line(pantalla, NEGRO, [100,200], [250, 200])
    pygame.draw.line(pantalla, NEGRO, [250,50], [250, 200])
 
    # Seleccionamos la fuente de texto a usar, su tamaño, negrita, cursiva
    fuente = pygame.font.SysFont('Calibri', 25, True, False)
 
    # Texto de lado
    textoo = fuente.render("Texto de lado", True, AZUL)
    texto = pygame.transform.rotate(textoo, 90)
    pantalla.blit(texto, [0, 0])
 
    # Texto de cabeza
    texto = fuente.render("Texto de cabeza", True, VERDE)
    texto = pygame.transform.rotate(texto, 180)
    pantalla.blit(texto, [30, 0])
 
    # Texto de cabeza y de lado
    texto = fuente.render("Texto de cabeza y de lado", True, ROJO)
    texto = pygame.transform.flip(texto, False, True)
    pantalla.blit(texto, [30, 20])
 
    # Rotación en movimiento
    texto = fuente.render("Texto rotado", True, NEGRO)
    texto = pygame.transform.rotate(texto, rotar_texto_grados)
    rotar_texto_grados += 1
    pantalla.blit(texto, [100, 50])
 
    # Avancemos y actualicemos la pantalla con todo lo que hemos dibujado.
    # Esto DEBE suceder después de todos los demás comandos de dibujo.
    pygame.display.flip()
 
    # Esto limita el bucle while a un máximo de 60 veces por segundo
    # Omitimos esto y usamos toda la CPU que podamos
    reloj.tick(60)
 
# Se bueno con el IDLE
pygame.quit()