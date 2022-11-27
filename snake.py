import turtle as t
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
ANGLES = [90, 270, 0, 180]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = t.Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != ANGLES[1]:
            self.head.setheading(ANGLES[0])

    def down(self):
        if self.head.heading() != ANGLES[0]:
            self.head.setheading(ANGLES[1])

    def right(self):
        if self.head.heading() != ANGLES[3]:
            self.head.setheading(ANGLES[2])

    def left(self):
        if self.head.heading() != ANGLES[2]:
            self.head.setheading(ANGLES[3])
