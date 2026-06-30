from menu import imprimir_menu, ingresar_opcion
from funciones_auxiliares import abrir_json_r
import funciones_generales as funct_app

lista_productos = abrir_json_r("productos.json")
lista_claves = list(lista_productos[0].keys())

while True:
    imprimir_menu()
    opcion_menu = ingresar_opcion(1, 9)
    
    match opcion_menu:
        case 1:
            funct_app.listar_productos(lista_productos)
        case 2:
            funct_app.agregar_producto(lista_productos)
        case 3:
            producto_buscado = funct_app.buscar_producto_por_nombre(
                lista_productos
            )
            funct_app.imprimir_producto(lista_claves, producto_buscado)
        case 4:
            lista_productos = funct_app.modificar_stock(lista_productos)
        case 5:
            lista_productos = funct_app.eliminiar_producto(lista_productos)
        case 6:
            productos_categoria = funct_app.calcular_cantidad_productos_categoria(
                lista_productos
            )
            print(productos_categoria)
        case 7:
            funct_app.mostrar_estadisticas(lista_productos)
        case 8:
            funct_app.exportar_json_a_csv(lista_productos)
        case 9:
            print("Gracias por utilizar el programa")
            break