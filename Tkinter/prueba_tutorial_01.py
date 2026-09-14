import tkinter as tk

#Generamos la ventana
ventana = tk.Tk()
ventana.title("Python Interfaces gráficas")
ventana.geometry("500x300")
                #Ancho x Alto

#Demás código:

#Fuentes
fuente_personalizada = ("Consolas", 20, "bold italic")
#Le pasas primero el nombre, tamaño y al final negritas, cursiva, etc.

#Etiquetas
etiqueta = tk.Label(
                text="!Hola mundo!", 
                bg="dark green",                       #bg es la abreviación de Background, o sea fondo
                fg="snow",                             #fg es la abreviación de Foreground, que no se que sea pero es el color de letra
                border=25,                             #Este es el borde que habrá al rededor del texto
                cursor="hand1",                        #Este es el tipo de cursos que aparece si lo pasas por encima 
                state="normal",                        #Este hace que el texto cambie de color para que parezca deshabilitado
                disabledforeground="light grey",       #Esto define el color para cuando este deshabilitado
                activeforeground="RoyalBlue2",         #Lo mismo para el modo
                font=fuente_personalizada              #Fuente elegida para el texto
                )
#Muestra la etiqueta en la ventana
etiqueta.pack()


#Bucle de ejecución
ventana.mainloop()
