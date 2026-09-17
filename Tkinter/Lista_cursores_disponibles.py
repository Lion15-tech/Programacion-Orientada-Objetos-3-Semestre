'''
Este código te permite visualizar, probar y copiar los diferentes cursores nativos de Tkinter
'''
import tkinter as tk

def actualizar_cursor(event):
    """Función que cambia el cursor cuando el usuario selecciona uno de la lista"""
    seleccion = lista_cursores.curselection()
    
    if seleccion:
        cursor_seleccionado = lista_cursores.get(seleccion)
        
        # Aplicar el cursor al área de pruebas
        zona_pruebas.config(cursor=cursor_seleccionado)
        
        # Actualizar texto de instrucción y habilitar botón de copia
        lbl_instruccion.config(text="¡Mueve el ratón aquí dentro para ver el cursor!", fg="#2ecc71", font=("Arial", 11, "bold"))
        lbl_nombre_cursor.config(text=f"Cursor activo: '{cursor_seleccionado}'", fg="black")
        btn_copiar.config(state=tk.NORMAL, text="📋 Copiar Nombre")

def copiar_al_portapapeles(event=None):
    """Función para copiar el nombre del cursor seleccionado al portapapeles"""
    seleccion = lista_cursores.curselection()
    
    if seleccion:
        cursor_seleccionado = lista_cursores.get(seleccion)
        
        # Limpiar portapapeles y añadir el nuevo texto
        root.clipboard_clear()
        root.clipboard_append(f"'{cursor_seleccionado}'") # Se copia con comillas listo para usar en tu código
        root.update() # Mantiene el texto en el portapapeles después de cerrar la app
        
        # Cambio visual temporal para confirmar el copiado
        btn_copiar.config(text="✅ ¡Copiado!")
        lbl_nombre_cursor.config(text=f"¡Copiado '{cursor_seleccionado}' al portapapeles!", fg="#27ae60")

# 1. Configuración de la ventana principal
root = tk.Tk()
root.title("Visor de Cursores de Tkinter")
root.geometry("500x630")

# 2. Contenedor para la lista y el scrollbar
frame_lista = tk.Frame(root)
frame_lista.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

# 3. Componentes de la lista (Listbox y Scrollbar)
scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_cursores = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, font=("Arial", 11))
lista_cursores.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=lista_cursores.yview)

# 4. Contenedor inferior para el área de pruebas
frame_previa = tk.LabelFrame(root, text=" Área de Pruebas ", padx=10, pady=10)
frame_previa.pack(padx=15, pady=15, fill=tk.X)

# Zona interactiva para el mouse
zona_pruebas = tk.Frame(frame_previa, height=100, bd=2, relief=tk.GROOVE, bg="#f8f9fa")
zona_pruebas.pack(fill=tk.X, pady=10)
zona_pruebas.pack_propagate(False)

lbl_instruccion = tk.Label(zona_pruebas, text="Selecciona un cursor arriba", font=("Arial", 11), bg="#f8f9fa", fg="gray")
lbl_instruccion.pack(expand=True)

# Etiqueta informativa con el nombre del cursor activo o aviso de copiado
lbl_nombre_cursor = tk.Label(frame_previa, text="Ningún cursor seleccionado", font=("Arial", 10, "italic"), fg="gray")
lbl_nombre_cursor.pack(pady=5)

# Botón para copiar (Empieza desactivado hasta que elijas un cursor)
btn_copiar = tk.Button(frame_previa, text="📋 Copiar Nombre", font=("Arial", 10, "bold"), state=tk.DISABLED, command=copiar_al_portapapeles)
btn_copiar.pack(pady=5)

# 5. Lista de cursores estándar soportados por Tkinter
cursores_estandar = sorted([
    "arrow", "circle", "clock", "cross", "crosshair", "diamond_cross", 
    "dot", "dotbox", "exchange", "fleur", "heart", "man", "mouse", 
    "pirate", "plus", "shuttle", "sizing", "spider", "spraycan", 
    "star", "target", "tcross", "trek", "watch", "xterm", "hand1", 
    "hand2", "double_arrow", "sb_h_double_arrow", "sb_v_double_arrow",
    "sb_left_arrow", "sb_right_arrow", "sb_up_arrow", "sb_down_arrow",
    "bottom_left_corner", "bottom_right_corner", "top_left_corner", "top_right_corner",
    "bottom_side", "top_side", "left_side", "right_side"
])

for cursor in cursores_estandar:
    lista_cursores.insert(tk.END, cursor)

# 6. Eventos
lista_cursores.bind("<<ListboxSelect>>", actualizar_cursor)
root.bind("<Control-c>", copiar_al_portapapeles) # Atajo opcional de teclado

# Iniciar la aplicación
root.mainloop()
