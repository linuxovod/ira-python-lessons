# SquaSpiral1.py - Рисование квадратной спирали бабабабабабабабабабабаба
import turtle
t = turtle.Pen()
colors = ["red", "yellow", "blue", "green", "pink"]
for x in range(100):
    t.pencolor(colors[x%5])  
    t.forward(x)
    t.left(72)
