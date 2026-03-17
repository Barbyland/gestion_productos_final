# Proyecto Final – Sistema de Gestión de Inventario

**Autor:** Barbara Bernhard  
**Fecha:** Julio 2025  
**Tecnología:** Python + SQLite  
**Curso:** Iniciación con Python dictado por **Talento Tech**

---

## 🗂 Descripción

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar un inventario de productos utilizando una base de datos SQLite. Fue creado como entrega final del curso, integrando estructuras de datos, validaciones, modularización y persistencia de datos.

---

## ⚙️ Funcionalidades principales

- 📥 Agregar productos con validación de nombre y precio
- 📋 Listar todos los productos con sus respectivos índices
- 🗑 Eliminar productos seleccionados por el usuario
- 💾 Guardado automático en una base de datos SQLite (`inventario.db`)

---

## 📄 Archivos del proyecto

| Archivo                  | Descripción                                        |
|--------------------------|----------------------------------------------------|
| `inventario.py`          | Script principal con el menú del programa          |
| `gestion_productos.py`   | Módulo con funciones para manipular productos      |
| `inventario.db`          | Base de datos SQLite que almacena los productos    |
| `requirements.txt`       | Dependencias del proyecto                          |
| `EntregaFinal.docx`      | Documento de entrega con descripción del proyecto  |
| `README.md`              | Documentación del proyecto                         |

---

## ▶️ Cómo ejecutar el programa

### Opción 1: ejecución directa
1. Asegurate de tener **Python 3.13 o superior** instalado.
2. Abrí una terminal en la carpeta del proyecto.
3. Ejecutá el archivo principal: 
```bash
python inventario.py


### Opción 2: usando entorno virtual
1. Crear el entorno virtual:
python -m venv .venv
2. Activarlo en PowerShell:
.venv\Scripts\Activate.ps1
3. Ejecutar el programa:
python inventario.py


##  Dependencias

Este proyecto utiliza principalmente módulos estándar de Python.
Actualmente, el archivo requirements.txt puede estar vacío porque no se instalaron librerías externas adicionales.

##  Comentarios finales 

Este proyecto fue una gran oportunidad para aplicar de manera práctica lo aprendido en el curso Iniciación con Python** dictado por **Talento Tech**.
Se trabajó con listas, estructuras de control, modularización del código y bases de datos con `sqlite3`.

📎 [Ver certificado](docs/certificado_python_inicial.pdf)
_________________________________________________________________________________________________________
English version

📦 Final Project – Inventory Management System
Author: Barbara Bernhard
Date: July 2025
Technology: Python + SQLite
Course: Python Basics – Talento Tech

🗂 Description
This project is a console-based Python application designed to manage a product inventory using an SQLite database. It was created as the final assignment for the course, integrating data structures, validation, modularization, and data persistence.

⚙️ Key Features
📥 Add products with name and price validation

📋 List all products with their indexes

🗑 Delete products selected by the user

💾 Automatic saving into SQLite database (inventario.db)

📄 Project Files
File	Description
inventario.py	Main script with the program menu
gestion_productos.py	Module with functions to manage products
inventario.db	SQLite database used to store product data
requirements.txt	Project dependencies
README.md	Project documentation

▶️ How to run the program

Option 1: direct execution
1. Make sure you have Python 3.13 or later installed.
2. Open a terminal in the project folder.
3. Run: python inventario.py

Option 2: using a virtual environment
1. Create the virtual environment:
python -m venv .venv
2. Activate it in PowerShell:
.venv\Scripts\Activate.ps1
3. Run the program:
python inventario.py

##Dependencies
This project mainly uses Python standard library modules.
At the moment, requirements.txt may be empty because no additional external packages were installed.

##Final comments
This project was a great opportunity to apply everything learned during the Python Basics course by Talento Tech.
It involved using lists, control structures, modularized code and the sqlite3 database module.