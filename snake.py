from turtle import Turtle

# constants
starting_position = [(0, 0), (-20, 0), (-40, 0)]
color = "white"
shape = 'square'
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # create snake function
    def create_snake(self):
        for i in starting_position:
            self.add_segment(i)

    def add_segment(self, i):
        new_segment = Turtle()
        new_segment.shape(shape)
        new_segment.color(color)
        new_segment.penup()
        new_segment.goto(i)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())  # hold the position of last segment

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            """This for loop, in order to move as one (not piece by piece),
            we loop through the segments in reverse order so that it won't "break"
            when we want to turn left or right of our snake body.

            We move the last segment, to the position of second to last segment, and so on.
            In simple, we want the tail follow the head
            """
            new_x_position = self.segments[segment_number - 1].xcor()
            new_y_position = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x_position, new_y_position)
        self.head.forward(20)

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

    def reset_snakeBody(self):
        for each_segment in self.segments:
            each_segment.goto(2000, 2000)  # move the previous snake out of the screen befere reset it,
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]  # reinitialise the snake
