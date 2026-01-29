from FileToVideo import  youtubeToStream
import tkinter as tk
from tkinter import filedialog
import os

# Función para abrir el diálogo de selección de archivo
def seleccionar_archivo():
    archivo = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if archivo:
        archivo_seleccionado.set(archivo)
        label_archivo.config(text=f"Archivo: {archivo}")

def generar_evento():
    archivo = archivo_seleccionado.get()
    enlace = caja_enlace.get()
    opcion = opcion_var.get()
    directorio = os.getcwd()
    conversor = youtubeToStream()
    
    if enlace.strip():  # Si hay enlace ingresado
        print(f"Procesando enlace: {enlace}")
        print(f"Formato: {opcion}")
        print(f"Descargando en: {directorio}")
        if opcion == "mp3":
            conversor.descarga_mp3(enlace, directorio)
        else:
            conversor.descarga_mp4(enlace, directorio)
    elif archivo != "No se ha seleccionado archivo":  # Si hay archivo seleccionado
        print(f"Procesando archivo: {archivo}")
        print(f"Formato: {opcion}")
        print(f"Descargando en: {directorio}")
        if opcion == "mp3":
            conversor.procesar_archivo_mp3(archivo, directorio)
        else:
            conversor.procesar_archivo_mp4(archivo, directorio)
    else:
        print("Por favor selecciona un archivo o ingresa un enlace")






root = tk.Tk()
root.title("Convierte un video de youtube a mp3 o mp4")


frame_input = tk.Frame(root,bg="lightgray",bd=2, relief="sunken",width=150, height=150)
frame_input.title = "Entrada de datos ingresando un link o archivo"
frame_input.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

tk.Label(frame_input, text="Selecciona como deseas descargar tu archivo desde youtube").pack(padx=10, pady=10)

frame_input_link = tk.Frame(frame_input,bg="lightgray")
frame_input_link.pack(pady=10, expand=True)
tk.Label(frame_input_link, text="Procesar Link",bg="lightgray").pack(side=tk.LEFT, padx=10, pady=10)
caja_enlace = tk.Entry(frame_input_link, width=50)
caja_enlace.pack(side=tk.LEFT, padx=10, pady=10)

frame_input_archivo = tk.Frame(frame_input,bg="lightgray")
frame_input_archivo.pack(pady=10, expand=True)

tk.Label(frame_input_archivo, text="Procesar Archivo:",bg="lightgray").pack(side=tk.LEFT,padx=10, pady=10)
btn_archivo = tk.Button(frame_input_archivo, text="seleccione aqui su archivo", command=seleccionar_archivo)
btn_archivo.pack(side=tk.LEFT, padx=10, pady=10)

label_archivo = tk.Label(frame_input_archivo, text="No se ha seleccionado archivo", fg="blue")
label_archivo.pack(side=tk.LEFT, pady=10)

# Label para mostrar el directorio seleccionado
label_directorio = tk.Label(frame_input, text=f"Directorio de descarga: {os.getcwd()}", fg="green")
label_directorio.pack(pady=10)


label = tk.Label(root, text="Selecciona mp3 o mp4 para la descarga")
label.pack(pady=10)

frame_generar = tk.Frame(root,bg="lightgray",bd=2, relief="sunken",width=150, height=150)
frame_generar.title = "Generar descarga"
frame_generar.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=5, pady=5)

# Variable para guardar la ruta del archivo seleccionado
archivo_seleccionado = tk.StringVar(frame_generar)
archivo_seleccionado.set("Convierte un video de youtube a mp3 o mp4")

opcion_var = tk.StringVar(frame_generar)
opcion_var.set("mp3") # Valor por defecto

# Creación del menú de opciones
menu = tk.OptionMenu(frame_generar, opcion_var, "mp3", "mp4")
menu.pack(expand=True,padx=10,pady=10)

# Botón para confirmar
btn = tk.Button(frame_generar, text="Generar", command=generar_evento)
btn.pack(expand=True,padx=10,pady=10)

root.mainloop()