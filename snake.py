from turtle import Turtle

SPAWN_CO_ORDS = [(0, 0), (-20, 0), (-40, 0)]
STEP_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_size = []
        self.spawn_snake()
        self.head = self.snake_size[0]

    def spawn_snake(self):
        for count in SPAWN_CO_ORDS:
            self.add_block(count)

    def add_block(self, count):
        box = Turtle()
        box.shape("square")
        box.color("white")
        box.pu()
        box.goto(count)
        self.snake_size.append(box)

    def grow(self):
        self.add_block(self.snake_size[-1].position())
        # plus_one = Turtle()
        # plus_one.shape("square")
        # plus_one.color("white")
        # plus_one.pu()
        # self.snake_size.append(plus_one)

    def move(self, direction):
        for seg in range(len(self.snake_size) - 1, 0, -1):
            new_x = self.snake_size[seg - 1].xcor()
            new_y = self.snake_size[seg - 1].ycor()
            self.snake_size[seg].goto(new_x, new_y)
        self.snake_size[0].fd(STEP_SIZE)

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
