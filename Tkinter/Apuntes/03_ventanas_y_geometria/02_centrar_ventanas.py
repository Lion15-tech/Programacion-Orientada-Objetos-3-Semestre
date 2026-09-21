import tkinter as tk

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Centrar ventanas dinámicamente")

# 1. Definir las dimensiones deseadas para la ventana
ancho_ventana = 500
alto_ventana = 300

# 2. Obtener las dimensiones reales de la pantalla del usuario (en píxeles)
# .winfo_screenwidth() -> Devuelve el ancho total del monitor
# .winfo_screenheight() -> Devuelve el alto total del monitor
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# 3. Calcular las coordenadas X e Y para centrar la ventana
# Se usa división entera (//) para obtener números enteros sin decimales
pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

# 4. Asignar la geometría calculada a la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

# Estilos
P5_NEGRO = "#000000"
P5_BLANCO = "#FFFFFF"

# Contenido informativo dentro de la ventana
etiqueta_datos = tk.Label(
    ventana,
    text=f"Resolución de pantalla: {ancho_pantalla}x{alto_pantalla}px\n"
        f"Tamaño de ventana: {ancho_ventana}x{alto_ventana}px\n"
        f"Coordenadas aplicadas: X={pos_x}, Y={pos_y}",
    bg=P5_NEGRO,
    fg=P5_BLANCO,
    font=("Arial", 11),
    justify="left",
    padx=15,
    pady=15
)
etiqueta_datos.pack(pady=50)

# Bucle principal
ventana.mainloop()

'''
Conceptos clave del apunte:
.winfo_screenwidth() / .winfo_screenheight(): 
Métodos que consultan directamente al sistema operativo las dimensiones 
totales del monitor en el que se ejecuta la aplicación.

Fórmula matemática de centrado:
pos_x = (ancho_pantalla - ancho_ventana) / 2
pos_y = (alto_pantalla - alto_ventana) / 2

División entera (//): 
En Python, la barra doble evita la creación
de números flotantes (con decimales) que 
Tkinter no acepta dentro de la cadena de texto de .geometry()
'''