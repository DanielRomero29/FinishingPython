def bisiesto(año):
    año = int(año)
    if (año % 4 == 0) and (año % 100 != 0):
        resultado = f"El año {año} es bisiesto"
    elif año % 400 == 0:
        resultado = f"El año {año} es bisiesto"
    else:
        resultado = f"El año {año} no es bisiesto"
    return resultado
        
if __name__ == "__main__":
    try:
        año = input("Introduza el año que desea saber si es bisiesto: ")
        resultado = bisiesto(año)
        print(resultado)
    except Exception as e:
        print(e)