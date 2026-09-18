import tkinter as tk

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Obtener posición del cursor en Widget Text")
ventana.geometry("500x500+50+50")

# Colores y Fuentes
P5_NEGRO = "#000000"
P5_BLANCO = "#FFFFFF"
P5_ROJO = "#D30000"
fuente_boton = ("TimesNewRoman", 10, "bold italic")

# Widget Text
texto = tk.Text(ventana, width=35, height=10)
texto.pack(pady=10)
texto.insert("1.0", "Haz clic o escribe en cualquier parte...\nSegunda línea de prueba\nTercera línea de prueba")

# Etiqueta para mostrar la información del cursor
etiqueta_posicion = tk.Label(
    ventana, 
    text="Posición del cursor: Línea 1, Columna 0", 
    fg=P5_ROJO, 
    font=("Arial", 11, "bold")
)
etiqueta_posicion.pack(pady=5) # pady=5 añade 5 píxeles de margen externo ARRIBA y ABAJO

# Función para obtener e interpretar el índice del cursor
def obtener_posicion_cursor():
    # tk.INSERT (o el string "insert") es la constante que referencia la ubicación exacta del cursor activo.
    # El método .index() transforma la constante "insert" en un string con formato "LÍNEA.COLUMNA" (ej. "2.4").
    posicion_string = texto.index(tk.INSERT)
    
    # Separamos la cadena por el caracter '.' para manipular línea y columna por separado.
    # RECUERDA: En Tkinter las líneas comienzan a contar en 1 y las columnas en 0.
    linea, columna = posicion_string.split('.')
    
    # Actualizamos el texto de la etiqueta con la posición calculada
    etiqueta_posicion.config(text=f"Posición del cursor: Línea {linea}, Columna {columna} (Índice: '{posicion_string}')")
    print(f"Índice obtenido: {posicion_string} -> Línea: {linea}, Columna: {columna}")

# Botón de acción
boton_posicion = tk.Button(
    ventana,
    text="OBTENER POSICIÓN DEL CURSOR",
    font=fuente_boton,
    bg=P5_NEGRO,
    fg=P5_BLANCO,
    activebackground=P5_BLANCO,
    activeforeground=P5_NEGRO,
    border=5,
    command=obtener_posicion_cursor
)
boton_posicion.pack(pady=10)

# Bucle de ejecución
ventana.mainloop()


'''
Detalles clave del apunte:

tk.INSERT: Es el identificador especial de Tkinter para la 
posición donde está parpadeando el cursor de inserción.

.index(tk.INSERT): Retorna una cadena con el formato 
"filas.caracteres" (ejemplo: "1.0" indica fila 1, caracter 0).

.split('.'): Método de cadenas en Python para separar de forma 
limpia el número de fila y columna como variables enteras o 
cadenas individuales.
'''