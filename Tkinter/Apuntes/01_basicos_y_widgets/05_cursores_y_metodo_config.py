import tkinter as tk

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Cursores y método config()")
ventana.geometry("500x500+50+50")

# Colores
P5_NEGRO = "#000000"
P5_BLANCO = "#FFFFFF"
P5_ROJO = "#D30000"

# Etiqueta inicial
# El parámetro 'cursor' define la forma que tomará el puntero del mouse al pasar sobre el widget.
etiqueta = tk.Label(
    ventana,
    text="Texto con estado inicial",
    bg=P5_NEGRO,
    fg=P5_BLANCO,
    font=("Arial", 12, "bold"),
    width=30,
    height=2,
    cursor="hand2"  # Cursor con forma de mano de selección
)
etiqueta.pack(pady=20)

# Función para modificar propiedades en tiempo de ejecución
def cambiar_estilo():
    # El método .config() (o .configure()) permite alterar cualquier parámetro de un widget
    # después de que ya ha sido instanciado y mostrado en pantalla.
    etiqueta.config(
        text="¡Propiedades cambiadas con .config()!",
        bg=P5_ROJO,
        fg=P5_BLANCO,
        cursor="cross"  # Cambiamos el cursor dinámicamente a una cruz de precisión
    )

def restaurar_estilo():
    etiqueta.config(
        text="Texto con estado inicial",
        bg=P5_NEGRO,
        fg=P5_BLANCO,
        cursor="hand2"
    )

# Botones para probar la reconfiguración dinámica
boton_modificar = tk.Button(
    ventana,
    text="APLICAR CONFIGURACIÓN",
    command=cambiar_estilo,
    cursor="sizing"     # Cursor de redimensión
)
boton_modificar.pack(pady=5)

boton_restaurar = tk.Button(
    ventana,
    text="RESTAURAR",
    command=restaurar_estilo,
    cursor="pirate"     # Cursor con forma de calavera
)
boton_restaurar.pack(pady=5)

# Bucle principal de ejecución
ventana.mainloop()

'''
Conceptos clave del apunte:

Método .config(): Permite leer o alterar las propiedades de 
cualquier widget (bg, fg, text, state, etc.) durante la 
ejecución del programa sin necesidad de redefinirlo o 
reempaquetarlo.

Parámetro cursor: Define el tipo de puntero del sistema operativo
al colocar la vista sobre la superficie del widget 
(ejemplos comunes: "hand1", "hand2", "xterm", "cross",
"watch", "pirate").
'''