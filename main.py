from serpientes_escaleras import SerpientesYEscaleras

def mostrar_instrucciones():
    print("\nInstrucciones del juego:")
    print("- Si caes en una casilla PAR, deberás responder una pregunta sobre un verbo.")
    print("- Si caes en una casilla IMPAR, deberás responder una pregunta sobre un sustantivo.")
    print("Selecciona el nivel de dificultad:")
    print("1. Nivel 1 (5 oportunidades)")
    print("2. Nivel 2 (2 oportunidades)")

def main():
    print("\nBienvenido a 🐍 Serpientes y Escaleras 🪜")
    print("Este es un juego de mesa simple pero emocionante que pondrá a prueba tu suerte y estrategia.")
    print("¿Estás listo para enfrentar el desafío y escalar hacia la victoria, o caerás presa de las serpientes traicioneras? 🚀")
    juego = SerpientesYEscaleras()
    nombre_jugador = input("Ingresa tu nombre para empezar el juego: ")
    juego.nombre_jugador = nombre_jugador
    mostrar_instrucciones()
    while True:
        eleccion = input("Ingresa el número correspondiente al nivel de dificultad: ")
        if eleccion in ["1", "2"]:
            juego.dificultad = int(eleccion)
            juego.max_intentos_guardados = 5 if juego.dificultad == 1 else 2
            juego.intentos_restantes = juego.max_intentos_guardados
            break
        else:
            print("Por favor, ingresa 1 o 2.")

    while True:
        input("Presiona Enter para lanzar el dado...")
        juego.posicion_jugador = 1
        while juego.intentos_restantes > 0:
            print("\n")  # Limpiar la consola
            juego.mostrar_tablero()
            print(f"\nTu posición actual: \033[1m\033[4m{juego.posicion_jugador}\033[0m")
            pasos = juego.lanzar_dado()
            juego.mover_jugador(pasos)
            juego.verificar_puntaje()
            input("Presiona Enter para continuar...")
            if juego.posicion_jugador >= 64:
                print("¡Felicidades! Has llegado a la casilla 64 y has ganado.")
                break
        if juego.intentos_restantes <= 0 and juego.posicion_jugador < 64:
            print("¡Has agotado tus oportunidades! Mejor suerte la próxima vez.")
        juego.jugadores[juego.nombre_jugador] = {"Turnos Jugados": 1, "Puntaje": [juego.puntaje]}
        intentar_otra_vez = input("¿Quieres jugar otra ronda? (si/no): ")
        if intentar_otra_vez.lower() != "si":
            juego.mostrar_historial_jugadores()
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()
