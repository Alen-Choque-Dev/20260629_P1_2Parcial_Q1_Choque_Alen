def validar_entero(numero: str) -> bool:
    if numero.isdigit() == True:
        validacion = True
    else:
        validacion = False
        print("Solo se admiten numeros enteros")
        
    return validacion


def validar_rango(numero: int, minimo: int, maximo: int) -> bool:
    if minimo <= numero <= maximo:
        validacion = True
    else:
        validacion = False
        print("Numero fuera de rango")
        
    return validacion

def validar_cadena_vacia(cadena: str) -> bool:
    if len(cadena) <= 0:
        print("Debe ingresar al menos un caracter")
        validacion = False
    else:
        validacion = True
        
    return validacion