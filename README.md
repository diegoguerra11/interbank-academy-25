# Proyecto de Manipulación de Cadenas y Columnas

## Introducción

Este proyecto tiene como objetivo realizar manipulaciones de cadenas y columnas numéricas en un marco de datos, permitiendo aplicar operaciones matemáticas, agrupar datos, realizar restas y otras transformaciones específicas. Está diseñado para facilitar el procesamiento de datos de manera eficiente y organizada, utilizando herramientas como Python y bibliotecas populares como pandas.

## Instrucciones de Ejecución

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/diegoguerra11/interbank-academy-25.git
   ```

2. Navega a la carpeta del proyecto:
   ```bash
   cd interbank-academy-25
   ```

3. Asegúrate de tener todas las dependencias instaladas. Si no las tienes, puedes instalarlas utilizando `python`:
   ```bash
   python -m venv .venv
   ```

4. Asegúrate de tener todas las dependencias instaladas. Si no las tienes, puedes instalarlas utilizando `python`:
   ```bash
   .venv/Scripts/activate (windows)
   /.venv/bin/activate (linux or macOS)
   ```

5. Asegúrate de tener todas las dependencias instaladas. Si no las tienes, puedes instalarlas utilizando `pip`:
   ```bash
   pip install -r requirements.txt
   ```

6. Para ejecutar el script de ejemplo:
   ```bash
   python main.py
   ```

## Enfoque y Solución

El enfoque principal del proyecto es trabajar con columnas de datos numéricos y categóricos en un DataFrame para aplicar operaciones matemáticas de forma eficiente. Las principales operaciones que se pueden realizar incluyen:

- Agrupación de datos según una columna categórica.
- Realización de operaciones matemáticas (como sumas, restas, multiplicaciones) en columnas numéricas.
- Manipulación de cadenas para crear nuevas columnas con información procesada.

El objetivo es proporcionar una estructura flexible que permita aplicar diversas transformaciones sobre los datos, facilitando su análisis y posterior utilización en informes o exportaciones.

## Estructura del Proyecto

```
/tu-repositorio
│
├── __pycache__/           # Archivos generados por Python para optimización
│
├── .venv/                 # Entorno virtual para las dependencias del proyecto
│
├── data/                  # Carpeta donde se encuentran los archivos de datos
│   └── data.csv
│
├── utils/                 # Funciones y utilidades auxiliares
│   └── helpers.py
│
├── .gitignore             # Archivos y directorios ignorados por Git
├── main.py                # Script principal del proyecto
├── README.md              # Este archivo de documentación
└── requirements.txt       # Archivo de dependencias de Python
```