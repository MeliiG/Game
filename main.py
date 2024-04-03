from serpientes_escaleras import SerpientesYEscaleras

def main():
    juego = SerpientesYEscaleras()
    juego.mostrar_historial_jugadores()  # Mostrar historial de jugadores al inicio del juego
    while True:
        juego.jugar()
        juego.guardar_historial_jugadores()  # Guardar historial de jugadores al finalizar el juego
        juego.puntaje = 0  # Reiniciar el puntaje al iniciar un nuevo juego

if __name__ == "__main__":
    main()
