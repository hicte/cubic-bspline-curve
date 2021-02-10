import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from scipy import interpolate

points = []


def bspl_plot():
    global points
    controller = np.array(points)

    x = controller[:, 0]
    y = controller[:, 1]

    x = np.append(x, [x[0]])
    y = np.append(y, [y[0]])

    l = len(x)

    t = np.linspace(0, 1, l-2, endpoint=True)
    t = np.append([0, 0, 0], t)
    t = np.append(t, [1, 1, 1])

    tck = [t, [x, y], 3]
    u3 = np.linspace(0, 1, (max(l*2, 70)), endpoint=True)
    out = interpolate.splev(u3, tck)

    plt.plot(x, y, 'k--', label='control', marker='o', markerfacecolor='red')
    plt.plot(out[0], out[1], 'b', linewidth=2.0, label='curve')

    plt.legend(loc='best')
    plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
    plt.title('CUBIC BSPLINE CURVE')

    plt.show()


def make_point(x, y):
    global points
    points.append((x, 512 - y))

    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red')


def click(event):
    make_point(event.x, event.y)


root = tk.Tk()
root.title('CUBIC BSPLINE CURVE')

message = tk.Message(root, width=512)
message.config(text='Click on screen and choose desired points.')
message.pack()

canvas = tk.Canvas(root, width=512, height=512, bg='white')
canvas.pack()
canvas.bind('<ButtonRelease-1>', click)

button = tk.Button(root, text='Draw', width=20, command=bspl_plot)
button.config(bg='black', fg='white')
button.config(activebackground='red', activeforeground='white')
button.pack()

root.mainloop()
