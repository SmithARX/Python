from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    screen = Screen()
    def __init__(self):
        super().__init__()
        #turn for up
        self.setheading(90)
        #Make the shape as turtle
        self.shape("turtle")
        #turn off the pen 
        self.penup()
        #goes to starting position
        self.goto(STARTING_POSITION)
    def go_up(self):
            self.forward(MOVE_DISTANCE)
    
    def go_down(self):
            if self.ycor()> -280:
                self.bk(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)


    

        
 