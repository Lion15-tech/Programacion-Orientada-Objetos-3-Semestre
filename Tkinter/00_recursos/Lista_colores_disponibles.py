'''
Este código te permite visualizar, probar y copiar los diferentes colores nativos de Tkinter
'''
import tkinter as tk

def actualizar_color(event):
    """Función que cambia el fondo y texto según el color seleccionado"""
    seleccion = lista_colores.curselection()
    
    if seleccion:
        color_seleccionado = lista_colores.get(seleccion)
        
        # 1. Intentar aplicar el color al fondo de la zona de pruebas
        try:
            zona_pruebas.config(bg=color_seleccionado)
            lbl_muestra.config(bg=color_seleccionado)
            
            # 2. Calcular contraste básico para que el texto sea legible
            # Si es un color muy oscuro, ponemos el texto blanco; si es claro, negro.
            colores_oscuros = ["black", "darkblue", "navy", "maroon", "purple", "indigo", "midnightblue", "darkgreen"]
            if any(oscuro in color_seleccionado.lower() for oscuro in colores_oscuros) or color_seleccionado == "gray10":
                lbl_muestra.config(fg="white")
            else:
                lbl_muestra.config(fg="black")
                
            # 3. Actualizar etiquetas y habilitar botón de copia
            lbl_muestra.config(text=f"Fondo: {color_seleccionado}")
            lbl_nombre_color.config(text=f"Color activo: '{color_seleccionado}'", fg="black")
            btn_copiar.config(state=tk.NORMAL, text="📋 Copiar Nombre")
        except tk.TclError:
            # Por si algún sistema operativo no reconoce un color específico
            lbl_muestra.config(text="Color no soportado en este OS", fg="red")

def copiar_al_portapapeles(event=None):
    """Función para copiar el nombre del color seleccionado al portapapeles"""
    seleccion = lista_colores.curselection()
    
    if seleccion:
        color_seleccionado = lista_colores.get(seleccion)
        
        root.clipboard_clear()
        root.clipboard_append(f"'{color_seleccionado}'") # Se copia listo con comillas
        root.update()
        
        btn_copiar.config(text="✅ ¡Copiado!")
        lbl_nombre_color.config(text=f"¡Copiado '{color_seleccionado}' al portapapeles!", fg="#27ae60")

# 1. Configuración de la ventana principal
root = tk.Tk()
root.title("Visor de Colores de Tkinter")
root.geometry("500x650")

# 2. Contenedor para la lista y el scrollbar
frame_lista = tk.Frame(root)
frame_lista.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_colores = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, font=("Arial", 11))
lista_colores.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=lista_colores.yview)


# 3. Contenedor inferior para la vista previa del color
frame_previa = tk.LabelFrame(root, text=" Vista Previa del Color ", padx=10, pady=10)
frame_previa.pack(padx=15, pady=15, fill=tk.X)

# Zona interactiva que cambiará de color de fondo
zona_pruebas = tk.Frame(frame_previa, height=100, bd=2, relief=tk.GROOVE, bg="#ffffff")
zona_pruebas.pack(fill=tk.X, pady=10)
zona_pruebas.pack_propagate(False)

lbl_muestra = tk.Label(zona_pruebas, text="Selecciona un color arriba", font=("Arial", 14, "bold"), bg="#ffffff", fg="gray")
lbl_muestra.pack(expand=True)

# Etiqueta informativa con el nombre del color activo o aviso de copiado
lbl_nombre_color = tk.Label(frame_previa, text="Ningún color seleccionado", font=("Arial", 10, "italic"), fg="gray")
lbl_nombre_color.pack(pady=5)

# Botón para copiar
btn_copiar = tk.Button(frame_previa, text="📋 Copiar Nombre", font=("Arial", 10, "bold"), state=tk.DISABLED, command=copiar_al_portapapeles)
btn_copiar.pack(pady=5)

# 4. Lista seleccionada de colores estándar de Tkinter (organizados alfabéticamente)
colores_tkinter = sorted([
    "white", "black", "red", "green", "blue", "yellow", "magenta", "cyan",
    "gray", "lightgray", "darkgray", "bisque", "blanchedalmond", "blueviolet",
    "brown", "burlywood", "cadetblue", "chocolate", "coral", "cornflowerblue",
    "cornsilk", "crimson", "darkblue", "darkcyan", "darkgoldenrod", "darkgreen",
    "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid",
    "darkred", "darksalmon", "darkseagreen", "darkslate honesty", "darkslateblue",
    "darkslategray", "darkturquoise", "darkviolet", "deeppink", "deepskyblue",
    "dimgray", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "gainsboro",
    "ghostwhite", "gold", "goldenrod", "honeydew", "hotpink", "indianred", "indigo",
    "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue",
    "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgreen", "lightpink",
    "lightsalmon", "lightseagreen", "lightskyblue", "lightslateblue", "lightslategray",
    "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "maroon",
    "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy",
    "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod",
    "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru",
    "pink", "plum", "powderblue", "purple", "royalblue", "saddlebrown", "salmon",
    "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue",
    "slategray", "snow", "springgreen", "steelblue", "tan", "teal", "thistle",
    "tomato", "turquoise", "violet", "wheat", "whitesmoke", "yellowgreen",
    "gray10", "gray25", "gray50", "gray75", "gray90"
])

for color in colores_tkinter:
    lista_colores.insert(tk.END, color)

# 5. Eventos
lista_colores.bind("<<ListboxSelect>>", actualizar_color)
root.bind("<Control-c>", copiar_al_portapapeles)

# Iniciar la aplicación
root.mainloop()
