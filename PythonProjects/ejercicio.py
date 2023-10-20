
#10. Para tributar un determinado impuesto se debe ser mayor de 16 años------------------------------------------
# y tener unos ingresos superiores a 1000 € mensuales. Escribir un programa
# que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla
# si el usuario tiene que tributar o no.
# Solicitar la edad del usuario

edad = int(input("Por favor, ingrese su edad: "))

# Solicitar los ingresos mensuales del usuario
ingresos_mensuales = float(input("Por favor, ingrese sus ingresos mensuales en €: "))

# Verificar si el usuario cumple con los requisitos para tributar
if edad > 16 and ingresos_mensuales > 1000:
    print("Tienes que tributar.")
else:
    print("No tienes que tributar.")

#11-------------------------------------------------------------------------------------------------------------------------------
# Solicitar la renta anual al usuario
renta_anual = float(input("Por favor, ingrese su renta anual en €: "))

# Determinar el tipo impositivo correspondiente
if renta_anual < 10000:
    tipo_impositivo = 5
elif renta_anual >= 10000 and renta_anual < 20000:
    tipo_impositivo = 15
elif renta_anual >= 20000 and renta_anual < 35000:
    tipo_impositivo = 20
elif renta_anual >= 35000 and renta_anual < 60000:
    tipo_impositivo = 30
else:
    tipo_impositivo = 45

# Mostrar el tipo impositivo correspondiente
print("Su tipo impositivo es del", tipo_impositivo, "%.")


















