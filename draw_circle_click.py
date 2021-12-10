"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
 
import pygame
import random
  
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
 
def dibuja_circulo(pantalla, x, y):
    pygame.draw.ellipse(pantalla, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), [1 + x, y, 40, 40], 0)

def dibuja_puntero(pantalla, x, y):
    pygame.draw.rect(pantalla, ROJO, [1 + x, y, 50, 50], 0)
     
# Inicio
pygame.init()
   
# Establecemos el largo y alto de la pantalla [largo,alto]
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
my_list = []
pygame.display.set_caption("Movimiento de mouse")
  
#Iteramos hasta que el usuario pulsa el botón de salir.
hecho = False
  
# Usamos esto para gestionar cuán rápido se actualiza la pantalla.
reloj = pygame.time.Clock()
 
# Ocultamos el cursor del ratón.
pygame.mouse.set_visible(0)
 
# -------- Bucle Principal del Programa -----------
pantalla.fill(BLANCO)
while not hecho:
    #TODO EL PROCESAMIENTO DE EVENTOS DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    dibuja_circulo(pantalla, 300, 200)
    for evento in pygame.event.get():  # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
            hecho = True               # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos_click = pygame.mouse.get_pos()
            my_list = pos_click
            pantalla.fill(BLANCO)
            dibuja_circulo(pantalla,  my_list[0],  my_list[1])
            # pygame.draw.ellipse(pantalla, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), [1 + pos_click[0], pos_click[1], 50, 50], 0)
            pygame.display.flip()
            # print(f"El usuario hizo clic sobre la pantalla {pos_click[0]},{pos_click[1]}")
    # print(my_list)
    # dibuja_circulo(pantalla,  my_list[0],  my_list[1])
    # TODO EL PROCESAMIENTO DE EVENTOS DEBERÍA IR ENCIMA DE ESTE COMENTARIO
 
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    # Llamamos a la función que dibuja al hombre de palitos
    # pos = pygame.mouse.get_pos()
    # x = pos[0]
    # y = pos[1]

    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
 
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    
    # Primero, limpiamos la pantalla con color blanco. No pongas otros comandos de dibujo 
    # encima de esto, de lo contrario serán borrados por el comando siguiente.
    # pantalla.fill(BLANCO)
    # dibuja_puntero(pantalla, x, y)
    # # TEXTO PARA VER LAS POSICIONES DEL MOUSE
    # myfont = pygame.font.SysFont("monospace", 15)
    # label = myfont.render(str(x) + ":" + str(y), 1, (255,0,0))
    # # label_click = myfont.render(str(pos_click[0]) + ":" + str(pos_click[1]), 1, (255,0,0))
    # pantalla.blit(label, (300, 240))
    # pantalla.blit(label_click, (300, 240))
    # dibuja_circulo(pantalla, x, y)
      
    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    # pygame.display.flip()
  
    # Limitamos a 60 fotogramas por segundo
    reloj.tick(60)
      
# Pórtate bien con el IDLE.
# Si nos olvidamos de esta línea, el programa se 'colgará'
# en la salida.
pygame.quit()