from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.color("white")
        self.respawn()

    def respawn(self):
        x_coord = random.randint(-280, 280)
        y_coord = random.randint(-280, 280)
        self.goto(x_coord, y_coord)
