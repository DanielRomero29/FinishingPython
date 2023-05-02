def celsius(celsius):
    try:
        #celsius = float(input("Introduzca los grados celsius: "))
        celsius = int(celsius)
        fahrenheit = (celsius*1.8) + 32
        
        return f"{celsius}º Celsius ==> {fahrenheit}º Fahrenheit"
        
    except:
        return "Error, introduce un dato correcto"