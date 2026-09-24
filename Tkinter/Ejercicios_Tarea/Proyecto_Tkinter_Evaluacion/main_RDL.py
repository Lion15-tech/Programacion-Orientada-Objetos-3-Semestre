import tkinter as tk
from tkinter import messagebox
import preguntas

class Evaluacion:
    def __init__(self, ventana):
        #Creamos la ventana
        self.ventana = ventana
        self.ventana.title("Evaluación Python") 
        self.ventana.geometry("300x300")

        #Pedimos el nombre
        tk.Label(ventana,
                text="Nombre: ").pack(pady=5)
        self.entrada_nombre = tk.Entry(ventana)
        self.entrada_nombre.pack()

        #Botón
        self.boton_ingresar = tk.Button(ventana, 
                                        text="Ingresar",
                                        command=self.ingresar
                                        )
        self.boton_ingresar.pack(pady=5) 

    def ingresar(self):
        #Vemos que si coloque un nombre
        nombre = self.entrada_nombre.get()
        if nombre.strip() == "":
            messagebox.showwarning("Error", "Debes colocar tu nombre para poder ingresar")
            return
        
        #Guardamos el nombre y calificación (temporal) en el diccionario
        preguntas.resultados_alumnos[nombre] = 0

        #Este nos permite ocultar la ventana
        self.ventana.withdraw()

        self.abrir_ventana_evaluacion(nombre)

    def abrir_ventana_evaluacion(self, nombre):
        #Creamos la ventana
        ventana_evaluacion = tk.Toplevel(ventana_root)
        ventana_evaluacion.title("Evaluación de Python")
        ventana_evaluacion.geometry("400x700")

        #Esto nos permite hacer que si el usuario cierra el cuestionario, el programa 
        #Se cierre por completo también
        ventana_evaluacion.protocol("WM_DELETE_WINDOW", ventana_root.destroy)

        tk.Label(ventana_evaluacion, 
                text=f"Evaluación Python").pack(anchor="n", pady=10)
        tk.Label(ventana_evaluacion,
                text=f"Alumno: {nombre}").pack(anchor="nw", pady=10, padx=10)

        #Hacemos una lista para guardar las respuestas que de
        respuestas_alumno = []

        #Imprimimos las preguntas enumerandolas
        for num_pregunta, pregunta_hacer in enumerate(preguntas.preguntas_evaluacion): 
            tk.Label(ventana_evaluacion,  # enumerate empieza en 0
                    text=f"{num_pregunta+1}.- {pregunta_hacer['pregunta']}").pack(anchor="w", 
                                                                                pady=5, padx=15)

            #Inicializamos una variable que usa Tkinter para guardar las respuestas
            respuesta_dada = tk.StringVar(value="")
            #Agregamos la respuesta a la lista
            respuestas_alumno.append(respuesta_dada)

            for opcion in pregunta_hacer["opciones"]:
                tk.Radiobutton(ventana_evaluacion,
                            text=opcion,
                            variable=respuesta_dada,
                            value=opcion).pack(anchor="w", padx=35)


    def enviar_respuestas(self):
        for respuesta in self.respuestas_alumno:
            if respuesta.get() == "":
                messagebox.showwarning("Incompleto", "Debes contestar todas las preguntas antes de enviarlo")
                return

        aciertos = 0
        total_preguntas = len(preguntas.preguntas_evaluacion)
        for pregunta, Respuesta in enumerate(self.respuestas_alumno):
            respuesta_usuario = Respuesta.get()
            respuesta_correcta = preguntas.preguntas_evaluacion[pregunta]["respuesta"]
            if respuesta_usuario == respuesta_correcta:
                aciertos = aciertos + 1

        promedio = (aciertos/total_preguntas) * 10

        preguntas.resultados_alumnos
#-----------------------------------------------
#-----------------------------------------------
#Ejecutamos el código
ventana_root = tk.Tk()
app = Evaluacion(ventana_root)

ventana_root.mainloop()