from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):

        self.list_of_turtles = []
        self.create_snake()
        self.head = self.list_of_turtles[0]

    def create_snake(self):
        for i in STARTING_POS:
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(i)
            self.list_of_turtles.append(new_turtle)

    def move(self):
        for seg in range(len(self.list_of_turtles) - 1, 0, -1):  # blocks to copy previous block
            new_x = self.list_of_turtles[seg - 1].xcor()
            new_y = self.list_of_turtles[seg - 1].ycor()
            self.list_of_turtles[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)