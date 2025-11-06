def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primos():
    numeros = []
    lista_numeros = int(
        input(
            "Por favor, ingrese la cantidad de números que desea organizar: "
        )
    )
    for i in range(lista_numeros):
        numero = int(
            input("Ingrese el valor " + str(i + 1) + ": ")
        )
        numeros.append(numero)
    for numero in numeros:
        if es_primo(numero):
            print(f"El número {numero} es primo.")
        else:
            print(f"El número {numero} NO es primo.")
            
try:
    primos()
except (ValueError, TypeError) as error:
    print(f"Error de entrada/tipo: {error}")
    exit(1)
except (NameError, AttributeError) as error:
    print(f"Error de definición/atributo: {error}")
    exit(1)
