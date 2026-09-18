import tkinter as tk

ventana = tk.Tk()
ventana.title("Widget Entry")
ventana.geometry("500x900+50+50")

# Colores
P5_ROJO = "#D30000"

# Entrada de texto
entrada = tk.Entry(ventana,
                bg= "snow3",
                fg= P5_ROJO,
                bd="5",                                                                     #bd quiere decir Borde, además es necesario para el relief
                relief="sunken",                                                            #esto le da como una especie de efecto  al rededor, depende de cual escojas
                cursor="xterm",                                                             #Es el cursos predeterminado cuando hay un campo de texto
                state="normal",
                )
entrada.pack()

ventana.mainloop()