import tkinter as tk

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Widget Button")
ventana.geometry("500x500+50+50")

# Colores y Fuentes
P5_NEGRO = "#000000"
P5_BLANCO = "#FFFFFF"
P5_ROJO = "#D30000"
fuente_boton = ("TimesNewRoman", 12, "bold italic")

# Función de evento que ejecutará el botón
def funcion_al_presionar():
    print("¡Botón presionado correctamente!")
    etiqueta_estado.config(text="Estado: Botón activado")

# Etiqueta auxiliar para reflejar el cambio de estado
etiqueta_estado = tk.Label(
    ventana, 
    text="Estado: Esperando interacción", 
    fg=P5_ROJO, 
    font=("Arial", 11)
)
etiqueta_estado.pack(pady=15)

# Widget Button
# NOTA IMPORTANTE: El parámetro 'command' pasa el nombre de la función SIN paréntesis.
boton_ejemplo = tk.Button(
    ventana,
    text="PRESIONAR AQUÍ",             # Texto desplegado dentro del botón
    font=fuente_boton,                 # Fuente aplicada al texto
    bg=P5_NEGRO,                       # Color de fondo (Background)
    fg=P5_BLANCO,                      # Color de la fuente (Foreground)
    activebackground=P5_ROJO,          # Color de fondo al hacer clic/mantener presionado
    activeforeground=P5_BLANCO,        # Color del texto al hacer clic/mantener presionado
    border=5,                          # Grosor del borde en píxeles (abreviado también como 'bd')
    relief="raised",                   # Estilo tridimensional del borde ('raised', 'sunken', 'flat', 'ridge', 'groove')
    cursor="hand2",                    # Apariencia del cursor al posicionarse sobre el widget
    state="normal",                    # Estado del widget ('normal' para activo, 'disabled' para inhabilitarlo)
    command=funcion_al_presionar       # Vinculación con la función a ejecutar
)
boton_ejemplo.pack(pady=10)

# Bucle principal de ejecución
ventana.mainloop()


'''
Conceptos clave del apunte:

command: Parámetro encargado de vincular una función al evento de clic. 
Se pasa únicamente la referencia de la función (sin ()), ya que de lo 
contrario se ejecutaría de inmediato al iniciar el programa.

activebackground / activeforeground: Controlan la respuesta visual del 
botón durante la interacción directa del usuario (el clic).

state: Permite cambiar la operatividad del botón. Un botón con state="disabled" no responde a clics ni ejecuta el parámetro command.
'''