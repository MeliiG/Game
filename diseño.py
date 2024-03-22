import pygame

# Definir colores
BLANCO = (255, 255, 255,128)
GRIS_CLARO = (200, 200, 200,128)
FUCSIA = (128, 0, 128)
AZUL = (64, 224, 208)
AZULL=(65, 105, 225)
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)
ROJO = (255, 0, 0)

# Definir dimensiones de la pantalla
ANCHO = 1000
ALTO = 800

# Definir tamaño de celda del tablero
ANCHO_CELDA = 80
ALTO_CELDA = 80

# Definir tamaño del dado
ANCHO_DADO = 60
ALTO_DADO = 60

# Definir posición inicial de la ficha
POSICION_INICIAL = (9, 0)

# Escaleras y Serpientes

serpientes = {24: 8, 32: 13, 39: 22, 50: 29 , 58:44}  # Diccionario de serpientes 
escaleras = {5: 12, 23: 40, 28: 43, 31: 48 , 52:62}  # Diccionario de escaleras 

 # Crear ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Escaleras y Serpientes")

MATRIZ_NUMERACION = [
    [64, 63, 62, 61, 60, 59, 58, 57],
    [49, 50, 51, 52, 53, 54, 55, 56],
    [48, 47, 46, 45, 44, 43, 42, 41],
    [33, 34, 35, 36, 37, 38, 39, 40],
    [32, 31, 30, 29, 28, 27, 26, 25],
    [17, 18, 19, 20, 21, 22, 23, 24],
    [16, 15, 14, 13, 12, 11, 10, 9],
    [1, 2, 3, 4, 5, 6, 7, 8]
]

secuencia_casillas = [
    [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7],
    [6, 7], [6, 6], [6, 5], [6, 4], [6, 3], [6, 2], [6, 1], [6, 0],
    [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7],
    [4, 7], [4, 6], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [4, 0],
    [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7],
    [2, 7], [2, 6], [2, 5], [2, 4], [2, 3], [2, 2], [2, 1], [2, 0],
    [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7],
    [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [0, 1], [0, 0]
]