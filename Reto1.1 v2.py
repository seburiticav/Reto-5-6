def suma(val1, val2):
    try:
        return val1 + val2
    except TypeError as error:
        print(f"Error en la suma: {error}")
        return None


def resta(val1, val2):
    try:
        return val1 - val2
    except TypeError as error:
        print(f"Error en la resta: {error}")
        return None


def multiplicacion(val1, val2):
    try:
        return val1 * val2
    except TypeError as error:
        print(f"Error en la multiplicación: {error}")
        return None


def division(val1, val2):
    try:
        return val1 / val2
    except ZeroDivisionError as error:
        print(f"Error: No se puede dividir entre cero - {error}")
        return None
    except TypeError as error:
        print(f"Error en la división: {error}")
        return None


try:
    val1 = float(input("Por favor, ingrese el primer valor para la operación que desea realizar: "))
    val2 = float(input("Por favor, ingrese el segundo valor para la operación que desea realizar: "))
except ValueError as error:
    print(f"Error: Debe ingresar valores numéricos válidos - {error}")
    exit()

try:
    operacion = input("Excelente, ahora ingrese la operación que desea hacer (+, -, *, /): ")
    if operacion not in ["+", "-", "*", "/"]:
        raise ValueError("Operación no válida")
except ValueError as error:
    print(f"Error: {error}")
    exit()

resultado = None
if operacion == "+":
    resultado = suma(val1, val2)
elif operacion == "-":
    resultado = resta(val1, val2)
elif operacion == "*":
    resultado = multiplicacion(val1, val2)
elif operacion == "/":
    resultado = division(val1, val2)

if resultado is not None:
    try:
        print(f"El resultado es: {resultado}")
    except Exception as error:
        print(f"Error al mostrar el resultado: {error}")