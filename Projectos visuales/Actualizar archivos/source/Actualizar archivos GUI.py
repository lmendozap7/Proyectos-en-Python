import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
from ttkthemes import ThemedStyle
import shutil
import os
from pathlib import Path
from datetime import datetime

class ActualizadorArchivos:
    def __init__(self, root):
        self.root = root
        self.root.title("Actualizador de Archivos")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Establecer el icono de la ventana
        try:
            self.root.iconbitmap("actualizar.ico")
        except:
            pass  # Si no encuentra el icono, usa el predeterminado

        # Configurar el tema oscuro
        self.style = ThemedStyle(self.root)
        self.style.set_theme("equilux")

        # Configurar colores personalizados
        self.root.configure(bg='#1e1e1e')  # Color de fondo principal
        self.style.configure("TFrame", background='#1e1e1e')
        self.style.configure("TButton", 
                           background='#2d2d2d',
                           foreground='#d4d4d4',
                           borderwidth=1,
                           focusthickness=0,
                           focuscolor='none')
        self.style.configure("TLabel", 
                           background='#1e1e1e',
                           foreground='#d4d4d4')
        self.style.configure("TEntry", 
                           fieldbackground='#2d2d2d',
                           foreground='#d4d4d4',
                           insertcolor='#d4d4d4')
        
        # Variables para las rutas
        self.origen_var = tk.StringVar()
        self.destino_var = tk.StringVar()
        
        # Crear el marco principal
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Sección de origen
        ttk.Label(main_frame, text="Carpeta de origen:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(main_frame, textvariable=self.origen_var, width=60).grid(row=0, column=1, padx=5)
        ttk.Button(main_frame, text="Examinar", command=self.seleccionar_origen).grid(row=0, column=2)
        
        # Sección de destino
        ttk.Label(main_frame, text="Carpeta de destino:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(main_frame, textvariable=self.destino_var, width=60).grid(row=1, column=1, padx=5)
        ttk.Button(main_frame, text="Examinar", command=self.seleccionar_destino).grid(row=1, column=2)
        
        # Área de log con tema oscuro
        self.log_area = scrolledtext.ScrolledText(main_frame, width=70, height=20,
                                                 bg='#1e1e1e',
                                                 fg='#d4d4d4',
                                                 insertbackground='#d4d4d4',
                                                 selectbackground='#264f78',
                                                 selectforeground='#ffffff')
        self.log_area.grid(row=2, column=0, columnspan=3, pady=10, padx=10, sticky='nsew')
        
        # Configurar los colores del área de log
        self.log_area.configure(font=('Consolas', 10))
        
        # Barra de progreso con tema oscuro
        self.progreso = ttk.Progressbar(main_frame, length=300, mode='determinate',
                                      style='Horizontal.TProgressbar')
        self.progreso.grid(row=3, column=0, columnspan=3, pady=10)
        
        # Configurar estilo de la barra de progreso
        self.style.configure("Horizontal.TProgressbar",
                           troughcolor='#2d2d2d',
                           background='#0e639c',
                           darkcolor='#0e639c',
                           lightcolor='#0e639c')
        
        # Botón de actualizar
        ttk.Button(main_frame, text="Actualizar Archivos", command=self.actualizar_archivos).grid(row=4, column=0, columnspan=3)
        
        # Cargar rutas predeterminadas si existen
        self.cargar_rutas_predeterminadas()

    def cargar_rutas_predeterminadas(self):
        try:
            origen = Path("D:/Indigo Projekt/Proyectos en CODESYS/bauer_stromnetze_berlin/")
            destino = Path("C:/Users/lmend/OneDrive/00 Programmierung/2025-220 Bauer Stromnetze Berlin/Unterlagen/")
            
            if origen.exists():
                self.origen_var.set(str(origen))
            if destino.exists():
                self.destino_var.set(str(destino))
        except:
            pass

    def seleccionar_origen(self):
        carpeta = filedialog.askdirectory()
        if carpeta:
            self.origen_var.set(carpeta)
    
    def seleccionar_destino(self):
        carpeta = filedialog.askdirectory()
        if carpeta:
            self.destino_var.set(carpeta)
    
    def log(self, mensaje):
        tiempo = datetime.now().strftime("%H:%M:%S")
        self.log_area.insert(tk.END, f"[{tiempo}] {mensaje}\n")
        self.log_area.see(tk.END)
        self.root.update()
    
    def actualizar_archivos(self):
        origen = Path(self.origen_var.get())
        destino = Path(self.destino_var.get())
        
        if not origen.exists() or not destino.exists():
            self.log("❌ Error: Las carpetas de origen y destino deben existir")
            return
        
        self.log("📂 Iniciando proceso de actualización...")
        self.log(f"📁 Carpeta de origen: {origen}")
        self.log(f"📁 Carpeta de destino: {destino}\n")
        
        archivos_procesados = 0
        archivos_actualizados = 0
        
        # Primero contamos los archivos para la barra de progreso
        total_archivos = sum(1 for _ in origen.rglob("*.*") if _.is_file())
        self.progreso["maximum"] = total_archivos
        
        for archivo_origen in origen.rglob("*.*"):
            if archivo_origen.is_file():
                archivos_procesados += 1
                self.progreso["value"] = archivos_procesados
                
                nombre = archivo_origen.name
                archivo_destino = next((f for f in destino.rglob(nombre) if f.is_file()), None)
                
                if archivo_destino:
                    fecha_origen = archivo_origen.stat().st_mtime
                    fecha_destino = archivo_destino.stat().st_mtime
                    
                    if fecha_origen > fecha_destino:
                        self.log(f"🔄 Actualizando: {nombre}")
                        try:
                            os.remove(archivo_destino)
                            shutil.copy2(archivo_origen, archivo_destino)
                            archivos_actualizados += 1
                        except Exception as e:
                            self.log(f"❌ Error al actualizar {nombre}: {str(e)}")
        
        self.log("\n📊 Resumen:")
        self.log(f"   - Archivos procesados: {archivos_procesados}")
        self.log(f"   - Archivos actualizados: {archivos_actualizados}")
        
        # Resetear la barra de progreso
        self.progreso["value"] = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = ActualizadorArchivos(root)
    root.mainloop()