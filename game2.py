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
#imagen_serpiente = pygame.image.load(os.path.join("imagenes", "snake.png")).convert_alpha()
imagen_tablero = pygame.image.load(os.path.join("imagenes", "tablero1.png")).convert_alpha()  # Cargar la imagen del tablero
imagen_tablero = pygame.transform.scale(imagen_tablero, (ANCHO_CELDA * 8, ALTO_CELDA * 8))  # Ajustar el tamaño de la imagen del tablero

POSICION_INICIAL = [7, 0]

def dibujar_tablero(pos_ficha):
    fuente = pygame.font.SysFont(None, 20)  # Definir la fuente fuera del bucle for
    for f in range(8):
        for c in range(8):
            color = BLANCO if (f + c) % 2 == 0 else GRIS_CLARO
            rect = pygame.Rect(c * ANCHO_CELDA, f * ALTO_CELDA, ANCHO_CELDA, ALTO_CELDA)
            if color == BLANCO or color == GRIS_CLARO:
                pygame.draw.rect(pantalla, color, rect)
            else:
                n_casilla = (7 - f) * 8 + c + 1
                texto = fuente.render(str(n_casilla), True, NEGRO)
                pantalla.blit(texto, (c * ANCHO_CELDA + ANCHO_CELDA - 20, f * ALTO_CELDA))
            if [f, c] == pos_ficha:
                txt_pos = fuente.render(f"Pf: {pos_ficha}", True, NEGRO)
                pantalla.blit(txt_pos, (c * ANCHO_CELDA + ANCHO_CELDA // 2 - txt_pos.get_width() // 2,
                                        (f + 1) * ALTO_CELDA - 20))
    
    # Dibujar la imagen del tablero encima del tablero de 8x8
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

    # Cargar la imagen correspondiente al número del dado
    imagen_dado = imagenes_dado[numero - 1]  # Restar 1 porque los índices comienzan desde 0
    imagen_dado = pygame.transform.scale(imagen_dado, (dado_ancho, dado_alto))
    pantalla.blit(imagen_dado, (dado_x, dado_y))

def mover_ficha(pos_ini, pos_fin, cant_pasos, dado):
    # Calcular el número máximo de pasos permitidos para llegar a la casilla final
    pasos_hasta_fin = pos_ini[1] - pos_fin[1] if pos_ini[0] == pos_fin[0] else (pos_ini[0] - pos_fin[0]) * 8 + (7 - pos_fin[1]) + 1
    
    # Ajustar la cantidad de pasos si es mayor que el máximo permitido
    cant_pasos = min(cant_pasos, pasos_hasta_fin)
    
    # Calcular los deltas para el movimiento
    delta_x = (pos_fin[1] - pos_ini[1]) * ANCHO_CELDA // cant_pasos
    delta_y = (pos_fin[0] - pos_ini[0]) * ALTO_CELDA // cant_pasos
    
    for p in range(cant_pasos):
        pantalla.fill(AZUL)
        dibujar_tablero(pos_ini)
        pygame.draw.circle(pantalla, FUCSIA, (pos_ini[1] * ANCHO_CELDA + ANCHO_CELDA // 2 + delta_x * p,
                                              pos_ini[0] * ALTO_CELDA + ALTO_CELDA // 2 + delta_y * p), 20)
        dibujar_dado(dado)
        pygame.display.flip()
        pygame.time.delay(50)
    # Ajuste final para asegurarse de que la ficha esté en la posición final exacta
    pantalla.fill(AZUL)
    dibujar_tablero(pos_fin)
    pygame.draw.circle(pantalla, FUCSIA, (pos_fin[1] * ANCHO_CELDA + ANCHO_CELDA // 2, pos_fin[0] * ALTO_CELDA + ALTO_CELDA // 2), 20)
    dibujar_dado(dado)
    pygame.display.flip()
    pygame.time.delay(300)
    
    

# Función principal del juego
def main():
    pos_ficha = list(POSICION_INICIAL)
    boton = pygame.Rect(ANCHO - ANCHO_DADO - 100, 70, ANCHO_DADO, ALTO_DADO)
    dado = 1
    mensaje_mostrado = False  # Variable para verificar si el mensaje final ya se ha mostrado

    jugando = True
    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton.collidepoint(event.pos):
                    dado = random.randint(1, 6)
                    pos_actual = list(pos_ficha)
                    for _ in range(dado):
                        pos_ficha[1] += 1
                        if pos_ficha[1] > 7:
                            pos_ficha[1] %= 8
                            pos_ficha[0] -= 1
                    mover_ficha(pos_actual, pos_ficha, dado, dado)
                    
                    # Verificar si la ficha ha llegado a una casilla especial
                    if pos_ficha == [7, 4]: # Casilla 5 ----------------------------->(Escaleras)
                        pos_ficha = [6, 4]  # Casilla 13
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [5, 6]: # Casilla 23 
                        pos_ficha = [3, 7] # Casilla 40
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [4, 1]: # Casilla 26 
                        pos_ficha = [2, 0] # Casilla 41
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [4, 4]: # Casilla 29 
                        pos_ficha = [2, 5] # Casilla 46
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [1, 3]: # Casilla 52 
                        pos_ficha = [0, 2] # Casilla 59
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    
                    if pos_ficha == [5, 7]: # Casilla 24 ----------------------------->(Serpientes)
                        pos_ficha = [7, 7]  # Casilla 8
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [4, 0]: # Casilla 25 
                        pos_ficha = [6, 3] # Casilla 12
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [3, 6]: # Casilla 39 
                        pos_ficha = [5, 5] # Casilla 22
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [1, 1]: # Casilla 50
                        pos_ficha = [4, 3] # Casilla 28
                        mover_ficha(pos_actual, pos_ficha, 1, 0)
                    elif pos_ficha == [0, 6]: # Casilla 63 
                        pos_ficha = [2, 4] # Casilla 45
                        mover_ficha(pos_actual, pos_ficha, 1, 0)    
                        
                    
                
                
                # Verificar si se alcanzó la posición final
                if pos_ficha == [0, 7] and not mensaje_mostrado:  
                    pantalla.fill(AZUL)
                    mensaje_final = fuente.render("¡Felicidades, has ganado!", True, BLANCO)
                    pantalla.blit(mensaje_final, (ANCHO // 2 - mensaje_final.get_width() // 2, ALTO // 2 - mensaje_final.get_height() // 2))
                    pygame.display.flip()
                    pygame.time.delay(2000)  
                    mensaje_mostrado = True  
                    jugando = False  

        pantalla.fill(AZUL)
        pygame.draw.circle(pantalla, FUCSIA, (pos_ficha[1] * ANCHO_CELDA + ANCHO_CELDA // 2, pos_ficha[0] * ALTO_CELDA + ALTO_CELDA // 2), 20)
        dibujar_dado(dado)
        dibujar_tablero(pos_ficha)  
        pygame.draw.rect(pantalla, FUCSIA, boton)
        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
