# Inicializar el tablero
tablero = [[' ' for _ in range(3)] for _ in range(3)]

# Función para mostrar el tablero
def mostrar_tablero():
    for fila in tablero:
        print(fila)

# Función para comprobar si hay un ganador
def comprobar_ganador(ficha):
    # Comprobar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == ficha for j in range(3)) or all(tablero[j][i] == ficha for j in range(3)):
            return True

    # Comprobar diagonales
    if (tablero[0][0] == tablero[1][1] == tablero[2][2] == ficha) or (tablero[0][2] == tablero[1][1] == tablero[2][0] == ficha):
        return True

    return False

# Función para jugar
def jugar():
    jugador = 'X'
    jugadas = 0

    while True:
        print("Turno del jugador", jugador)
        mostrar_tablero()

        while True:
            try:
                x = int(input("Introduce la coordenada X del 1 al 3: "))
                y = int(input("Introduce la coordenada Y del 1 al 3: "))

                if x < 1 or x > 3 or y < 1 or y > 3:
                    print("Coordenadas fuera de rango.")
                elif tablero[y - 1][x - 1] != ' ':
                    print("Esa coordenada ya está siendo utilizada.")
                else:
                    break
            except ValueError:
                print("Entrada no válida. Debes ingresar números enteros.")

        tablero[y - 1][x - 1] = jugador
        jugadas += 1

        if comprobar_ganador(jugador):
            mostrar_tablero()
            print(f"La partida la ha ganado el jugador con la ficha {jugador}.")
            break
        elif jugadas == 9:
            mostrar_tablero()
            print("¡Empate!")
            break

        jugador = 'X' if jugador == 'O' else 'O'

# Iniciar el juego
print("Juego de Tres en raya")
jugar()
