'''
Suite de Diseño Unificada para Tkinter
Herramienta de soporte para visualizar y copiar Fuentes, Cursores y Colores del sistema.
'''
import tkinter as tk
from tkinter import ttk
from tkinter.font import families

# ==========================================
# 1. FUNCIONES DE LÓGICA (EVENTOS)
# ==========================================

# --- Funciones para la pestaña de Fuentes ---
def actualizar_fuente(event):
    seleccion = lista_fuentes.curselection()
    if seleccion:
        fuente_sel = lista_fuentes.get(seleccion)
        lbl_vista_fuente.config(font=(fuente_sel, 24))
        lbl_info_fuente.config(text=f"Fuente actual: {fuente_sel}", fg="black")
        btn_copiar_fuente.config(state=tk.NORMAL, text="📋 Copiar Nombre")

def copiar_fuente(event=None):
    seleccion = lista_fuentes.curselection()
    if seleccion:
        fuente_sel = lista_fuentes.get(seleccion)
        root.clipboard_clear()
        root.clipboard_append(f"'{fuente_sel}'")
        root.update()
        btn_copiar_fuente.config(text="✅ ¡Copiado!")
        lbl_info_fuente.config(text=f"¡Copiado '{fuente_sel}' al portapapeles!", fg="#27ae60")

# --- Funciones para la pestaña de Cursores ---
def actualizar_cursor(event):
    seleccion = lista_cursores.curselection()
    if seleccion:
        cursor_sel = lista_cursores.get(seleccion)
        zona_pruebas_cursor.config(cursor=cursor_sel)
        lbl_instruccion_cursor.config(text="¡Mueve el ratón aquí dentro para ver el cursor!", fg="#2ecc71", font=("Arial", 11, "bold"))
        lbl_info_cursor.config(text=f"Cursor activo: '{cursor_sel}'", fg="black")
        btn_copiar_cursor.config(state=tk.NORMAL, text="📋 Copiar Nombre")

def copiar_cursor(event=None):
    seleccion = lista_cursores.curselection()
    if seleccion:
        cursor_sel = lista_cursores.get(seleccion)
        root.clipboard_clear()
        root.clipboard_append(f"'{cursor_sel}'")
        root.update()
        btn_copiar_cursor.config(text="✅ ¡Copiado!")
        lbl_info_cursor.config(text=f"¡Copiado '{cursor_sel}' al portapapeles!", fg="#27ae60")

# --- Funciones para la pestaña de Colores ---
def actualizar_color(event):
    seleccion = lista_colores.curselection()
    if seleccion:
        color_sel = lista_colores.get(seleccion)
        try:
            zona_pruebas_color.config(bg=color_sel)
            lbl_muestra_color.config(bg=color_sel)
            
            # Contraste inteligente para legibilidad del texto
            colores_oscuros = ["black", "darkblue", "navy", "maroon", "purple", "indigo", "midnightblue", "darkgreen"]
            if any(oscuro in color_sel.lower() for oscuro in colores_oscuros) or color_sel == "gray10":
                lbl_muestra_color.config(fg="white")
            else:
                lbl_muestra_color.config(fg="black")
                
            lbl_muestra_color.config(text=f"Fondo: {color_sel}")
            lbl_info_color.config(text=f"Color activo: '{color_sel}'", fg="black")
            btn_copiar_color.config(state=tk.NORMAL, text="📋 Copiar Nombre")
        except tk.TclError:
            lbl_muestra_color.config(text="Color no soportado en este OS", fg="red")

def copiar_color(event=None):
    seleccion = lista_colores.curselection()
    if seleccion:
        color_sel = lista_colores.get(seleccion)
        root.clipboard_clear()
        root.clipboard_append(f"'{color_sel}'")
        root.update()
        btn_copiar_color.config(text="✅ ¡Copiado!")
        lbl_info_color.config(text=f"¡Copiado '{color_sel}' al portapapeles!", fg="#27ae60")

# --- Manejador Global de Ctrl + C ---
def copiar_atajo_teclado(event):
    pestana_activa = notebook.index(notebook.select())
    if pestana_activa == 0:
        copiar_fuente()
    elif pestana_activa == 1:
        copiar_cursor()
    elif pestana_activa == 2:
        copiar_color()

# ==========================================
# 2. CONFIGURACIÓN DE LA INTERFAZ
# ==========================================
root = tk.Tk()
root.title("Suite de Apoyo para Tkinter")
root.geometry("550x700")

# Contenedor de pestañas (Notebook)
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# ------------------------------------------
# PESTAÑA 1: FUENTES
# ------------------------------------------
tab_fuentes = tk.Frame(notebook)
notebook.add(tab_fuentes, text=" 🔤 Fuentes ")

frame_lista_f = tk.Frame(tab_fuentes)
frame_lista_f.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)

scroll_f = tk.Scrollbar(frame_lista_f)
scroll_f.pack(side=tk.RIGHT, fill=tk.Y)

lista_fuentes = tk.Listbox(frame_lista_f, yscrollcommand=scroll_f.set, font=("Arial", 11))
lista_fuentes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scroll_f.config(command=lista_fuentes.yview)

frame_prev_f = tk.LabelFrame(tab_fuentes, text=" Vista Previa ", padx=10, pady=10)
frame_prev_f.pack(padx=15, pady=15, fill=tk.X)

lbl_vista_fuente = tk.Label(frame_prev_f, text="AbcDeF 12345 !@#", font=("Arial", 24))
lbl_vista_fuente.pack(pady=10)

lbl_info_fuente = tk.Label(frame_prev_f, text="Selecciona una fuente arriba", font=("Arial", 10, "italic"), fg="gray")
lbl_info_fuente.pack(pady=5)

btn_copiar_fuente = tk.Button(frame_prev_f, text="📋 Copiar Nombre", font=("Arial", 10, "bold"), state=tk.DISABLED, command=copiar_fuente)
btn_copiar_fuente.pack(pady=5)

fuentes_unicas = sorted(set(families()))
for f in fuentes_unicas:
    if f and not f.startswith("@"):
        lista_fuentes.insert(tk.END, f)

lista_fuentes.bind("<<ListboxSelect>>", actualizar_fuente)

# ------------------------------------------
# PESTAÑA 2: CURSORES
# ------------------------------------------
tab_cursores = tk.Frame(notebook)
notebook.add(tab_cursores, text=" 🖱️ Cursores ")

frame_lista_cu = tk.Frame(tab_cursores)
frame_lista_cu.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)

scroll_cu = tk.Scrollbar(frame_lista_cu)
scroll_cu.pack(side=tk.RIGHT, fill=tk.Y)

lista_cursores = tk.Listbox(frame_lista_cu, yscrollcommand=scroll_cu.set, font=("Arial", 11))
lista_cursores.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scroll_cu.config(command=lista_cursores.yview)

frame_prev_cu = tk.LabelFrame(tab_cursores, text=" Área de Pruebas ", padx=10, pady=10)
frame_prev_cu.pack(padx=15, pady=15, fill=tk.X)

zona_pruebas_cursor = tk.Frame(frame_prev_cu, height=100, bd=2, relief=tk.GROOVE, bg="#f8f9fa")
zona_pruebas_cursor.pack(fill=tk.X, pady=10)
zona_pruebas_cursor.pack_propagate(False)

lbl_instruccion_cursor = tk.Label(zona_pruebas_cursor, text="Selecciona un cursor arriba", font=("Arial", 11), bg="#f8f9fa", fg="gray")
lbl_instruccion_cursor.pack(expand=True)

lbl_info_cursor = tk.Label(frame_prev_cu, text="Ningún cursor seleccionado", font=("Arial", 10, "italic"), fg="gray")
lbl_info_cursor.pack(pady=5)

btn_copiar_cursor = tk.Button(frame_prev_cu, text="📋 Copiar Nombre", font=("Arial", 10, "bold"), state=tk.DISABLED, command=copiar_cursor)
btn_copiar_cursor.pack(pady=5)

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
for c in cursores_estandar:
    lista_cursores.insert(tk.END, c)

lista_cursores.bind("<<ListboxSelect>>", actualizar_cursor)

# ------------------------------------------
# PESTAÑA 3: COLORES (¡Optimizada!)
# ------------------------------------------
tab_colores = tk.Frame(notebook)
notebook.add(tab_colores, text=" 🎨 Colores ")

frame_lista_co = tk.Frame(tab_colores)
frame_lista_co.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)

scroll_co = tk.Scrollbar(frame_lista_co)
scroll_co.pack(side=tk.RIGHT, fill=tk.Y)

lista_colores = tk.Listbox(frame_lista_co, yscrollcommand=scroll_co.set, font=("Arial", 11))
lista_colores.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scroll_co.config(command=lista_colores.yview)

frame_prev_co = tk.LabelFrame(tab_colores, text=" Vista Previa del Color ", padx=10, pady=10)
frame_prev_co.pack(padx=15, pady=15, fill=tk.X)

zona_pruebas_color = tk.Frame(frame_prev_co, height=100, bd=2, relief=tk.GROOVE, bg="#ffffff")
zona_pruebas_color.pack(fill=tk.X, pady=10)
zona_pruebas_color.pack_propagate(False)

lbl_muestra_color = tk.Label(zona_pruebas_color, text="Selecciona un color arriba", font=("Arial", 14, "bold"), bg="#ffffff", fg="gray")
lbl_muestra_color.pack(expand=True)

lbl_info_color = tk.Label(frame_prev_co, text="Ningún color seleccionado", font=("Arial", 10, "italic"), fg="gray")
lbl_info_color.pack(pady=5)

btn_copiar_color = tk.Button(frame_prev_co, text="📋 Copiar Nombre", font=("Arial", 10, "bold"), state=tk.DISABLED, command=copiar_color)
btn_copiar_color.pack(pady=5)

# OBTENER COLORES AUTOMÁTICAMENTE DEL SISTEMA
# Se filtran los que empiezan con "System" o tienen nombres internos complejos
colores_sistema = sorted([
    c for c in root.getrgb_names() 
    if not c.startswith("System") and " " not in c
])

for color in colores_sistema:
    lista_colores.insert(tk.END, color)

lista_colores.bind("<<ListboxSelect>>", actualizar_color)

# --- Configuración del Atajo Global ---
root.bind("<Control-c>", copiar_atajo_teclado)

# Iniciar aplicación
root.mainloop()
