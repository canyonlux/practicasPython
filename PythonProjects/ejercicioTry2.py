# Función para multiplicar dos matrices
def multiplicar_matrices(a, b):
    # Verificamos si el número de columnas de la matriz 'a' es igual al número de filas de la matriz 'b'
    if len(a[0]) != len(b):
        print("No se pueden multiplicar las matrices")
        return None

    # Inicializamos una matriz resultante con ceros
    resultado = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    # Realizamos la multiplicación de matrices
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                resultado[i][j] += a[i][k] * b[k][j]

    return resultado

# Solicitamos al usuario las matrices 'a' y 'b'
a = []
b = []

# Solicitamos la matriz 'a' al usuario
filas_a = int(input("Ingrese el número de filas de la matriz 'a': "))
columnas_a = int(input("Ingrese el número de columnas de la matriz 'a': "))

print("Ingrese los elementos de la matriz 'a':")
for i in range(filas_a):
    fila = []
    for j in range(columnas_a):
        valor = float(input(f'Elemento a[{i}][{j}]: '))
        fila.append(valor)
    a.append(fila)

# Solicitamos la matriz 'b' al usuario
filas_b = int(input("Ingrese el número de filas de la matriz 'b': "))
columnas_b = int(input("Ingrese el número de columnas de la matriz 'b': "))

print("Ingrese los elementos de la matriz 'b':")
for i in range(filas_b):
    fila = []
    for j in range(columnas_b):
        valor = float(input(f'Elemento b[{i}][{j}]: '))
        fila.append(valor)
    b.append(fila)

# Multiplicamos las matrices y mostramos el resultado
resultado = multiplicar_matrices(a, b)
if resultado:
    print("El resultado de la multiplicación de matrices es:")
    for fila in resultado:
        print(fila)


