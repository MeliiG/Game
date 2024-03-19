import pygame
from diseño import *

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Escaleras y Serpientes")

def dibujar_elementos():
    # Lista de tuplas con tres elementos: (inicio, fin, color)
    elementos = [(escaleras, AMARILLO), (serpientes, ROJO)]
    for inicio, color in elementos:
        for ini, end in inicio.items():
            ini_f, ini_c = 9 - (ini - 1) // 10, (ini - 1) % 10
            end_f, end_c = 9 - (end - 1) // 10, (end - 1) % 10
            pygame.draw.line(pantalla, color, (ini_c * ANCHO_CELDA + ANCHO_CELDA // 2, ini_f * ALTO_CELDA + ALTO_CELDA // 2),
                             (end_c * ANCHO_CELDA + ANCHO_CELDA // 2, end_f * ALTO_CELDA + ALTO_CELDA // 2), 5)

def dibujar_tablero(pos_ficha):
    for f in range(10):
        for c in range(10):
            color = BLANCO if (f + c) % 2 == 0 else GRIS_CLARO
            pygame.draw.rect(pantalla, color, (c * ANCHO_CELDA, f * ALTO_CELDA, ANCHO_CELDA, ALTO_CELDA))
            fuente = pygame.font.SysFont(None, 20)
            n_casilla = (9 - f) * 10 + c + 1
            texto = fuente.render(str(n_casilla), True, NEGRO)
            pantalla.blit(texto, (c * ANCHO_CELDA + ANCHO_CELDA - 20, f * ALTO_CELDA))
            if [f, c] == pos_ficha:
                txt_pos = fuente.render(f"Pf: {pos_ficha}", True, NEGRO)
                pantalla.blit(txt_pos, (c * ANCHO_CELDA + ANCHO_CELDA // 2 - txt_pos.get_width() // 2,
                                        (f + 1) * ALTO_CELDA - 20))

def dibujar_dado(numero):
    pygame.draw.rect(pantalla, BLANCO, (ANCHO - ANCHO_DADO - 10, 10, ANCHO_DADO, ALTO_DADO))
    fuente = pygame.font.SysFont(None, 40)
    texto = fuente.render(str(numero), True, NEGRO)
    pantalla.blit(texto, (ANCHO - ANCHO_DADO // 2 - texto.get_width() // 2, ALTO_DADO // 2 - texto.get_height() // 2))

def mover_ficha(pos_ini, pos_fin, cant_pasos, dado):
    delta_x = (pos_fin[1] - pos_ini[1]) * ANCHO_CELDA // cant_pasos
    delta_y = (pos_fin[0] - pos_ini[0]) * ALTO_CELDA // cant_pasos
    for p in range(cant_pasos):
        pantalla.fill(AZUL)
        dibujar_tablero(pos_ini)
        pygame.draw.circle(pantalla, FUCSIA, (pos_ini[1] * ANCHO_CELDA + ANCHO_CELDA // 2 + delta_x * p,
                                              pos_ini[0] * ALTO_CELDA + ALTO_CELDA // 2 + delta_y * p), 20)
        dibujar_dado(dado)
        dibujar_elementos()
        pygame.display.flip()
        pygame.time.delay(50)
    pygame.time.delay(300)

def main():
    pos_ficha = list(POSICION_INICIAL)
    dado = 1
    boton = pygame.Rect(ANCHO - ANCHO_DADO - 10, 70, ANCHO_DADO, ALTO_DADO)
    texto_ingresado = ""

    jugando = True
    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        dado = int(texto_ingresado)
                        if 1 <= dado <= 6:
                            pos_actual = list(pos_ficha)
                            for _ in range(dado):
                                pos_ficha[1] += 1
                                if pos_ficha[1] > 9:
                                    pos_ficha[1] %= 10
                                    pos_ficha[0] -= 1
                            mover_ficha(pos_actual, pos_ficha, dado, dado)
                            if pos_ficha == [9, 1]: # casilla 2  --------------->Escaleras<-------------
                                pos_ficha = [8, 2]  # casilla 13
                                mover_ficha(pos_actual, pos_ficha, 1, 0)
                            elif pos_ficha == [8, 8]: # casilla 19
                                pos_ficha = [1, 1] # casilla 82
                                mover_ficha(pos_actual, pos_ficha, 1, 0)
                            elif pos_ficha == [7, 1]: # casilla 22
                                pos_ficha = [4, 2] # casilla 53
                                mover_ficha(pos_actual, pos_ficha, 1, 0)
                            elif pos_ficha == [5, 8]: # casilla 49
                                pos_ficha = [0, 7]    # casilla 98
                                mover_ficha(pos_actual, pos_ficha, 1, 0)
                            elif pos_ficha == [3, 5]: # casilla 66
                                pos_ficha = [1, 6]    # casilla 87
                                mover_ficha(pos_actual, pos_ficha, 1, 0)
                            elif pos_ficha == [0, 9]: # casilla 100
                                mostrar_mensaje("¡Felicidades, ganaste!")
                                pygame.time.delay(2000)
                                jugando = False
                            
                            if pos_ficha == [8, 5]: # casilla 16  --------------->Serpientes<-------------
                                pos_ficha = [9, 5]  # casilla 6
                                mover_ficha(pos_actual, pos_ficha, 1, 0)
                            elif pos_ficha == [5, 2]: # casilla 43
                                pos_ficha = [6, 4] # casilla 35
                                mover_ficha(pos_actual, pos_ficha, 1, 0)
                            elif pos_ficha == [1, 8]: # casilla 89
                                pos_ficha = [9, 3] # casilla 4
                                mover_ficha(pos_actual, pos_ficha, 1, 0)
                            elif pos_ficha == [0, 2]: # casilla 93
                                pos_ficha = [3, 0] # casilla 51
                                mover_ficha(pos_actual, pos_ficha, 1, 0)
                            elif pos_ficha == [0, 4]: # casilla 95
                                pos_ficha = [6, 8] # casilla 39
                                mover_ficha(pos_actual, pos_ficha, 1, 0)
                    except ValueError:
                        print("Por favor, ingresa un número del 1 al 6.")
                    texto_ingresado = ""
                elif event.key == pygame.K_BACKSPACE:
                    texto_ingresado = texto_ingresado[:-1]
                elif event.key in range(48, 58):
                    texto_ingresado += chr(event.key)

        pantalla.fill(AZUL)
        dibujar_tablero(pos_ficha)
        dibujar_elementos()
        pygame.draw.circle(pantalla, FUCSIA, (pos_ficha[1] * ANCHO_CELDA + ANCHO_CELDA // 2, pos_ficha[0] * ALTO_CELDA + ALTO_CELDA // 2), 20)
        dibujar_dado(dado)
        pygame.draw.rect(pantalla, FUCSIA, boton)
        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()

def mostrar_mensaje(mensaje):
    fuente = pygame.font.SysFont(None, 40)
    texto = fuente.render(mensaje, True, NEGRO)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))
    pygame.display.flip()


if __name__ == "__main__":
    main()
