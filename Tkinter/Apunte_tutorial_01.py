import tkinter as tk

#Generamos la ventana
ventana = tk.Tk()
ventana.title("Python Interfaces gráficas")
ventana.geometry("500x300+50+50")
                #Ancho x Alto + coordena_X + coordenada_Y

#Podemos generar ventanas secundarias con
# ventana_secundaria = tk.Toplevel()

#Demás código:
contador_lineas = 0

#Colores y Fuentes
P5_ROJO = "#D30000"
P5_NEGRO = "#000000"
P5_BLANCO = "#FFFFFF"

#Le pasas primero el nombre, tamaño y al final negritas, cursiva, etc.
#La fuente Earwing Factory hay que instalarla
#Esta le da ese toque de Persona 5
fuente_Persona5 = ("Earwig Factory", 20)
fuente_boton = ("TimesNewRoman", 10, "bold italic")

#Puedes hacer un archivo a parte con todas las fuentes que vayas a utilizar
#para que sea más facil utilizarlas


#Etiquetas
etiqueta = tk.Label(ventana,
                text="H o l a  m u n d o !", 
                bg=P5_ROJO,                                                                         #bg es la abreviación de Background, o sea fondo
                fg=P5_BLANCO,                                                                       #fg es la abreviación de Foreground, que no se que sea pero es el color de letra
                border=5,                                                                           #Este es el borde que habrá al rededor del texto
                cursor="hand1",                                                                     #Este es el tipo de cursos que aparece si lo pasas por encima 
                state="normal",                                                                     #Este hace que el texto cambie de color para que parezca deshabilitado
                disabledforeground="light grey",                                                    #Esto define el color para cuando este deshabilitado
                activeforeground="RoyalBlue2",                                                      #Lo mismo para el modo
                font=fuente_Persona5                                                                #Fuente elegida para el texto
                )
#Muestra la etiqueta en la ventana
etiqueta.pack()


#El método insert
#Esta función se puede asociar a un botón mediante el parámetro command 
#tal cual como esta abajo en el botón

#Su sintaxis es la siguiente: widget_de_texto.insert(posición, "texto a insertar")
def insertar_texto():
    global contador_lineas
    contador_lineas += 1
    #En vez de tk.END podemos usar "end" nada más
    texto.insert(tk.END, f"Línea {contador_lineas}\n")                                              #END es una posición especial que hace que el texto se inserte al final del widget
#Además de END, podemos utilizar INSERT que hace que el texto se inserte en la posición del cursor, 
#o también podemos utilizar un número "2.3" (en la fila 2, columna carácter 3 (o posición 4 porque cuenta de 0)) 
#que representa la posición en la que queremos insertar el texto

#Botón
boton = tk.Button(ventana,
                text="INSERTAR TEXTO",
                font=fuente_boton,
                bg=P5_NEGRO,
                fg=P5_BLANCO,
                activebackground=P5_BLANCO,                                                         #Este hace que cambie el color de fondo cuando esta presionado
                activeforeground=P5_NEGRO,                                                          #Este hace que cambie el color de letra cuando esta presionado
                border=10,
                command=insertar_texto                                                              #Este es el parámetro que llama la función para que se ejecute
                )
boton.pack()


#Entrada de texto
entrada = tk.Entry(ventana,
                bg= "snow3",
                fg= P5_ROJO,
                bd="5",                                                                             #bd quiere decir Borde, además es necesario para el relief
                relief="sunken",                                                                    #esto le da como una especie de efecto  al rededor, depende de cual escojas
                cursor="xterm",                                                                     #Es el cursos predeterminado cuando hay un campo de texto
                state="normal",
                )
entrada.pack()


#Widget text
#Este widget tiene muchos de las cosas para personalizarlo 
#al igual que los anteriores, así que no me pondré a detallar 
#mucho en eso
texto = tk.Text(ventana,)
#Podemos utilizar el método config para definir el tamaño
#o también podemos definirlo al momento de crearlo
texto.config(width=25, height=10)                                                                   #El tamaño no se mide en pixeles, sino que en carácteres
texto.pack()


#Así mismo igual se puede usar el método insert sin necesidad de una función
texto.insert("1.0", "Este texto se inserta al inicio del programa\n")

#También podemos utilizar el método delete para eliminar texto
#Su sintaxis es la siguiente: widget_de_texto.delete(posición_inicial, posición_final)
#O sea especificamos un rango de donde a donde borrar
def eliminar_texto_completo():
    texto.delete("1.0", tk.END)                                                                     #Esto borra todo el texto del widget

def eliminar_un_rango():
    texto.delete("1.0", "2.end")                                                                       #Esto borra desde la línea 1, caracter 0 hasta la línea 2, caracter 25

#Podemos agregar 2 botones más para usar ambas funciones
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


#Método get
#Este método nos permite obtener el texto que hay en un widget de texto
#su sintaxis es la siguiente: widget_de_texto.get(posición_inicial, posición_final)
def obtener_texto():
    texto_obtenido = texto.get("1.0", tk.END)                                                        #Esto obtiene todo el texto del widget
    print(texto_obtenido)
#Botón para obtener el texto
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

#De la misma manera podemos obtener el texto seleccionado
def obtener_texto_seleccionado():
    texto_seleccionado = texto.get(tk.SEL_FIRST, tk.SEL_LAST)                                        #Sel.FIRST y SEL_LAST son cosas que representan el inicio y el final del texto seleccionado
    print(texto_seleccionado)
#Botón para obtener el texto seleccionado
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

#Bucle de ejecución
ventana.mainloop()
