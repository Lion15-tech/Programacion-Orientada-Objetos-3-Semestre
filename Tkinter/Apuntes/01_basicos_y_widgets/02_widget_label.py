import tkinter as tk

ventana = tk.Tk()
ventana.title("Widget Label")
ventana.geometry("500x900+50+50")

# Colores y Fuentes
P5_ROJO = "#D30000"
P5_BLANCO = "#FFFFFF"

# Le pasas primero el nombre, tamaño y al final negritas, cursiva, etc.
# La fuente Earwing Factory hay que instalarla
# Esta le da ese toque de Persona 5
fuente_Persona5 = ("Earwig Factory", 20)

# Etiquetas
etiqueta = tk.Label(ventana,
                text="H o l a  m u n d o !", 
                bg=P5_ROJO,                                                                 #bg es la abreviación de Background, o sea fondo
                fg=P5_BLANCO,                                                               #fg es la abreviación de Foreground, que no se que sea pero es el color de letra
                border=5,                                                                   #Este es el borde que habrá al rededor del texto
                cursor="hand1",                                                             #Este es el tipo de cursos que aparece si lo pasas por encima 
                state="normal",                                                             #Este hace que el texto cambie de color para que parezca deshabilitado
                disabledforeground="light grey",                                            #Esto define el color para cuando este deshabilitado
                activeforeground="RoyalBlue2",                                              #Lo mismo para el modo
                font=fuente_Persona5                                                        #Fuente elegida para el texto
                )
# Muestra la etiqueta en la ventana
etiqueta.pack()

ventana.mainloop()