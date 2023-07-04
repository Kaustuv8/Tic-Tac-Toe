import turtle as T
from Grid import Grid
from Player import Player
# Setting up the screen

Screen = T.Screen()
Screen.setup(width=350, height=600)

NewGrid = Grid()

Play = Player()
Screen.listen()
Screen.onkey(Play.MoveUp, "w")
Screen.onkey(Play.MoveDown, "s")
Screen.onkey(Play.MoveRight, "d")
Screen.onkey(Play.MoveLeft, "a")
Screen.onkey(Play.MakeShape, "e")
Screen.onkey(Play.NewRound, "r")
Screen.exitonclick()
