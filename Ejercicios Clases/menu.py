#Esta es una librería que sirve para realizar importaciones dínamicas
import importlib
#O sea me va a evitar poner 31 imports y 31 if/elif manualmente según la IA

num_ejercicio = input("Elige un ejercicio que quieras abrir: ").strip()

#Intenta abir los archivos
try:
    #Carga el archivo que escogiste
    abrir_archivo = importlib.import_module(f"ejercicio_{num_ejercicio}")

    #Busca la función que esta dentro del archivo, donde se supone que estan los ejercicios
    funcion_ejercicio = getattr(abrir_archivo, f"ejercicio{num_ejercicio}")

    #Llama y ejecuta el ejercicio
    funcion_ejercicio()

except ModuleNotFoundError:
    print(f"El archivo {num_ejercicio} no existe")
except ValueError:
    print(f"No se encontró la función del ejercicio {num_ejercicio}")