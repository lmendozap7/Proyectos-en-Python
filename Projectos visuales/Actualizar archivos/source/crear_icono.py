from PIL import Image, ImageDraw
import os
import math

def create_smooth_circle_arc(draw, center, radius, start_angle, end_angle, width, color):
    # Crear un arco suave con antialiasing
    for w in range(-width//2, width//2 + 1):
        r = radius + w
        points = []
        for angle in range(start_angle, end_angle):
            x = center[0] + r * math.cos(math.radians(angle))
            y = center[1] + r * math.sin(math.radians(angle))
            points.append((x, y))
        if points:
            for i in range(len(points) - 1):
                draw.line((points[i], points[i+1]), fill=color, width=1)

def create_smooth_arrow(draw, center_x, center_y, size, color):
    # Crear una flecha suave con antialiasing
    arrow_width = size // 3
    arrow_height = size
    
    # Puntos de la flecha
    points = [
        (center_x, center_y - arrow_height//2),  # Punta superior
        (center_x - arrow_width, center_y),      # Centro izquierdo
        (center_x, center_y + arrow_height//2),  # Punta inferior
    ]
    
    # Dibujar la flecha con borde suave
    draw.polygon(points, fill=color)

def create_refresh_icon(size=256):
    # Colores
    bg_color = (0, 0, 0, 0)  # Transparente
    main_color = (0, 122, 204, 255)  # Azul más profesional
    
    # Crear imagen base
    img = Image.new('RGBA', (size, size), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Calcular dimensiones
    center = (size//2, size//2)
    radius = int(size * 0.35)
    stroke_width = int(size * 0.08)
    
    # Dibujar el arco circular (300 grados para mejor efecto visual)
    create_smooth_circle_arc(draw, center, radius, -30, 270, stroke_width, main_color)
    
    # Calcular posición de la flecha
    arrow_size = int(size * 0.2)
    arrow_x = center[0] + int(radius * math.cos(math.radians(270)))
    arrow_y = center[1] + int(radius * math.sin(math.radians(270)))
    
    # Dibujar la flecha
    create_smooth_arrow(draw, arrow_x, arrow_y, arrow_size, main_color)
    
    # Guardar con múltiples tamaños para mejor calidad
    img.save('actualizar.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])

# Crear el icono
create_refresh_icon()