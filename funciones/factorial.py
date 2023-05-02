def fac(numero):
    try:
        factorial = 1
        num = int(numero)
        for i in range(num):
            factorial = factorial * (i+1)
        
        return f"El factorial de {num} es {factorial}"
        
    except:
        return "Error, introduce un dato correcto"