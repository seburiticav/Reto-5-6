# ...existing code...
def suma_consecutiva():
    lista_numero = []
    try:
        cantidad_numeros = int(
            input(
                "Por favor, ingrese la cantidad de números que desea sumar "
                "consecutivamente: "
            )
        )
    except (ValueError, TypeError) as error:
        print(f"Error leyendo la cantidad: {error}")
        return

    for i in range(cantidad_numeros):
        try:
            numero = int(
                input("Ingrese el valor " + str(i + 1) + ": ")
            )
        except (ValueError, TypeError) as error:
            print(f"Error leyendo el número {i+1}: {error}")
            return
        lista_numero.append(numero)

        lista_numero.sort()
        suma_valores_max = sum(lista_numero[-2:])
        print(f"La suma más alta posible es: {suma_valores_max}")

try:
    suma_consecutiva()
except (NameError, AttributeError) as error:
    print(f"Error de definición/atributo: {error}")
    exit(1)
