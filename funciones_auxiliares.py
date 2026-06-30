import json

def abrir_json_r(ruta_archivo: str) -> list[dict]:
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lista_de_diccionarios = json.load(archivo)
        
    return lista_de_diccionarios


def calcular_stock_acumulado(lista_productos: list[dict]) -> int:
    stock_acumuluado = 0
    for producto in lista_productos:
        stock_actual = producto["stock"]
        stock_acumuluado += stock_actual
        
    return stock_acumuluado


def calcular_max_min(lista_productos: list[dict], clave: str, criterio: str = "max") -> int:
    
    max_min = lista_productos[0][clave]
    for i in range(1, len(lista_productos), 1):
        if lista_productos[i][clave] > max_min and criterio == "max":
            max_min = lista_productos[i][clave]
        elif lista_productos[i][clave] < max_min and criterio == "min":
            max_min = lista_productos[i][clave]
            
    return max_min