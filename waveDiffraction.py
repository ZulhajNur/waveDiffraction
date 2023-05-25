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

slit = 40
if slit%2 == 0:
    slitu = int(slit/2)
else:
    slitu = int(slit/2 + 1)
slitd = int(-slit/2)

for i in range(slitd, slitu):
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

ani = animation.FuncAnimation(fig, updateFig, frames=range(0, 200), interval=0.1, repeat=True)

plt.show()
