import pygame

# Definir colores
BLANCO = (255, 255, 255)
GRIS_CLARO = (200, 200, 200)
FUCSIA = (255, 0, 255)
AZUL = (64, 224, 208)
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

serpientes = {16:6 , 43:35 , 89:4  , 93:61 , 95:39 }
escaleras = {2:13, 19:82 , 22:53 , 66:87 , 49:98 }  
#escaleras = {2: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
#serpientes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}

# Crear ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Escaleras y Serpientes")