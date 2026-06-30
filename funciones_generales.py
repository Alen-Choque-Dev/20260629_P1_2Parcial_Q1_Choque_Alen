from validaciones import validar_cadena_vacia, validar_entero
from funciones_auxiliares import calcular_stock_acumulado, calcular_max_min

def imprimir_producto(lista_claves: list, producto: dict):
    print("-----------------------------")
    for clave in lista_claves:
        print(f"{clave}: {producto[clave]}")
        

def listar_productos(lista_productos: list[dict]):
    lista_claves = list(lista_productos[0].keys())
    print("LISTA DE PRODCUTOS:")
    for producto in lista_productos:
        imprimir_producto(lista_claves, producto)
        
            
def agregar_producto(lista_productos: list[dict]):
    lista_claves = list(lista_productos[0].keys())
    producto_nuevo = {}
    
    for clave in lista_claves:
        while True:
            valor_actual = input(f"{clave} del producto: ")
            
            match clave:
                case "id" | "precio" | "stock":
                    entero_valido = validar_entero(valor_actual)
                    if entero_valido == True:
                        valor_actual = int(valor_actual)
                        break
                case _:       
                    cadena_existe = validar_cadena_vacia(valor_actual)
                    if cadena_existe == True:
                        break
            
        producto_nuevo[clave] = valor_actual
    lista_productos.append(producto_nuevo)


def buscar_producto_por_nombre(lista_productos: list[dict]) -> dict:
    prodcuto_buscado = dict()
    prodcuto_encontrado = False
    
    while prodcuto_encontrado == False:
        nombre_a_buscar = input(
            "Indique el nombre del producto que desea buscar: "
            )
    
        for producto in lista_productos:
            if producto["nombre"] == nombre_a_buscar:
                prodcuto_buscado = producto
                print("Producto encontrado")
                prodcuto_encontrado = True
                break
            
        if prodcuto_encontrado == False:
            print("Prodcuto no encontrado\n")
            
    return prodcuto_buscado


def modificar_stock(lista_productos: list[dict]):
    for producto in lista_productos:
        while True:
            print(f"\nProducto: {producto["nombre"]}")
            nuevo_stock = input("Ingrese el nuevo stock: ")
            entero_valido = validar_entero(nuevo_stock)
            if entero_valido == True:
                nuevo_stock = int(nuevo_stock)
                producto["stock"] = nuevo_stock
                break
            
    return lista_productos
        
        
def eliminiar_producto(lista_productos: list[dict]) -> list[dict]:
    producto_a_eliminar = input("Que producto desea elimiar?: ")
    producto_existe = False
    
    for i in range(len(lista_productos)):
        if lista_productos[i]["nombre"] == producto_a_eliminar:
            lista_productos.pop(i)
            print("Producto eliminado")
            producto_existe = True
            break
        
    if producto_existe == False:
        print(f"El producto: {producto_a_eliminar}, no existe en el inventario")

    return lista_productos

    
def calcular_cantidad_productos_categoria(lista_productos: list[dict]):
    categorias = []
    for producto in lista_productos:
        if producto["categoria"] not in categorias:
            categorias.append(producto["categoria"])
            
    cantidad_por_categoria = [0] * len(categorias)
    
    for i in range(len(lista_productos)):
        for j in range(len(categorias)):
            if lista_productos[i]["categoria"] == categorias[j]:
                cantidad_por_categoria[j] += 1
                break
            
    cantidad_productos_categoria = [categorias, cantidad_por_categoria]
    
    return cantidad_productos_categoria


def mostrar_estadisticas(lista_productos: list[dict]):
    cantidad_productos = len(lista_productos)
    stock_total = calcular_stock_acumulado(lista_productos)
    precio_mas_caro = calcular_max_min(lista_productos, "precio")
    precio_mas_barato = calcular_max_min(lista_productos, "precio", "min")
    
    print(f"Cantidad de productos: {cantidad_productos}")
    print(f"Stock total de productos: {stock_total}")
    print(f"Precio del producto mas caro: {precio_mas_caro}")
    print(f"Precio del producto mas barato: {precio_mas_barato}")


def exportar_json_a_csv(lista_productos: list[dict]):
    claves = list(lista_productos[0].keys())
    encabezado_csv = ",".join(claves)
    
    with open("productos.csv", "w", encoding="utf-8") as archivo_csv:
        archivo_csv.write(encabezado_csv)
        for producto in lista_productos:
            valores = []
            for clave in claves:
                valor = producto[clave]
                valor = str(valor) 
                valores.append(valor)
            fila_csv = ",".join(valores)
            archivo_csv.write("\n" + fila_csv)