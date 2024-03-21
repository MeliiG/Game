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

serpientes = {24: 8, 25: 12, 39: 22, 50: 28 , 63:45}  # Diccionario de serpientes con el tablero hecho
escaleras = {5: 13, 23: 40, 26: 41, 29: 46 , 52:59}  # Diccionario de escaleras con el tablero hecho

 
#escaleras = {2: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
#serpientes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}

# Crear ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Escaleras y Serpientes")