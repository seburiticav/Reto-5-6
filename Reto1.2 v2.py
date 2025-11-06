def palindromo(palabra):
    palabra_invertida = ''.join(reversed(palabra))
    if palabra == palabra_invertida:
        return "La palabra es un palíndromo."
    else:
        return "La palabra NO es un palíndromo."


def comprobacion(palabra):
    if not palabra.isalpha() or len(palabra) < 3:
        return "La palabra no es válida."
    else:
        return palindromo(palabra)


try:
    palabra = str(
        input(
            "Por favor, ingrese una palabra que tenga más de 2 caracteres, "
            "que no posea valores numéricos y que no posea símbolos: "
        )
    )
except (TypeError, ValueError, NameError, AttributeError) as error:
    print(f"Error leyendo la entrada: {error}")
    exit(1)

try:
    print(comprobacion(palabra))
except (TypeError, AttributeError, NameError) as error:
    print(f"Error al comprobar/mostrar la palabra: {error}")
    exit(1)
