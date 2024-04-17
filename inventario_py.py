import os
import pandas as pd

inventario = {}

def agregar_producto():
    codigo = input("Ingrese el código del producto: ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    inventario[codigo] = {'productos': producto, 'Cantidad': cantidad, 'Precio': precio, 'vendidos': 0}
    print(f"Producto '{producto}' agregado correctamente.")

def retirar_producto():
    codigo = input("Ingrese el código del producto a retirar: ")
    if codigo in inventario:
        cantidad_retirar = int(input("Ingrese la cantidad a retirar: "))
        cantidad_actual = inventario[codigo]['Cantidad']
        if cantidad_retirar <= cantidad_actual:
            inventario[codigo]['Cantidad'] -= cantidad_retirar
            inventario[codigo]['vendidos'] += cantidad_retirar  # Actualizar el número de productos vendidos
            print(f"{cantidad_retirar} unidades del producto '{inventario[codigo]['productos']}' retiradas correctamente.")
        else:
            print("No hay suficiente cantidad en el inventario.")
    else:
        print("El código especificado no existe en el inventario.")

def modificar_inventario():
    codigo = input("Ingrese el código del producto a modificar: ")
    if codigo in inventario:
        nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        inventario[codigo]['Cantidad'] = nueva_cantidad
        print(f"Cantidad del producto '{inventario[codigo]['productos']}' modificada correctamente.")
    else:
        print("El código especificado no existe en el inventario.")

def mostrar_inventario():
    print("\nInventario:")
    for codigo, datos in inventario.items():
        print(f"Código: {codigo}, Producto: {datos['productos']}, Cantidad: {datos['Cantidad']}, Precio: {datos['Precio']}, Vendidos: {datos['vendidos']}")

def guardar_inventario_excel():
    df = pd.DataFrame.from_dict(inventario, orient='index')
    nombre_archivo = input("Ingrese el nombre del archivo para guardar el inventario (sin extensión): ") + '.xlsx'
    df.to_excel(nombre_archivo, index_label='Código')
    print(f"Inventario guardado en '{nombre_archivo}' correctamente.")

def cargar_inventario_excel():
    nombre_archivo = input("Ingrese el nombre del archivo del inventario a cargar (sin extensión): ") + '.xlsx'
    if os.path.exists(nombre_archivo):
        df = pd.read_excel(nombre_archivo, index_col='Código')
        inventario.update(df.to_dict(orient='index'))
        print(f"Inventario cargado desde '{nombre_archivo}' correctamente.")
    else:
        print(f"No se encontró el archivo '{nombre_archivo}'. No se cargó ningún inventario.")

def buscar_producto():
    opcion = input("Seleccione una opción de búsqueda:\n1. Buscar por código\n2. Buscar por nombre\nOpción: ")
    if opcion == "1":
        codigo = input("Ingrese el código del producto: ")
        if codigo.isdigit():  # Verificar si el código es un número entero
            codigo = int(codigo)  # Convertir a entero si es un número
            if codigo in inventario:
                print(f"Producto encontrado - Código: {codigo}, Nombre: {inventario[codigo]['productos']}, Cantidad: {inventario[codigo]['Cantidad']}, Precio: {inventario[codigo]['Precio']}")

            else:
                print("Producto no encontrado en el inventario.")
        else:
            print("El código debe ser un número entero.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ")
        productos_encontrados = [codigo for codigo, datos in inventario.items() if datos['productos'].lower() == nombre.lower()]
        if productos_encontrados:
            for codigo in productos_encontrados:
                print(f"Producto encontrado - Código: {codigo}, Nombre: {inventario[codigo]['productos']}, Cantidad: {inventario[codigo]['Cantidad']}, Precio: {inventario[codigo]['Precio']}")
        else:
            print("Producto no encontrado en el inventario.")
    else:
        print("Opción no válida.")

def mas_vendidos():
    # ordenar con sort
    inventario_ordenado = list(inventario.values())
    inventario_ordenado.sort(key=lambda x: x['vendidos'], reverse=True) #reverse=True es el forma descendente

    # Mostramos los dos primeros productos más vendidos
    print("Los productos más vendidos son:")
    for producto in inventario_ordenado[:2]:
        print(f"Nombre: {producto['productos']}, Vendidos: {producto['vendidos']}")

def menu():
    print("\nMenú:")
    print("1. Agregar producto al inventario")
    print("2. Retirar producto del inventario")
    print("3. Modificar inventario")
    print("4. Mostrar inventario")
    print("5. Buscar producto en el inventario")
    print("6. Guardar inventario en Excel")
    print("7. Cargar inventario desde Excel")
    print("8. Más vendidos")
    print("9. Salir")

def alertar_stock_bajo(): 
    productos_stock_bajo = [f"{datos['productos']} solo quedan {datos['Cantidad']} en stock" for codigo, datos in inventario.items() if datos['Cantidad'] < 5]
    if productos_stock_bajo:
        print("\033[91m" + f"¡ALERTA! Los siguientes productos tienen un stock bajo:\n{', '.join(productos_stock_bajo)}" + "\033[0m")

cargar_inventario_excel()

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        retirar_producto()
    elif opcion == "3":
        modificar_inventario()
    elif opcion == "4":
        mostrar_inventario()
    elif opcion == "5":
        buscar_producto()
    elif opcion == "6":
        guardar_inventario_excel()
    elif opcion == "7":
        cargar_inventario_excel()
    elif opcion == "8":
        mas_vendidos()
    elif opcion == "9":
        print("Saliendo del programa...")
        print("\n:")

        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
