import tkinter as tk

#Generamos la ventana
ventana = tk.Tk()
ventana.title("Python Interfaces gráficas")
ventana.geometry("500x300+50+50")
                #Ancho x Alto + coordena_X + coordenada_Y
#Podemos generar ventanas secundarias con
# ventana_secundaria = tk.Toplevel()

#Demás código:


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
                bg=P5_ROJO,                                             #bg es la abreviación de Background, o sea fondo
                fg=P5_BLANCO,                                           #fg es la abreviación de Foreground, que no se que sea pero es el color de letra
                border=5,                                               #Este es el borde que habrá al rededor del texto
                cursor="hand1",                                         #Este es el tipo de cursos que aparece si lo pasas por encima 
                state="normal",                                         #Este hace que el texto cambie de color para que parezca deshabilitado
                disabledforeground="light grey",                        #Esto define el color para cuando este deshabilitado
                activeforeground="RoyalBlue2",                          #Lo mismo para el modo
                font=fuente_Persona5                                    #Fuente elegida para el texto
                )
#Muestra la etiqueta en la ventana
etiqueta.pack()


#Botón
boton = tk.Button(ventana,
                text="Haz click aquí",
                font=fuente_boton,
                bg=P5_NEGRO,
                fg=P5_BLANCO,
                activebackground=P5_BLANCO,                            #Este hace que cambie el color de fondo cuando esta presionado
                activeforeground=P5_NEGRO,                             #Este hace que cambie el color de letra cuando esta presionado
                border=10
                )
boton.pack()


#Entrada de texto
entrada = tk.Entry(ventana,
                bg= "snow3",
                fg= P5_ROJO,
                bd="5",                                                #bd quiere decir Borde, además es necesario para el relief
                relief="sunken",                                       #esto le da como una especie de efecto  al rededor, depende de cual escojas
                cursor="xterm",                                        #Es el cursos predeterminado cuando hay un campo de texto
                state="normal",
                )
entrada.pack()



#Bucle de ejecución
ventana.mainloop()
