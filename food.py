from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.screen.register_shape("bitcoin.gif")
        self.shape("bitcoin.gif")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
