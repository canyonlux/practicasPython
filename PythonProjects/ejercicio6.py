

print((lambda x: x**2)(float(input("Ingrese un número: "))))
#------------------------------------------------------------

def procesar_parametros(*args):
    resultado = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            resultado += arg ** 2
        else:
            resultado = "No es un número" if resultado == 0 else resultado
            resultado += str(arg)
    return resultado

print(procesar_parametros(5))                      # Devuelve 25
print(procesar_parametros("Hola", 3, "Mundo"))     # Devuelve "No es un númeroHolaNo es un númeroMundo9"
print(procesar_parametros(2, 3, 4, 5))            # Devuelve 54



