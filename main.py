# Practicando redio buttons

import tkinter as tk
from tkinter import *


def albumFotos():
    if seleccion.get() == 1:
        mensaje = "Acá podrás ver las fotos de tu viaje a Brasil."
        
    if seleccion.get() == 2:
        mensaje = 'Acá podrás ver todas las fotos de tu viaje a Chile.'
        
    if seleccion.get() == 3:
        mensaje = "Acá podrás ver las fotos de tu viaje a Bariloche."
        
    if seleccion.get() == 4:
        mensaje = 'Acá podrás ver las fotos de tu viaje a Venezuela.'
        
    lblMensaje.config(text = mensaje)
    
def reset():
    seleccion.set(None)
    lblMensaje.config(text='Selecciona otro lugar')
    

ventana = tk.Tk()
seleccion = tk.IntVar()

rbnBrasil = tk.Radiobutton(ventana, text = 'Brasil', variable = seleccion, value = 1 ,command = albumFotos).pack(anchor = tk.W)

rbnChile = tk.Radiobutton(ventana, text = 'Chile', variable = seleccion, value = 2 ,command = albumFotos).pack(anchor = tk.W)

rbnBariloche = tk.Radiobutton(ventana, text = 'Bariloche', variable = seleccion, value = 3 ,command = albumFotos).pack(anchor = tk.W)

rbnVenezuela = tk.Radiobutton(ventana, text = 'Venezuela', variable = seleccion, value = 4 ,command = albumFotos).pack(anchor = tk.W)

lblMensaje = tk.Label(ventana)
lblMensaje.pack()
Button(ventana, text="Reiniciar", command=reset).pack()
ventana.mainloop()
    