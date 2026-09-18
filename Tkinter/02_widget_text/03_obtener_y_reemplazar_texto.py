import tkinter as tk

ventana = tk.Tk()
ventana.title("Obtener y reemplazar texto en el widget Text")
ventana.geometry("500x900+50+50")

P5_NEGRO = "#000000"
P5_BLANCO = "#FFFFFF"
fuente_boton = ("TimesNewRoman", 10, "bold italic")

texto = tk.Text(ventana)
texto.config(width=25, height=10)
texto.pack()
texto.insert("1.0", "Texto de ejemplo para obtener o reemplazar\n")

# Método get
# Este método nos permite obtener el texto que hay en un widget de texto
# su sintaxis es la siguiente: widget_de_texto.get(posición_inicial, posición_final)
def obtener_texto():
    texto_obtenido = texto.get("1.0", tk.END)                                                       #Esto obtiene todo el texto del widget
    print(texto_obtenido)

# Botón para obtener el texto
boton_obtener_texto = tk.Button(ventana,
                text="OBTENER TEXTO",
                font=fuente_boton,
                bg=P5_NEGRO,
                fg=P5_BLANCO,
                activebackground=P5_BLANCO,
                activeforeground=P5_NEGRO,
                border=10,
                command=obtener_texto
                )
boton_obtener_texto.pack()

# De la misma manera podemos obtener el texto seleccionado
def obtener_texto_seleccionado():
    texto_seleccionado = texto.get(tk.SEL_FIRST, tk.SEL_LAST)                                       #Sel.FIRST y SEL_LAST son cosas que representan el inicio y el final del texto seleccionado
    print(texto_seleccionado)

# Botón para obtener el texto seleccionado
boton_obtener_seleccionado = tk.Button(ventana,
                    text="OBTENER TEXTO SELECCIONADO",
                    font=fuente_boton,
                    bg=P5_NEGRO,
                    fg=P5_BLANCO,
                    activebackground=P5_BLANCO,
                    activeforeground=P5_NEGRO,
                    border=10,
                    command=obtener_texto_seleccionado
                    )
boton_obtener_seleccionado.pack()

# Modificar texto seleccionado:
def modificar_seleccion():
    nuevo_texto = "Hola Mundo!"
    texto.replace(tk.SEL_FIRST, tk.SEL_LAST, nuevo_texto)

# Botón para reemplazar
boton_modificar_seleccionado = tk.Button(ventana,
                    text="MODIFICAR TEXTO SELECCIONADO",
                    font=fuente_boton,
                    bg=P5_NEGRO,
                    fg=P5_BLANCO,
                    activebackground=P5_BLANCO,
                    activeforeground=P5_NEGRO,
                    border=10,
                    command=modificar_seleccion
                    )
boton_modificar_seleccionado.pack()

ventana.mainloop()