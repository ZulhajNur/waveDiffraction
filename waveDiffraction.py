import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import multiprocessing as mp
import tkinter as tk
from PIL import Image, ImageTk
    
def f(x, w=1, t=0):
    y = np.sin(k*x-w*t)
    return y

def rad(x, y, c):
    y = np.sqrt((x-c[0])**2+(y-c[1])**2)
    return int(y)

def plotWave(r):
    global arr
    
    arrPlot = np.zeros((res[0], res[1]))
    c       = int(len(arrPlot[0])/2 + r), int(len(arrPlot)/2)
    
    for i in range(0, len(arrPlot[0])):
        for j in range(int(len(arrPlot[0])/2), len(arrPlot)):
            arrPlot[i, j] = f(rad(i, j, c))

    arr += arrPlot

def updateFig(n):
    line.set_ydata(arr[:,200+n])

fig, ax = plt.subplots()

k = 0.8

res  = 400, 400

arr = np.zeros((res[0], res[1]))

for i in range(-20, 20):
    plotWave(i)

### Straight Wave Section
##for i in range(0, len(arr)):
##    for j in range(0, int(len(arr[0])/2)):
##        arr[i, j] = f(j)

##ratio = 1
##plt.text(0, -10, '1 pixel : {} mm'.format(ratio))
##plt.imshow(arr, cmap='gray')


line, = ax.plot(arr[:, 200])
ax.set_ylim(np.min(arr), np.max(arr))

ani = animation.FuncAnimation(fig, updateFig, interval=0.1)
plt.show()



##x = []
##
##for i in range(0, 400):
##    x.append(i)

##plt.plot(x, arr[:, 400-1])
##plt.show()


##n3Img = (arr1/np.max(arr1))*255

##canvas = None
##
##root = tk.Tk()

##mainFrame = tk.Frame(root, width=404, height=404)
##mainFrame.grid(), mainFrame.grid_propagate(0)
##
##LImage = tk.Label(mainFrame, image=ImageTk.PhotoImage(Image.fromarray(np.array(n3Img))))
##LImage.grid(row=0, column=1)


##LImage.config(image = img)
##LImage.image = img

