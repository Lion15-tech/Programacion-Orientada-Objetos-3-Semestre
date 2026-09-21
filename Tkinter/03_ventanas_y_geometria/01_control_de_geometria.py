import tkinter as tk

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Control de Geometría con geometry()")

# SINTAXIS DEL MÉTODO GEOMETRY:
# ventana.geometry("ANCHO x ALTO + COORDENADA_X + COORDENADA_Y")
# - Ancho y Alto: Definidos en píxeles (separados obligatoriamente por la letra 'x' en minúscula).
# - Coordenada X: Distancia en píxeles desde el borde izquierdo de la pantalla (+X mueve a la derecha).
# - Coordenada Y: Distancia en píxeles desde el borde superior de la pantalla (+Y mueve hacia abajo).

# Definición de dimensiones en variables para facilitar su manipulación
ancho_ventana = 500
alto_ventana = 300
pos_x = 200
pos_y = 100

# Aplicamos la geometría inicial usando f-strings
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

# Colores
P5_NEGRO = "#000000"
P5_BLANCO = "#FFFFFF"
P5_ROJO = "#D30000"

# Etiqueta informativa
etiqueta_info = tk.Label(
    ventana,
    text=f"Dimensiones actuales: {ancho_ventana}x{alto_ventana}\nPosición en pantalla: X={pos_x}, Y={pos_y}",
    bg=P5_NEGRO,
    fg=P5_BLANCO,
    font=("Arial", 11),
    pady=10
)
etiqueta_info.pack(pady=20)

# Función para modificar la geometría en tiempo de ejecución
def redimensionar():
    # También se pueden usar valores negativos para alinear respecto a bordes derechos o inferiores:
    # "500x300-100-100" coloca la ventana a 100px del borde derecho e inferior.
    nueva_geometria = "600x400+50+50"
    ventana.geometry(nueva_geometria)
    etiqueta_info.config(
        text="Dimensiones actualizadas: 600x400\nPosición en pantalla: X=50, Y=50",
        bg=P5_ROJO
    )

# Botón para cambiar el tamaño y posición dinámicamente
boton_redimensionar = tk.Button(
    ventana,
    text="APLICAR NUEVA GEOMETRÍA",
    bg=P5_NEGRO,
    fg=P5_BLANCO,
    activebackground=P5_BLANCO,
    activeforeground=P5_NEGRO,
    border=5,
    command=redimensionar
)
boton_redimensionar.pack(pady=10)

# Bucle principal
ventana.mainloop()

'''
Conceptos clave del apunte:

Formato de cadena en .geometry(): Es estrictamente una 
cadena con la estructura "AnchoxAlto+X+Y". Usar 'x' 
minúscula entre el ancho y alto es obligatorio.

Coordenadas relativas a pantalla: +X cuenta desde la 
esquina superior izquierda de tu monitor hacia la derecha,
mientras que +Y cuenta hacia abajo.

Valores negativos (-X-Y): Si sustituyes los signos + 
por -, Tkinter calculará la posición de la ventana 
partiendo desde la esquina inferior derecha del monitor.
'''