# Definimos una función para calcular el área de un círculo
def calcular_area_circulo(radio):
    pi = 3.14159  # Valor aproximado de pi
    area = pi * radio**2
    return area

# Solicitamos al usuario que ingrese el radio del círculo
radio_usuario = float(input("Ingresa el radio del círculo: "))

# Llamamos a la función calcular_area_circulo con el radio ingresado y mostramos el resultado
area_circulo = calcular_area_circulo(radio_usuario)
print(f"El área del círculo con radio {radio_usuario} es: {area_circulo}")
