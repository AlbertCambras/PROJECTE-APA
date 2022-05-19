from tkinter import *
from PIL import ImageTk ,Image
import numpy as np

root = Tk()

# declarem imatge
img = ImageTk.PhotoImage(Image.open("flor.jpg"))

# hem de ficar la imatge en algun container
etiqueta = Label(image = img)

# la mostrem
etiqueta.pack()

px = img.load()

root.mainloop() # bucle del programa
