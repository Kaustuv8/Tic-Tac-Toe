import turtle as T
class Grid:
    def __init__(self):
        self.GridMaker = T.Turtle()
        self.MakeGrid()
    def MakeGrid(self):
        self.GridMaker.hideturtle()
        self.GridMaker.penup()
        self.GridMaker.pensize(width=10)
        self.GridMaker.pencolor("black")
        # Setting Direction
        self.GridMaker.setpos(-150, 50)
        # First Horizontal Line
        self.MakeStraightLine()
        # Setting the second horizontal line
        self.GridMaker.setpos(-150, -50)
        self.MakeStraightLine()
        self.GridMaker.right(90)
        # First Vertical Line
        self.GridMaker.setpos(-50, 150)
        self.MakeStraightLine()
        # Second Vertical Line
        self.GridMaker.setpos(50, 150)
        self.MakeStraightLine()
        self.GridMaker.setpos(300, 0)
    def MakeStraightLine(self):
        self.GridMaker.pendown()
        self.GridMaker.forward(300)
        self.GridMaker.penup()