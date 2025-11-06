# ...existing code...
def anagramas():
    lista_palabras = []
    letras_por_palabra = []
    try:
        cantidad_palabras = int(
            input(
                "Por favor, ingrese la cantidad de palabras que desea añadir a la lista: "
            )
        )
    except (ValueError, TypeError) as error:
        print(f"Error leyendo la cantidad de palabras: {error}")
        return

    for i in range(cantidad_palabras):
        try:
            palabra = str(
                input("Ingrese la palabra " + str(i + 1) + ": ")
            )

        except (TypeError) as error:
            print(f"Error leyendo la palabra {i+1}: {error}")
            return

        if palabra == "":
            print(f"Entrada vacía en la palabra {i+1}.")
            return

        lista_palabras.append(palabra)
        letras_por_palabra.append(sorted(list(palabra)))

    for i in range(len(letras_por_palabra)):
        for j in range(i + 1, len(letras_por_palabra)):
            if letras_por_palabra[i] == letras_por_palabra[j]:
                print(
                    f"Las palabras anagramas son {lista_palabras[i]} y {lista_palabras[j]}"
                )

try:
    anagramas()
except (NameError, AttributeError) as error:
    print(f"Error de definición/atributo: {error}")
    exit(1)
