def primo(numero):
    posiblePrimo = int(numero)
    primo = True
    numero = posiblePrimo - 1
    while numero >= 2:
        if posiblePrimo % numero == 0:
            primo = False
            break
        else:
            numero -= 1
    if primo == True:
        resultado = f"El número {posiblePrimo} es primo"
    else:
        resultado = f"El número {posiblePrimo} no es primo, pues {numero} es un divisor del mismo"
    return resultado
if __name__ == "__main__":
    try:
        numero = input("Introduza el numero que desea saber si es primo: ")
        resultado = primo(numero)
        print(resultado)
    except Exception as e:
        print(e)