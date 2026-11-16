import os
from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 24, "normal")
DIRECTORY = os.path.dirname(__file__)
FILE_PATH = os.path.join(DIRECTORY, "data.txt")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open(FILE_PATH, mode="r") as data:
                content = data.read().strip()
                self.high_score = int(content) if content else 0
        except FileNotFoundError:
            self.high_score = 0
            with open(FILE_PATH, mode="w") as data:
                data.write("0")
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_screenboard()

    def update_screenboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE_PATH, mode="w") as data:
                data.write(f"{self.high_score}")
            
        self.score = 0
        self.update_screenboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_screenboard()
