import shutil
import os
from pathlib import Path

print("📂 Iniciando el proceso de actualización de archivos...")

origen = Path("D:/Indigo Projekt/Proyectos en CODESYS/bauer_stromnetze_berlin/")
destino = Path("C:/Users/lmend/OneDrive/00 Programmierung/2025-220 Bauer Stromnetze Berlin/Unterlagen/")

print(f"📁 Carpeta de origen: {origen}")
print(f"📁 Carpeta de destino: {destino}\n")

archivos_procesados = 0
archivos_actualizados = 0

for archivo_origen in origen.rglob("*.*"):
    if archivo_origen.is_file():
        archivos_procesados += 1
        nombre = archivo_origen.name
        
        archivo_destino = next((f for f in destino.rglob(nombre) if f.is_file()), None)

        if archivo_destino:
            fecha_origen = archivo_origen.stat().st_mtime
            fecha_destino = archivo_destino.stat().st_mtime
            
            if fecha_origen > fecha_destino:
                print(f"🔄 Actualizando: {nombre}")
                os.remove(archivo_destino)
                shutil.copy2(archivo_origen, archivo_destino)
                archivos_actualizados += 1

print(f"\n📊 Resumen:")
print(f"   - Archivos procesados: {archivos_procesados}")
print(f"   - Archivos actualizados: {archivos_actualizados}")