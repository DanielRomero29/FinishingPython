def parImpar(numero):
    try:

        num = int(numero)
        if num % 2 == 0:
            return f"{num} es numero par"
        else:
            return f"{num} es numero impar"
        
    except:
        return "Error, introduce un dato correcto"