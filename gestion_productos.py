# Lista principal para almacenar productos
productos = []

# Función para validar entrada de texto no vacía
def ingresar_texto(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        else:
            print("❌ No puede estar vacío. Intente de nuevo.")

# Función para validar entrada de precio (entero positivo)
def ingresar_precio(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        else:
            print("❌ Ingrese un número válido (sin centavos y mayor que 0).")

# Función para mostrar productos
def mostrar_productos():
    if not productos:
        print("📭 No hay productos registrados.")
    else:
        print("\n📦 Lista de Productos Registrados:")
        for i, producto in enumerate(productos, 1):
            print(f"{i}. Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")

# Función para buscar productos por nombre
def buscar_producto():
    termino = ingresar_texto("🔍 Ingrese el nombre del producto a buscar: ").lower()
    encontrados = [p for p in productos if termino in p[0].lower()]
    if encontrados:
        print("\n✅ Productos encontrados:")
        for producto in encontrados:
            print(f"- Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")
    else:
        print("⚠️ No se encontraron productos con ese nombre.")

# Función para eliminar productos por número
def eliminar_producto():
    mostrar_productos()
    if productos:
        while True:
            num = input("🗑 Ingrese el número del producto a eliminar: ")
            if num.isdigit():
                num = int(num)
                if 1 <= num <= len(productos):
                    eliminado = productos.pop(num - 1)
                    print(f"✅ Producto '{eliminado[0]}' eliminado.")
                    break
                else:
                    print("❌ Número fuera de rango.")
            else:
                print("❌ Ingrese un número válido.")

# Función principal del menú
def menu():
    while True:
        print("\n📋 Sistema de Gestión Básica De Productos")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            nombre = ingresar_texto("📝 Ingrese el nombre del producto: ")
            categoria = ingresar_texto("📂 Ingrese la categoría: ")
            precio = ingresar_precio("💲 Ingrese el precio (sin centavos): ")
            productos.append([nombre, categoria, precio])
            print("✅ Producto agregado correctamente.")
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("👋 ¡Gracias por usar el sistema!")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

# Ejecutar menú
menu()
