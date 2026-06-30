from validaciones import validar_entero, validar_rango

def imprimir_menu():
    menu = """Sistema de Gestión de Supermercado:
========================================    
1. Listar productos
2. Agregar producto
3. Buscar producto por nombre
4. Modificar stock
5. Eliminar producto
6. Mostrar productos por categoría
7. Mostrar estadísticas
8. Exportar reporte CSV
9. Guardar y salir
=========================================
"""
    
    print(menu)
    

def ingresar_opcion(minimo: int, maximo: int) -> int:
    while True:
        opcion = input("Ingrese una opcion: ")
        entero_valido = validar_entero(opcion)
        
        if entero_valido == True:
            opcion = int(opcion)
            rango_valido = validar_rango(opcion, minimo, maximo)
            
            if rango_valido == True:
                break
            
    return opcion