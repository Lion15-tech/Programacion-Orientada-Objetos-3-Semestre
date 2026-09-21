import tkinter as tk

ventana = tk.Tk()
ventana.title("Eliminar texto en el widget Text")
ventana.geometry("500x900+50+50")

contador_lineas = 0

P5_NEGRO = "#000000"
P5_BLANCO = "#FFFFFF"
fuente_boton = ("TimesNewRoman", 10, "bold italic")

texto = tk.Text(ventana)
texto.config(width=25, height=10)
texto.pack()
texto.insert("1.0", "Texto de prueba línea 1\nTexto de prueba línea 2\n")

# También podemos utilizar el método delete para eliminar texto
# Su sintaxis es la siguiente: widget_de_texto.delete(posición_inicial, posición_final)
# O sea especificamos un rango de donde a donde borrar
def eliminar_texto_completo():
    texto.delete("1.0", tk.END)                                                                     #Esto borra todo el texto del widget

def eliminar_un_rango():
    texto.delete("1.0", "2.end")                                                                      #Esto borra desde la línea 1, caracter 0 hasta la línea 2, caracter 25

# Podemos agregar 2 botones más para usar ambas funciones
boton_eliminar_completo = tk.Button(ventana,
                text="ELIMINAR TEXTO COMPLETO",
                font=fuente_boton,
                bg=P5_NEGRO,
                fg=P5_BLANCO,
                activebackground=P5_BLANCO,
                activeforeground=P5_NEGRO,
                border=10,
                command=eliminar_texto_completo
                )
boton_eliminar_completo.pack()

boton_eliminar_rango = tk.Button(ventana,
                text="ELIMINAR RANGO DE TEXTO",
                font=fuente_boton,
                bg=P5_NEGRO,
                fg=P5_BLANCO,
                activebackground=P5_BLANCO,
                activeforeground=P5_NEGRO,
                border=10,
                command=eliminar_un_rango
                )
boton_eliminar_rango.pack()


def insertar_texto():
    global contador_lineas
    contador_lineas += 1
    texto.insert(tk.END, f"Línea {contador_lineas}\n")                                             #END es una posición especial que hace que el texto se inserte al final del widget

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