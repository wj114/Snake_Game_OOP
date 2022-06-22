from turtle import Turtle

Alignment = "center"
Font = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())  # read the high scorer from "data.txt"
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()  # hide the turtle icon

    def update_score(self):
        self.clear()  # to clear the score writing to avoid overlap
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align=Alignment, font=Font)

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")  # write the high score for record
        self.score = 0
        self.update_score()

    # def game0ver(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", False, align=Alignment, font=Font)
