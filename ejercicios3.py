

#EJERCICIO1
N1= float(input ("Ingresa la nota del parcial 1: "))
N2= float(input ("Ingresa la nota del parcial 2: "))
N3= float(input ("Ingresa la nota del parcial 3: "))
print(N1, N2, N3)
P = (N1+N2+N3) / 3
print("El promedio del estudiante es: "+ str(P))
#------------------------------------------------------------------------
#EJERCICIO2
base= float(input("Ingresa la base del rectangulo: "))
altura= float(input("Ingresa la altura del rectangulo: "))
perimetro= (base+altura)*2
superficie= (base*altura)
print("El perimetro es: "+ str (perimetro) +" y la superficie es: "+ str (superficie))
#--------------------------------------------------------------------------
#EJERCICIO3
numero1= int(input("Ingresa el primer numero: "))
numero2= int(input("Ingresa un numero entero valido: "))
if numero1<numero2:
    print("El numero menor es: " + str(numero1))
else: print("El numero menor es: " + str(numero2))
#-----------------------------------------------------------------------------
#EJERCICIO4
año= int(input("Introduce un año valido: "))
if (año % 4 == 0) and (año % 100 != 0) or (año % 400==0):
    print("El año es bisiesto")
else: print("El año no es bisiesto")
#--------------------------------------------------------------------------
#EJERCICIO5
from itertools import permutations
# Valores de las variables
a = 2
b = 90
c = 45
# Crear una lista con las variables
variables = [a, b, c]
# Obtener todas las permutaciones de las variables
permutaciones = list(permutations(variables))
# Imprimir todas las permutaciones
for perm in permutaciones:
    print(perm)
#EJERCICIO5 (ALTERNATIVA)
# Valores de las variables
a = 2
b = 90
c = 45
# Combinación 1: a, b, c
if a < b and a < c:
    if b < c:
    print(a, b, c)
else:
print(a, c, b)
# Combinación 2: a, c, b
if a < b and a < c:
    if c < b:
    print(a, c, b)
else:
print(a, b, c)
# Combinación 3: b, a, c
if b < a and b < c:
    if a < c:
    print(b, a, c)
else:
print(b, c, a)
# Combinación 4: b, c, a
if b < a and b < c:
    if c < a:
    print(b, c, a)
else:
print(b, a, c)
# Combinación 5: c, a, b
if c < a and c < b:
    if a < b:
    print(c, a, b)
else:
print(c, b, a)
# Combinación 6: c, b, a
if c < a and c < b:
    if b < a:
    print(c, b, a)
else:
print(c, a, b)
#----------------------------------------------------------
#EJERCICIO6
# Pedir al usuario que ingrese el capital inicial, el interés y el tiempo en años
c = float(input("Introduce un capital inicial: "))
i = float(input("Introduce el tipo de interés (entre 0 y 100): "))
m = int(input("Introduce el tiempo en años: "))
# Comprobar las condiciones
if c < 0 or i <= 0 or i > 100 or m <= 0:
    print("Las entradas no son válidas. Asegúrate de que el capital sea positivo, el interés esté
en el rango [0, 100], y el tiempo sea mayor que 0.")
else:
# Calcular el monto final acumulativo
monto_final = c * (1 + (i / 100))**m
print(f"El monto final después de {m} años es: {monto_final:.2f}")
#------------------------------------------------------------------------------------------------------------
#EJERCICIO7
# Pedir al usuario que ingrese el valor de x
x = float(input("Introduce el valor de x: "))
# Inicializar las variables
e_to_x = 1.0 # Valor inicial de e^x
n = 1 # Inicializar el contador
term = x # Inicializar el primer término de la serie
# Calcular e^x
while abs(term) >= 0.00001:
    e_to_x += term
n += 1
term *= x / n
# Imprimir el resultado
print(f"e^{x} aproximado es: {e_to_x:.5f}")
#------------------------------------------------------------------------------------------
#EJERCICIO8
# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
    return False # 0 y 1 no son primos
if numero <= 3:
    return True # 2 y 3 son primos
if numero % 2 == 0 or numero % 3 == 0:
    return False # Si es divisible por 2 o 3, no es primo
i = 5
while i * i <= numero:
    if numero % i == 0 or numero % (i + 2) == 0:
    return False # Si es divisible por algún número entre i y i+2, no es primo
i += 6
return True # Si no se encontraron divisores, es primo
# Función principal
def main():
    contador = 0
numero = 2
while contador < 10: # Queremos encontrar los primeros 10 números primos
    if es_primo(numero):
    cubo = numero ** 3 # Calculamos el cubo del número primo
print(f"{numero} - {cubo}") # Imprimimos el número primo y su cubo
contador += 1 # Incrementamos el contador de números primos encontrados
numero += 1 # Pasamos al siguiente número
if __name__ == "__main__":
    main() # Llamamos a la función principal si el script es ejecutado directamente
#---------------------------------------------------------------------------------------------
#EJERCICIO9
# Solicitar la cantidad de empleados
ce = int(input("Ingrese la cantidad de empleados: "))
i = 1
smayor = 0
# Inicializar la variable c para almacenar el número de orden del empleado con el sueldo
más alto
c = 0
print("Ingrese los sueldos:")
while i <= ce:
    sueldo = float(input("Ingrese el sueldo del empleado {}: ".format(i)))
# Verificar si el sueldo actual es mayor que el sueldo más alto encontrado hasta ahora
if sueldo > smayor:
    smayor = sueldo
c = i # Actualizar el número de orden del empleado con el sueldo más alto
i += 1
# Imprimir el número de orden del empleado con el sueldo más alto y su sueldo
print("El empleado número {} tiene el mayor sueldo que es: {}".format(c, smayor))
#---------------------------------------------------------------------------------------------
#EJERCICIO10
# Solicitar la cantidad de temperaturas
N = int(input("Ingrese la cantidad de temperaturas: "))
# Inicializar una lista para almacenar las temperaturas
temperaturas = []
# Leer las temperaturas y almacenarlas en la lista
for i in range(N):
    temperatura = float(input("Ingrese la temperatura {} en grados Celsius: ".format(i + 1)))
temperaturas.append(temperatura)
# Calcular la media de las temperaturas
suma_temperaturas = sum(temperaturas)
media = suma_temperaturas / N
# Contar cuántas temperaturas son superiores o iguales a la media
contador_superiores_o_iguales = 0
for temperatura in temperaturas:
    if temperatura >= media:
    contador_superiores_o_iguales += 1
# Imprimir la media y el número de temperaturas superiores o iguales a la media
print("La media de las temperaturas es: {:.2f}".format(media))
print("Hay {} temperaturas superiores o iguales a la
media.".format(contador_superiores_o_iguales"))