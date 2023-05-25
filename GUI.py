import waveDiffraction
import tkinter as tk
from PIL import Image, ImageTk

canvas = None

root = tk.Tk()

mainFrame = tk.Frame(root, width=404, height=404)
mainFrame.grid(), mainFrame.grid_propagate(0)

LImage = tk.Label(mainFrame, image=ImageTk.PhotoImage(Image.fromarray(np.array(n3Img))))
LImage.grid(row=0, column=1)


LImage.config(image = img)
LImage.image = img

