from turtle import Turtle as t
from turtle import Screen as sc
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
    
tony = t()
screen = sc()


tony.speed("fastest")
screen.colormode(255)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tony.color(random_color())
        tony.circle(100)
        tony.setheading(tony.heading() + size_of_gap)
        
draw_spirograph(5)

screen.exitonclick()
