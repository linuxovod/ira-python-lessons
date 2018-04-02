import turtle
t = turtle.Pen()
turtle.bgcolor("black")
# Вы можете задать от 2 до 6 граней - и получить крутые фигуры
sides = 4
colors = ["red", "yellow", "blue", "purple", "green", "pink"]
for x in range(360):
    t.pencolor(colors[x%sides])  
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
