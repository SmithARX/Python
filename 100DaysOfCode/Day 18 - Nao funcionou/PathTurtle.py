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
tony.shape("turtle")
tony.pensize(10)
colours = ["CornflowerBlue", "DarkOrchid", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "Red"]
angles = [0, 90, 180, 270]
tony.speed(10)
screen.colormode(255)


for _ in range(100):
    tony.color(random_color())   
    tony.setheading(random.choice(angles))
    tony.forward(30)
    
screen.exitonclick()
