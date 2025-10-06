# Actualizador de Archivos

Este proyecto contiene un programa para sincronizar archivos entre dos carpetas, manteniendo la versión más reciente en la carpeta de destino.

## Archivos del Proyecto

- `Actualizar archivos GUI.py`: Versión con interfaz gráfica del programa
- `Actualizar archivos.py`: Versión de línea de comandos
- `crear_icono.py`: Script para generar el icono de la aplicación
- `actualizar.ico`: Icono de la aplicación
- `requirements.txt`: Lista de dependencias del proyecto
- `Actualizar archivos GUI.spec`: Archivo de configuración para PyInstaller

## Requisitos

```bash
pip install -r requirements.txt
```

## Cómo modificar el código

1. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Modificar los archivos según sea necesario:
   - Para cambios en la interfaz: editar `Actualizar archivos GUI.py`
   - Para cambios en la lógica base: editar `Actualizar archivos.py`
   - Para cambiar el icono: editar `crear_icono.py` y ejecutarlo

3. Crear el ejecutable:
   ```bash
   pyinstaller --onefile --windowed --icon="actualizar.ico" "Actualizar archivos GUI.py"
   ```

## Notas

- El ejecutable se generará en la carpeta `dist`
- Los archivos temporales se crean en la carpeta `build`
- Para cambiar las rutas predeterminadas, modificar las variables `origen` y `destino` en los archivos principales