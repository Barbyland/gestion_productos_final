import sqlite3
from colorama import init, Fore, Style

init(autoreset=True)

# ---------- CONEXIÓN Y CREACIÓN DE LA BASE DE DATOS ----------
def crear_bd():
    try:
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT
            )
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(Fore.RED + f"Error al crear la base de datos: {e}")

# ---------- FUNCIONES DEL SISTEMA ----------
def registrar_producto():
    try:
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print(Fore.RED + "⚠️ El nombre no puede estar vacío.")
            return
        descripcion = input("Descripción: ").strip()
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        categoria = input("Categoría: ").strip()

        # Confirmación antes de registrar
        print(Fore.CYAN + "\n🔍 Verificá los datos ingresados:")
        print(f"Nombre: {nombre}")
        print(f"Descripción: {descripcion}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio: ${precio}")
        print(f"Categoría: {categoria}")
        confirmar = input(Fore.YELLOW + "¿Confirmar registro? (s/n): ").strip().lower()
        if confirmar != "s":
            print(Fore.YELLOW + "❗ Registro cancelado. Volvé a intentarlo.")
            return

        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)''', (nombre, descripcion, cantidad, precio, categoria))
        conn.commit()
        conn.close()
        print(Fore.GREEN + "✅ Producto registrado con éxito.")
    except ValueError:
        print(Fore.RED + "⚠️ Error: ingresá números válidos en 'cantidad' y 'precio'.")
    except Exception as e:
        print(Fore.RED + f"❌ Error al registrar producto: {e}")

def ver_productos():
    try:
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()
        conn.close()

        if productos:
            print(Fore.CYAN + "\n📦 Lista de productos:")
            for p in productos:
                print(f"ID: {p[0]}, Nombre: {p[1]}, Cantidad: {p[3]}, Precio: ${p[4]:.2f}, Categoría: {p[5]}")
                print()  # esta línea deja un espacio visual después del listado
        else:
            print(Fore.YELLOW + "⚠️ No hay productos registrados.")
    except Exception as e:
        print(Fore.RED + f"❌ Error al mostrar productos: {e}")

def actualizar_producto():
    try:
        id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if producto:
            print("Deje el campo vacío si no quiere modificarlo.")
            nuevo_nombre = input("Nuevo nombre: ") or producto[1]
            nueva_desc = input("Nueva descripción: ") or producto[2]
            nueva_cant = input("Nueva cantidad: ")
            nueva_cant = int(nueva_cant) if nueva_cant else producto[3]
            nuevo_precio = input("Nuevo precio: ")
            nuevo_precio = float(nuevo_precio) if nuevo_precio else producto[4]
            nueva_categoria = input("Nueva categoría: ") or producto[5]

            cursor.execute('''
                UPDATE productos
                SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
                WHERE id = ?''', (nuevo_nombre, nueva_desc, nueva_cant, nuevo_precio, nueva_categoria, id_producto))
            conn.commit()
            print(Fore.GREEN + "✅ Producto actualizado.\n")
        else:
            print(Fore.YELLOW + "⚠️ Producto no encontrado.")
        conn.close()
    except ValueError:
        print(Fore.RED + "⚠️ Ingresá números válidos en cantidad o precio.")
    except Exception as e:
        print(Fore.RED + f"❌ Error al actualizar producto: {e}")

def eliminar_producto():
    try:
        id_producto = int(input("ID del producto a eliminar: "))
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conn.commit()
        conn.close()
        print(Fore.RED + "🗑️ Producto eliminado (si existía).\n")
    except ValueError:
        print(Fore.RED + "⚠️ Ingresá un número válido.")
    except Exception as e:
        print(Fore.RED + f"❌ Error al eliminar producto: {e}")

def buscar_producto():
    try:
        id_producto = int(input("ID del producto a buscar: "))
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()
        conn.close()
        if producto:
            print(Fore.CYAN + f"🔎 ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[3]}, Precio: ${producto[4]:.2f}, Categoría: {producto[5]}")
        else:
            print(Fore.YELLOW + "⚠️ Producto no encontrado.")
    except ValueError:
        print(Fore.RED + "⚠️ Ingresá un número válido.")
    except Exception as e:
        print(Fore.RED + f"❌ Error al buscar producto: {e}")

def reporte_stock_bajo():
    try:
        limite = int(input("Mostrar productos con cantidad menor o igual a: "))
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
        productos = cursor.fetchall()
        conn.close()
        if productos:
            print(Fore.MAGENTA + "\n📉 Productos con stock bajo:")
            for p in productos:
                print(f"ID: {p[0]}, Nombre: {p[1]}, Cantidad: {p[3]}")
                print()  # esta línea deja un espacio visual después del listado
        else:
            print(Fore.GREEN + "✅ No hay productos con ese nivel de stock.")
    except ValueError:
        print(Fore.RED + "⚠️ Ingresá un número válido.")
    except Exception as e:
        print(Fore.RED + f"❌ Error al generar reporte: {e}")

# ---------- MENÚ PRINCIPAL ----------
def menu():
    while True:
        print(Fore.BLUE + Style.BRIGHT + "\n" + "="*40)
        print("📦  SISTEMA DE GESTIÓN DE INVENTARIO")
        print("="*40)
        print(Fore.YELLOW + "1️⃣  Registrar producto")
        print("2️⃣  Ver productos")
        print("3️⃣  Actualizar producto")
        print("4️⃣  Eliminar producto")
        print("5️⃣  Buscar producto por ID")
        print("6️⃣  📉 Reporte de stock bajo")
        print("0️⃣  ❌ Salir")
        print("="*40)
        opcion = input(Fore.CYAN + "Seleccioná una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_stock_bajo()
        elif opcion == "0":
            print(Fore.BLUE + "👋 ¡Gracias por usar el sistema!")
            break
        else:
            print(Fore.RED + "❌ Opción no válida. Intente nuevamente.")


# ---------- EJECUCIÓN ----------
crear_bd()
menu()
