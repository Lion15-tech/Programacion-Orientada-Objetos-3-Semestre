import tkinter as tk

ventana = tk.Tk()
ventana.title("Widget Text e Insertar Texto")
ventana.geometry("500x900+50+50")

contador_lineas = 0

# Colores y Fuentes
P5_NEGRO = "#000000"
P5_BLANCO = "#FFFFFF"

fuente_boton = ("TimesNewRoman", 10, "bold italic")

# Widget text
# Este widget tiene muchos de las cosas para personalizarlo 
# al igual que los anteriores, así que no me pondré a detallar 
# mucho en eso
texto = tk.Text(ventana,)
# Podemos utilizar el método config para definir el tamaño
# o también podemos definirlo al momento de crearlo
texto.config(width=25, height=10)                                                               #El tamaño no se mide en pixeles, sino que en carácteres
texto.pack()

# Así mismo igual se puede usar el método insert sin necesidad de una función
texto.insert("1.0", "Este texto se inserta al inicio del programa\n")

# El método insert
# Esta función se puede asociar a un botón mediante el parámetro command 
# tal cual como esta abajo en el botón

# Su sintaxis es la siguiente: widget_de_texto.insert(posición, "texto a insertar")
def insertar_texto():
    global contador_lineas
    contador_lineas += 1
    # En vez de tk.END podemos usar "end" nada más
    texto.insert(tk.END, f"Línea {contador_lineas}\n")                                             #END es una posición especial que hace que el texto se inserte al final del widget
# Además de END, podemos utilizar INSERT que hace que el texto se inserte en la posición del cursor, 
# o también podemos utilizar un número "2.3" (en la fila 2, columna carácter 3 (o posición 4 porque cuenta de 0)) 
# que representa la posición en la que queremos insertar el texto

# Botón
boton = tk.Button(ventana,
                text="INSERTAR TEXTO",
                font=fuente_boton,
                bg=P5_NEGRO,
                fg=P5_BLANCO,
                activebackground=P5_BLANCO,                                                         #Este hace que cambie el color de fondo cuando esta presionado
                activeforeground=P5_NEGRO,                                                         #Este hace que cambie el color de letra cuando esta presionado
                border=10,
                command=insertar_texto                                                              #Este es el parámetro que llama la función para que se ejecute
                )
boton.pack()

ventana.mainloop()