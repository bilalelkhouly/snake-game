from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        square = Turtle(shape="square")
        square.penup()
        square.color("white")
        square.goto(position)
        self.squares.append(square)

    def extend(self):
        self.add_segment(self.squares[-1].position())

    def move(self):
        for index in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[index - 1].xcor()
            new_y = self.squares[index - 1].ycor()
            self.squares[index].goto(new_x, new_y)
        self.squares[0].forward(MOVE_DISTANCE)

    def reset_snake(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
