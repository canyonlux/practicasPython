try:
    # Obtener la entrada del teclado (como cadena)
    rawInput = input('Ingresa un número: ')

    # Intentar convertir la cadena a un entero
    x = int(rawInput)

    # Calcular el cuadrado del número
    result = x * x

    # Imprimir el resultado
    print(f'El cuadrado de {x} es {result}')

except ValueError:
    # Manejar la excepción si se ingresa una entrada no numérica
    print('Error: Debes ingresar un número válido.')

#------------------------------------------------------------------------------------------------------------------------

# Definimos una lista llamada "alumnos" con algunos nombres de estudiantes
alumnos = ["Estudiante1", "Estudiante2", "Estudiante3", "Estudiante4", "Estudiante5" , "Estudiante6", "Estudiante7", "Estudiante8", "Estudiante9", "Estudiante10"]

# Utilizamos un bucle "for" para recorrer la lista de alumnos
for alumno in alumnos:
    # Imprimimos cada nombre de estudiante
    print(alumno)

#------------------------------------------------------------------------------------------------------------------------
#ZeroDivisionError: Esta excepción se produce cuando intentas dividir un número por cero
#TypeError: Esta excepción se produce cuando intentas realizar una operación entre tipos de datos incompatibles
try:
    # Intenta dividir 34 por 0, lo que generará un ZeroDivisionError
    r = 34/0

except ZeroDivisionError as e:
    # Maneja la excepción ZeroDivisionError
    print(f'Error: {e}. No puedes dividir por cero.')

try:
    # Intenta sumar un número entero (5) con una cadena de texto ('Enter number:'), lo que generará un TypeError
    patata = 5 + 'Enter number:'

except TypeError as e:
    # Maneja la excepción TypeError
    print(f'Error: {e}. No puedes sumar un número con una cadena de texto.')

#------------------------------------------------------------------------------------------------------------------------
fichero = None  # Inicializamos la variable 'fichero' fuera del bloque try

try:
    fichero = open('calabaza', 'r')
    contenido = fichero.read()  # Lee el contenido del archivo

    # Realiza la operación de suma después de haber leído el archivo
    patata = mi_lista[15] + 'Enter number:'
    print(contenido)

except ZeroDivisionError as e:
    print(f'Error: {e}. No puedes dividir por cero.')

except TypeError as e:
    print(f'Error: {e}. No puedes sumar un número con una cadena de texto.')

except FileNotFoundError as e:
    print(f'Error: {e}. El archivo "calabaza" no se encuentra.')

except IndexError as e:
    print(f'Error: {e}. La lista no tiene suficientes elementos.')

finally:
    # Asegúrate de cerrar el archivo en el bloque 'finally' para que se cierre incluso si ocurre una excepción
    if fichero is not None:
        fichero.close()


#------------------------------------------------------------------------------------------------------------------------
