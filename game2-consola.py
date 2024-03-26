import random

class SerpientesYEscaleras:
    """Clase que implementa el juego de Serpientes y Escaleras."""
    def __init__(self):
        self.tablero = self.crear_tablero()
        self.serpientes = {20: 6, 29: 10, 38: 13, 52: 25}  # Definir las serpientes
        self.escaleras = {4: 22, 14: 32, 36: 60, 35: 53}  # Definir las escaleras
        self.jugadores = {}  # Inicializar el diccionario de jugadores
        self.posicion_jugador = 1  # Inicializar posición del jugador en 1
        self.dificultad = None
        self.max_intentos = None
        self.max_intentos_guardados = None  # Variable para almacenar el número máximo de intentos
        self.puntaje = 0
        self.intentos_restantes = None
        self.preguntas = {
            "sustantivos": [
                ("¿Qué cosa se usa para escribir en un papel?", "lápiz"),("¿Qué objeto usas para cortar el césped?", "guadaña"),("¿Qué cosa se usa para secar el cuerpo después de bañarse?", "toalla"),
                ("¿Qué objeto se usa para abrir puertas?", "llave"),("¿Qué cosa se usa para llevar libros a la escuela?", "maleta"),("¿Qué objeto se usa para tomar fotografías?", "cámara"),
                ("¿Qué cosa se usa para enfriar alimentos y bebidas?", "nevera"),("¿Qué objeto se usa para cortar el pelo?", "tijera"),("¿Qué cosa se usa para jugar al fútbol?", "balón"),
                ("¿Qué objeto se usa para cortar el pan?", "cuchillo"),("¿Qué cosa se usa para limpiar el suelo?", "escoba")
            ],
            "verbos": [
                ("¿Qué acción realizas cuando te lavas las manos?", "lavarse"),("¿Qué acción realizas cuando te cepillas los dientes?", "cepillarse"),("¿Qué acción realizas cuando te peinas el cabello?", "peinarse"),
                ("¿Qué acción realizas cuando te bañas en la ducha?", "bañarse"),("¿Qué acción realizas cuando cocinas la cena?", "cocinar"),("¿Qué acción realizas cuando limpias el suelo?", "limpiar"),
                ("¿Qué acción realizas cuando juegas con un balón?", "jugar"),("¿Qué acción realizas cuando cortas verduras?", "cortar"),("¿Qué acción realizas cuando corres en el parque?", "correr"),
                ("¿Qué acción realizas cuando escuchas música?", "escuchar"),("¿Qué acción realizas cuando lees un libro?", "leer")
            ]
        }
        self.historial_jugadores = []  # Historial de jugadores
        self.cargar_historial_jugadores()  # Cargar historial de jugadores al inicio

    def crear_tablero(self):
        """Crea un tablero de 8x8 con números del 1 al 64."""
        tablero = []
        contador = 1  # Contador inicializado en 1
        for i in range(8):
            fila = []
            for _ in range(8):
                fila.append(contador)
                contador += 1  # Incrementar el contador
            if i % 2 != 0:
                fila.reverse()
            tablero.append(fila)
        return tablero

    def elegir_dificultad(self):
        """Permite al jugador elegir el nivel de dificultad y mostrar las instrucciones del juego."""
        self.nombre_jugador = input("Ingresa tu nombre para empezar el juego: ")
        print("\nInstrucciones del juego:")
        print("- Si caes en una casilla PAR, deberás responder una pregunta sobre un verbo.")
        print("- Si caes en una casilla IMPAR, deberás responder una pregunta sobre un sustantivo.")
        print("Selecciona el nivel de dificultad:")
        print("1. Nivel 1 (5 oportunidades)")
        print("2. Nivel 2 (2 oportunidades)")
        while True:
            eleccion = input("Ingresa el número correspondiente al nivel de dificultad: ")
            if eleccion in ["1", "2"]:
                self.dificultad = int(eleccion)
                self.max_intentos_guardados = 5 if self.dificultad == 1 else 2
                self.intentos_restantes = self.max_intentos_guardados  # Actualizar intentos restantes
                break
            else:
                print("Por favor, ingresa 1 o 2.")

    def mostrar_tablero(self):
        """Imprime el tablero y el puntaje actual del jugador."""
        tablero_copia = [fila[:] for fila in self.tablero]  # Copia del tablero original
        fila_jugador, col_jugador = divmod(self.posicion_jugador - 1, 8)  # Fila y columna del jugador
        # Si la fila es impar, invertir la columna
        if fila_jugador % 2 != 0:
            col_jugador = 7 - col_jugador
        # Reemplazar las serpientes y escaleras en el tablero con letras
        for cabeza_serpiente, cola_serpiente in self.serpientes.items():
            fila_cabeza, col_cabeza = divmod(cabeza_serpiente - 1, 8)
            fila_cola, col_cola = divmod(cola_serpiente - 1, 8)
            if fila_cabeza % 2 != 0:
                col_cabeza = 7 - col_cabeza
            if fila_cola % 2 != 0:
                col_cola = 7 - col_cola
            tablero_copia[fila_cabeza][col_cabeza] = " X "
            tablero_copia[fila_cola][col_cola] = " x "
        for base_escalera, cima_escalera in self.escaleras.items():
            fila_base, col_base = divmod(base_escalera - 1, 8)
            fila_cima, col_cima = divmod(cima_escalera - 1, 8)
            if fila_base % 2 != 0:
                col_base = 7 - col_base
            if fila_cima % 2 != 0:
                col_cima = 7 - col_cima
            tablero_copia[fila_base][col_base] = " W "
            tablero_copia[fila_cima][col_cima] = " w "                
        tablero_copia[fila_jugador][col_jugador] = "\033[95m ★ \033[0m" # del jugador en el tablero copiado con un triángulo
        
        for fila in reversed(tablero_copia): # Imprimir el tablero en orden ascendente
            fila_str = "|".join(str(celda).center(3) for celda in fila)
            print(fila_str)
            print("-" * len(fila_str))
        print(f"Puntaje actual : {self.puntaje}")# Mostrar el puntaje actual del jugador
        print(f"Intentos restantes: {self.intentos_restantes}")  # Mostrar intentos restantes

    def lanzar_dado(self):
        """Simula tirar un dado y muestra la cara del dado."""
        numero = random.randint(1, 6)
        caras_dado = [
    ["\033[95m-------\033[0m", "\033[95m|     |\033[0m", "\033[95m|  o  |\033[0m", "\033[95m|     |\033[0m", "\033[95m-------\033[0m"],
    ["\033[95m-------\033[0m", "\033[95m|    o|\033[0m", "\033[95m|     |\033[0m", "\033[95m|o    |\033[0m", "\033[95m-------\033[0m"],
    ["\033[95m-------\033[0m", "\033[95m|o    |\033[0m", "\033[95m|  o  |\033[0m", "\033[95m|    o|\033[0m", "\033[95m-------\033[0m"],
    ["\033[95m-------\033[0m", "\033[95m|o   o|\033[0m", "\033[95m|     |\033[0m", "\033[95m|o   o|\033[0m", "\033[95m-------\033[0m"],
    ["\033[95m-------\033[0m", "\033[95m|o   o|\033[0m", "\033[95m|  o  |\033[0m", "\033[95m|o   o|\033[0m", "\033[95m-------\033[0m"],
    ["\033[95m-------\033[0m", "\033[95m|o   o|\033[0m", "\033[95m|o   o|\033[0m", "\033[95m|o   o|\033[0m", "\033[95m-------\033[0m"]
]

        for linea in caras_dado[numero - 1]:
            print(linea)
        print(f"Has sacado un {numero}:")
        return numero

    def mover_jugador(self, pasos):
        """Mueve al jugador y gestiona las serpientes y escaleras."""
        self.posicion_jugador += pasos
        if self.posicion_jugador in self.serpientes:
            print(f"¡Oh no! Caíste en una serpiente y retrocedes a la casilla {self.serpientes[self.posicion_jugador]}")
            self.posicion_jugador = self.serpientes[self.posicion_jugador]
        elif self.posicion_jugador in self.escaleras:
            print(f"¡Felicidades! Subiste por una escalera y avanzas a la casilla {self.escaleras[self.posicion_jugador]}")
            self.posicion_jugador = self.escaleras[self.posicion_jugador]
        
        # Verificar el tipo de pregunta según el nivel de dificultad y la posición del jugador
        if self.dificultad == 2:
            if self.posicion_jugador in [8, 16, 24, 32, 36, 44, 48, 56, 58, 60, 64]:
                self.hacer_pregunta("verbos")
            elif self.posicion_jugador in [5, 9, 15, 21, 31, 33, 39, 47, 51, 57, 61]:
                self.hacer_pregunta("sustantivos")
        elif self.dificultad == 1:
            if self.posicion_jugador in [8, 16, 24, 32]:
                self.hacer_pregunta("verbos")
            elif self.posicion_jugador in [5, 9, 15, 21]:
                self.hacer_pregunta("sustantivos")

    def hacer_pregunta(self, tipo_pregunta):
        """Hace una pregunta y verifica la respuesta."""
        if tipo_pregunta == "verbos":
            pregunta, respuesta = random.choice(self.preguntas["verbos"])
            respuesta_usuario = input(f"Pregunta: {pregunta} ")
        elif tipo_pregunta == "sustantivos":
            pregunta, respuesta = random.choice(self.preguntas["sustantivos"])
            respuesta_usuario = input(f"Pregunta: {pregunta} ")

        if respuesta_usuario.lower() == respuesta.lower():
            print("¡Respuesta correcta! Ganaste 5 puntos.")
            self.puntaje += 5
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es: \033[91m\033[1m{respuesta}\033[0m. ---> Pierdes un intento ☹.")
            self.intentos_restantes -= 1  # Reducir intentos restantes

    def verificar_puntaje(self):
        """Verifica si el jugador ha completado una columna y actualiza el puntaje."""
        columna = (self.posicion_jugador - 1) % 8
        if columna == 0:
            self.puntaje += 15
            print(f"¡Has completado una columna y has ganado 15 puntos! Tu puntaje total es: {self.puntaje}")
    
    def jugar(self):
        """Función principal para ejecutar el juego."""
        print("\n\033[34m\033[1mBienvenido a 🐍 Serpientes y Escaleras 🪜\033[0m")

        self.elegir_dificultad()
        while True:
            input("Presiona Enter para lanzar el dado...")
            self.posicion_jugador = 1
            while self.intentos_restantes > 0:
                print("\n" * 20)  # Limpiar la consola
                self.mostrar_tablero()
                print(f"\nTu posición actual: \033[1m\033[4m{self.posicion_jugador}\033[0m")
                pasos = self.lanzar_dado()
                self.mover_jugador(pasos)
                self.verificar_puntaje()
                input("Presiona Enter para continuar...")
                if self.posicion_jugador >= 64:
                    print("¡Felicidades! Has llegado a la casilla 64 y has ganado.")
                    break
            if self.intentos_restantes <= 0 and self.posicion_jugador < 64:  # Reemplazar max_intentos con intentos_restantes
                print("¡Has agotado tus oportunidades! Mejor suerte la próxima vez.")
                
            if self.nombre_jugador in self.jugadores:
                self.jugadores[self.nombre_jugador]["Turnos Jugados"] += 1
                self.jugadores[self.nombre_jugador]["Puntaje"].append(self.puntaje)
            else:
                self.jugadores[self.nombre_jugador] = {"Turnos Jugados": 1, "Puntaje": [self.puntaje]}
                
            intentar_otra_vez = input("¿Quieres jugar otra ronda? (si/no): ")
            if intentar_otra_vez.lower() != "si":
                self.mostrar_historial_jugadores()  # Mostrar historial si no se desea continuar
                break            
                print("¡Gracias por jugar!")

    def mostrar_historial_jugadores(self):
        """Muestra el historial de jugadores con el puntaje actual ordenado por puntaje descendente, encerrado en una tabla."""
        print("\nHistorial de Jugadores:")
        jugadores_ordenados = sorted(self.jugadores.items(), key=lambda x: x[1]["Puntaje"][-1] if x[1]["Puntaje"] else 0, reverse=True)
    
        print("-" * 45)# Imprimir encabezado de la tabla
        print("| Nombre   | Turnos Jugados | Puntaje actual |")
        print("-" * 45)
    
        for i, (jugador, datos) in enumerate(jugadores_ordenados[:5]):  # Limitar a los primeros 5 jugadores
            total_turnos = datos["Turnos Jugados"]
            puntaje_actual = datos["Puntaje"][-1] if datos["Puntaje"] else 0  # Obtener el puntaje actual del jugador
            print(f"| {jugador.ljust(9)}| {str(total_turnos).center(15)}| {str(puntaje_actual).center(15)}|") # Imprimir cada fila de la tabla 
        print("-" * 45)# Imprimir línea inferior de la tabla
        
    def cargar_historial_jugadores(self):
        """Carga los datos del historial de jugadores desde un archivo."""
        try:
            with open("historial_jugadores.txt", "r") as archivo:
                for linea in archivo:
                    nombre_jugador, turnos_jugados, puntaje_actual = linea.strip().split(",")
                    self.jugadores[nombre_jugador] = {"Turnos Jugados": int(turnos_jugados), "Puntaje": [int(puntaje_actual)]}
        except FileNotFoundError:
            print("No se encontró el archivo del historial de jugadores. Se creará uno nuevo al finalizar el juego.")

    def guardar_historial_jugadores(self):
        """Guarda los datos del historial de jugadores en un archivo."""
        with open("historial_jugadores.txt", "w") as archivo:
            jugadores_ordenados = sorted(self.jugadores.items(), key=lambda x: x[1]["Puntaje"][-1] if x[1]["Puntaje"] else 0, reverse=True)
            for jugador, datos in jugadores_ordenados[:5]:  # Limitar a los primeros 5 jugadores
                total_turnos = datos["Turnos Jugados"]
                puntaje_actual = datos["Puntaje"][-1] if datos["Puntaje"] else 0  # Obtener el puntaje actual del jugador
                archivo.write(f"{jugador},{total_turnos},{puntaje_actual}\n")

if __name__ == "__main__":
    juego = SerpientesYEscaleras()
    juego.mostrar_historial_jugadores()  # Mostrar historial de jugadores al inicio del juego
    while True:
        juego.jugar()
        juego.guardar_historial_jugadores()  # Guardar historial de jugadores al finalizar el juego
        juego.puntaje = 0  # Reiniciar el puntaje al iniciar un nuevo juego