import pygame
import random
from diseño import *

# Inicializar Pygame
pygame.init()

# Función para dibujar las escaleras y serpientes en el tablero
def dibujar_escaleras_y_serpientes():
    for inicio, fin in escaleras.items():
        inicio_fila, inicio_col = divmod(inicio - 1, 10)
        fin_fila, fin_col = divmod(fin - 1, 10)
        pygame.draw.line(pantalla, AMARILLO, (inicio_col * ANCHO_CELDA + ANCHO_CELDA // 2, (9 - inicio_fila) * ALTO_CELDA + ALTO_CELDA // 2),
                         (fin_col * ANCHO_CELDA + ANCHO_CELDA // 2, (9 - fin_fila) * ALTO_CELDA + ALTO_CELDA // 2), 5)
    for inicio, fin in serpientes.items():
        inicio_fila, inicio_col = divmod(inicio - 1, 10)
        fin_fila, fin_col = divmod(fin - 1, 10)
        pygame.draw.line(pantalla, ROJO, (inicio_col * ANCHO_CELDA + ANCHO_CELDA // 2, (9 - inicio_fila) * ALTO_CELDA + ALTO_CELDA // 2),
                         (fin_col * ANCHO_CELDA + ANCHO_CELDA // 2, (9 - fin_fila) * ALTO_CELDA + ALTO_CELDA // 2), 5)

# Función para dibujar el tablero con números en cada casilla
def dibujar_tablero(posicion_ficha):
    for fila in range(10):
        for col in range(10):
            if (fila + col) % 2 == 0:
                color = BLANCO
            else:
                color = GRIS_CLARO
            pygame.draw.rect(pantalla, color, (col * ANCHO_CELDA, fila * ALTO_CELDA, ANCHO_CELDA, ALTO_CELDA))
            # Dibujar número en la esquina superior derecha de cada casilla
            fuente = pygame.font.SysFont(None, 20)
            numero_casilla = (9 - fila) * 10 + col + 1  # Calcular número de casilla
            texto = fuente.render(str(numero_casilla), True, NEGRO)
            pantalla.blit(texto, (col * ANCHO_CELDA + ANCHO_CELDA - 20, fila * ALTO_CELDA))

# Función para dibujar el dado
def dibujar_dado(numero):
    pygame.draw.rect(pantalla, BLANCO, (ANCHO - ANCHO_DADO - 10, 10, ANCHO_DADO, ALTO_DADO))
    fuente = pygame.font.SysFont(None, 40)
    texto = fuente.render(str(numero), True, NEGRO)
    pantalla.blit(texto, (ANCHO - ANCHO_DADO // 2 - texto.get_width() // 2, ALTO_DADO // 2 - texto.get_height() // 2))

# Función para mover la ficha animadamente
def mover_ficha(posicion_inicial, posicion_final, cantidad_pasos, numero_dado):
    delta_x = (posicion_final[1] - posicion_inicial[1]) * ANCHO_CELDA // cantidad_pasos
    delta_y = (posicion_final[0] - posicion_inicial[0]) * ALTO_CELDA // cantidad_pasos
    for paso in range(cantidad_pasos):
        pantalla.fill(AZUL)
        dibujar_tablero(posicion_inicial)
        pygame.draw.circle(pantalla, FUCSIA, (posicion_inicial[1] * ANCHO_CELDA + ANCHO_CELDA // 2 + delta_x * paso,
                                               posicion_inicial[0] * ALTO_CELDA + ALTO_CELDA // 2 + delta_y * paso), 20)
        dibujar_dado(numero_dado)
        pygame.display.flip()
        pygame.time.delay(100)
    pygame.time.delay(500)

    # Verificar si la ficha está en una escalera o serpiente
    casilla_actual = posicion_final[0] * 10 + posicion_final[1] + 1
    if casilla_actual in escaleras:
        # Si la ficha está en una escalera, mover automáticamente a la casilla superior de la escalera
        nueva_posicion = [(escaleras[casilla_actual] - 1) // 10, (escaleras[casilla_actual] - 1) % 10]
        mover_ficha(posicion_final, nueva_posicion, 1, 0)  # Animación de movimiento
        posicion_final = nueva_posicion  # Actualizar la posición final de la ficha
    elif casilla_actual in serpientes:
        # Si la ficha está en una serpiente, mover automáticamente a la casilla inferior de la serpiente
        nueva_posicion = [(serpientes[casilla_actual] - 1) // 10, (serpientes[casilla_actual] - 1) % 10]
        mover_ficha(posicion_final, nueva_posicion, 1, 0)  # Animación de movimiento
        posicion_final = nueva_posicion  # Actualizar la posición final de la ficha

# Función principal del juego
def main():
    # Posición inicial de la ficha
    posicion_ficha = list(POSICION_INICIAL)
    
    # Número aleatorio inicial
    numero_dado = 1
    
    # Crear botón
    boton = pygame.Rect(ANCHO - ANCHO_DADO - 10, 70, ANCHO_DADO, ALTO_DADO)
    
    # Ciclo principal del juego
    jugando = True
    while jugando:
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1 and boton.collidepoint(evento.pos):
                    # Tirar el dado
                    numero_dado = random.randint(1, 6)
                    # Guardar posición actual de la ficha
                    posicion_actual = list(posicion_ficha)
                    # Mover la ficha animadamente
                    for _ in range(numero_dado):
                        posicion_ficha[1] += 1  # Mover hacia la derecha
                        if posicion_ficha[1] > 9:  # Si supera el límite de la columna
                            posicion_ficha[1] = posicion_ficha[1] % 10  # Reiniciar en la primera columna
                            posicion_ficha[0] -= 1  # Mover hacia arriba una fila
                    mover_ficha(posicion_actual, posicion_ficha, numero_dado, numero_dado)
                    
                    # Después de verificar si la ficha está en una escalera o serpiente
                    casilla_actual = (posicion_ficha[0] * 10) + posicion_ficha[1] + 1
                    if casilla_actual in escaleras:
                        # Si la ficha está en una escalera, avanzar automáticamente a la casilla superior de la escalera
                        nueva_posicion = [(escaleras[casilla_actual] - 1) // 10, (escaleras[casilla_actual] - 1) % 10]
                        mover_ficha(posicion_ficha, nueva_posicion, 1, 0)  # Animación de movimiento
                        posicion_ficha = nueva_posicion  # Actualizar la posición de la ficha
                    elif casilla_actual in serpientes:
                        # Si la ficha está en una serpiente, retroceder automáticamente a la casilla inferior de la serpiente
                        nueva_posicion = [(serpientes[casilla_actual] - 1) // 10, (serpientes[casilla_actual] - 1) % 10]
                        mover_ficha(posicion_ficha, nueva_posicion, 1, 0)  # Animación de movimiento
                        posicion_ficha = nueva_posicion  # Actualizar la posición de la ficha

        # Dibujar el tablero y la ficha
        pantalla.fill(AZUL)
        dibujar_tablero(posicion_ficha)
        dibujar_escaleras_y_serpientes()
        pygame.draw.circle(pantalla, FUCSIA, (posicion_ficha[1] * ANCHO_CELDA + ANCHO_CELDA // 2, posicion_ficha[0] * ALTO_CELDA + ALTO_CELDA // 2), 20)
        
        # Dibujar el dado
        dibujar_dado(numero_dado)
        
        # Dibujar el botón
        pygame.draw.rect(pantalla, FUCSIA, boton)
        
        # Actualizar pantalla
        pygame.display.flip()
        
        # Controlar la velocidad de actualización
        pygame.time.Clock().tick(30)

    # Salir de Pygame
    pygame.quit()

# Iniciar el juego
if __name__ == "__main__":
    main()
