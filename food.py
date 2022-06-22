from turtle import Turtle
import random


class Food(Turtle):  # inheritance

    def __init__(self):
        super().__init__()  # inherit all the attributes and methods from Turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # make the size smaller
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
