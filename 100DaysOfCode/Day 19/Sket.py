from turtle import Turtle, Screen

screen = Screen()
tom = Turtle()
def moveForward():
    tom.forward(10)
def righSide():
    tom.right(10)
def leftSide():
    tom.left(10)
def backWard():
    tom.backward(10)
def Clear():
    tom.clear()    


screen.listen()
screen.onkeypress(moveForward, "w")
screen.onkeypress(leftSide, "a")
screen.onkeypress(backWard, "s")
screen.onkeypress(righSide, "d")
screen.onkeypress(Clear, "x")

screen.exitonclick()
