'''
Este código te permite ver, probar y copiar todas las fuentes que tengas instaladas en tu computadora
'''
import tkinter as tk
from tkinter.font import families

def actualizar_vista_previa(event):
    """Función que se ejecuta cuando el usuario selecciona una fuente"""
    # Obtener el índice del elemento seleccionado
    seleccion = lista_fuentes.curselection()
    
    if seleccion:
        # Obtener el nombre de la fuente según el índice
        fuente_seleccionada = lista_fuentes.get(seleccion[0])
        # Actualizar la tipografía de la etiqueta de vista previa (Tamaño 24)
        lbl_vista_previa.config(font=(fuente_seleccionada, 24))
        # Mostrar el nombre de la fuente en el texto de abajo
        lbl_nombre_fuente.config(text=f"Fuente actual: {fuente_seleccionada}", fg="black")
        # Habilitar el botón de copia y restablecer su texto original
        btn_copiar.config(state=tk.NORMAL, text="📋 Copiar Nombre")

def copiar_al_portapapeles(event=None):
    """Función para copiar el nombre de la fuente seleccionada al portapapeles"""
    seleccion = lista_fuentes.curselection()
    
    if seleccion:
        fuente_seleccionada = lista_fuentes.get(seleccion[0])
        
        # Limpiar portapapeles y añadir el nuevo texto
        root.clipboard_clear()
        root.clipboard_append(f"'{fuente_seleccionada}'") # Se copia con comillas listo para usar
        root.update() # Mantiene el texto en el portapapeles tras cerrar la app
        
        # Cambio visual temporal para confirmar el copiado
        btn_copiar.config(text="✅ ¡Copiado!")
        lbl_nombre_fuente.config(text=f"¡Copiado '{fuente_seleccionada}' al portapapeles!", fg="#27ae60")

# 1. Configuración de la ventana principal
root = tk.Tk()
root.title("Visor de Fuentes de Sistema")
root.geometry("500x650") # Ajustado ligeramente el alto para el botón

# 2. Contenedor para la lista y el scrollbar
frame_lista = tk.Frame(root)
frame_lista.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

# 3. Componentes de la lista (Listbox y Scrollbar)
scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_fuentes = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, font=("Arial", 11))
lista_fuentes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=lista_fuentes.yview)

# 4. Contenedor inferior para la vista previa
frame_previa = tk.LabelFrame(root, text=" Vista Previa ", padx=10, pady=10)
frame_previa.pack(padx=15, pady=15, fill=tk.X)

# Texto de ejemplo que cambiará de forma
lbl_vista_previa = tk.Label(frame_previa, text="AbcDeF 12345 !@#", font=("Arial", 24))
lbl_vista_previa.pack(pady=10)

# Etiqueta informativa con el nombre de la fuente activa o aviso de copiado
lbl_nombre_fuente = tk.Label(frame_previa, text="Selecciona una fuente arriba", font=("Arial", 10, "italic"), fg="gray")
lbl_nombre_fuente.pack(pady=5)

# Botón para copiar (Empieza desactivado hasta que elijas una fuente)
btn_copiar = tk.Button(frame_previa, text="📋 Copiar Nombre", font=("Arial", 10, "bold"), state=tk.DISABLED, command=copiar_al_portapapeles)
btn_copiar.pack(pady=5)

# 5. Llenar la lista usando el bucle 'for'
fuentes_unicas = sorted(set(families()))
for fuente in fuentes_unicas:
    if fuente and not fuente.startswith("@"):  # Elige nombres válidos y evita fuentes verticales de Windows
        lista_fuentes.insert(tk.END, fuente)

# 6. Eventos
lista_fuentes.bind("<<ListboxSelect>>", actualizar_vista_previa)
root.bind("<Control-c>", copiar_al_portapapeles) # Atajo opcional de teclado

# Iniciar la aplicación
root.mainloop()
