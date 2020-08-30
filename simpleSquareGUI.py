import turtle

square= turtle.Turtle()

def squareFunc():
    square.forward(100)
    square.left(90)
    square.forward(100)
    square.left(90)
    square.forward(100)
    square.left(90)
    square.forward(100)

squareFunc()
square.forward(100)
squareFunc()
turtle.Screen()._root.mainloop()  