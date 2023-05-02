def dni(dni):
    if len(dni) == 8:
        try:
            dni = int(dni)
            
        except Exception as e:
            print(f"Se ha producido el error: \n{e} \nPorque el DNI introducido es inválido")
            
        else:
            tablaLetrasDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
            resultadoResto = dni % 23 
            letra = tablaLetrasDNI[resultadoResto]  
            return f"La letra asociada al número de DNI {dni} es {letra}"
    else:
        return "El DNI introducido es inválido"

if __name__ == "__main__":
    DNI = input("Introduzca los números del DNI: ")
    letra = dni(DNI)
    print(letra)
            