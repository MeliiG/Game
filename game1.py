import pygame
import random
import os
from diseño import *

pygame.init()
fuente = pygame.font.SysFont(None, 20) 
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Escaleras y Serpientes")



def cargar_imagenes_dado():
    imagenes = []
    for i in range(1, 7):
        ruta = os.path.join("imagenes", f"{i}.jpg")
        imagen = pygame.image.load(ruta).convert_alpha()
        imagenes.append(imagen)
    return imagenes

imagenes_dado = cargar_imagenes_dado()
imagen_tablero = pygame.image.load(os.path.join("imagenes", "Tablero.png")).convert_alpha()  # Cargar la imagen del tablero
imagen_tablero = pygame.transform.scale(imagen_tablero, (ANCHO_CELDA * 8, ALTO_CELDA * 8)) # Ajustar el tamaño de la imagen del tablero
musica_fondo = pygame.mixer.Sound(os.path.join("imagenes", "music.mp3"))  

# Función para reproducir la música de fondo
def reproducir_musica():
    pygame.mixer.music.load(os.path.join("imagenes", "music.mp3"))  
    pygame.mixer.music.play(-1)  # El argumento -1 indica que la música se repetirá indefinidamente

POSICION_INICIAL = [7, 0]

def dibujar_tablero(pos_ficha):
    fuente = pygame.font.SysFont(None, 20)
    for f in range(8):  
        for c in range(8):
            num_casilla = MATRIZ_NUMERACION[f][c]
            color = BLANCO if (f + c) % 2 == 0 else GRIS_CLARO
            rect = pygame.Rect(c * ANCHO_CELDA, f * ALTO_CELDA, ANCHO_CELDA, ALTO_CELDA)
            pygame.draw.rect(pantalla, color, rect)
            texto = fuente.render(str(num_casilla), True, NEGRO)
            text_rect = texto.get_rect(topright=(rect.x + rect.width - 5, rect.y + 5))
            pantalla.blit(texto, text_rect)
            
    pantalla.blit(imagen_tablero, (0, 0))  # Ajusta las coordenadas según sea necesario
    pygame.draw.circle(pantalla, FUCSIA, (pos_ficha[1] * ANCHO_CELDA + ANCHO_CELDA // 2, pos_ficha[0] * ALTO_CELDA + ALTO_CELDA // 2), 20)
    # Mostrar la posición actual de la ficha debajo de la ficha misma
    txt_pos_ficha = fuente.render(f"Pos: {pos_ficha}", True, AZULL)
    pantalla.blit(txt_pos_ficha, (pos_ficha[1] * ANCHO_CELDA + ANCHO_CELDA // 2 - txt_pos_ficha.get_width() // 2,
                                  (pos_ficha[0] + 1) * ALTO_CELDA + 10))


def dibujar_dado(numero):
    dado_ancho = 70
    dado_alto = 70
    dado_x = ANCHO - ANCHO_DADO - 200
    dado_y = 70

    imagen_dado = imagenes_dado[numero - 1]
    imagen_dado = pygame.transform.scale(imagen_dado, (dado_ancho, dado_alto))
    pantalla.blit(imagen_dado, (dado_x, dado_y))




def mover_ficha(pos_ini, pos_fin, cant_pasos, dado):
    delta_x = (pos_fin[1] - pos_ini[1]) * ANCHO_CELDA
    delta_y = (pos_fin[0] - pos_ini[0]) * ALTO_CELDA
    paso_x = delta_x / cant_pasos
    paso_y = delta_y / cant_pasos

    pos_actual = list(pos_ini)
    for _ in range(cant_pasos):
        pos_actual[0] += paso_y
        pos_actual[1] += paso_x

        pantalla.fill(AZUL)
        dibujar_tablero(pos_ini)  # Dibujar el tablero con la posición inicial
        pygame.draw.circle(pantalla, FUCSIA, (int(pos_actual[1] * ANCHO_CELDA + ANCHO_CELDA // 2), int(pos_actual[0] * ALTO_CELDA + ALTO_CELDA // 2)), 20)
        dibujar_dado(dado)
        pygame.display.flip()
        pygame.time.delay(10)

    pantalla.fill(AZUL)
    dibujar_tablero(pos_fin)  # Dibujar el tablero con la posición final
    pygame.draw.circle(pantalla, FUCSIA, (pos_fin[1] * ANCHO_CELDA + ANCHO_CELDA // 2, pos_fin[0] * ALTO_CELDA + ALTO_CELDA // 2), 20)
    dibujar_dado(dado)
    pygame.display.flip()
    pygame.time.delay(300)

# Función principal del juego
def main():
    reproducir_musica()
    pos_ficha = list(POSICION_INICIAL)
    boton = pygame.Rect(ANCHO - ANCHO_DADO - 100, 70, ANCHO_DADO, ALTO_DADO)
    mensaje_mostrado = False  

    jugando = True
    
    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton.collidepoint(event.pos):
                    dado = random.randint(1, 6)
                    pos_actual = list(pos_ficha)
                    pos_destino = pos_actual
                    for _ in range(dado):
                        if pos_destino in secuencia_casillas:
                            idx = secuencia_casillas.index(pos_destino)
                            if idx < len(secuencia_casillas) - 1:
                                pos_destino = secuencia_casillas[idx + 1]
                    mover_ficha(pos_actual, pos_destino, 1, dado)
                    pos_ficha = pos_destino
                    # Verificar si la ficha ha llegado a una casilla especial
                    if pos_ficha == [7, 4]: # Casilla 5 ----------------------------->(Escaleras)
                        pos_ficha = [6, 4]  # Casilla 12..
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [5, 6]: # Casilla 23 
                        pos_ficha = [3, 7] # Casilla 40..
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [4, 4]: # Casilla 28
                        pos_ficha = [2, 5] # Casilla 43..
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [4, 1]: # Casilla 31
                        pos_ficha = [2, 0] # Casilla 48..
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [1, 3]: # Casilla 52 
                        pos_ficha = [0, 2] # Casilla 62..
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    
                    if pos_ficha == [5, 7]: # Casilla 24 ----------------------------->(Serpientes)
                        pos_ficha = [7, 7]  # Casilla 8..
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [4, 0]: # Casilla 32 
                        pos_ficha = [6, 3] # Casilla 13..
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [3, 6]: # Casilla 39 
                        pos_ficha = [5, 5] # Casilla 22..
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [1, 1]: # Casilla 50
                        pos_ficha = [4, 3] # Casilla 29
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [0, 6]: # Casilla 58 
                        pos_ficha = [2, 4] # Casilla 44
                        mover_ficha(pos_actual, pos_ficha, 1, 0)  
                    
                    if pos_ficha == [0, 0] and not mensaje_mostrado:  
                        pantalla.fill(AZUL)
                        mensaje_final = fuente.render("¡Felicidades, has ganado!", True, BLANCO)
                        pantalla.blit(mensaje_final, (ANCHO // 2 - mensaje_final.get_width() // 2, ALTO // 2 - mensaje_final.get_height() // 2))
                        pygame.display.flip()
                        pygame.time.delay(2000)  
                        mensaje_mostrado = True  
                        jugando = False  

        pantalla.fill(AZUL)
        dibujar_tablero(pos_ficha)  
        pygame.draw.rect(pantalla, FUCSIA, boton)
        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()


