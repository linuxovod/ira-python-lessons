# SquaSpiral1.py - Рисование квадратной спирали бабабабабабабабабабабаба
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "pink"]
for x in range(200):
    t.pencolor(colors[x%5])  
    t.circle(x)
    t.left(72)
