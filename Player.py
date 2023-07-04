import turtle as T

Check = 1

Cells = {"Cell--100.0100.0" : [False, False , -100.0,100.0],
         "Cell-0.0100.0" : [False, False, 0.0,100.0],
         "Cell-100.0100.0" : [False, False, 100.0, 100.0],
         "Cell--100.00.0" : [False, False, -100.0, 0,0],
         "Cell-0.00.0" : [False, False, 0.0, 0.0],
         "Cell-100.00.0" : [False, False, 100.0, 0.0],
         "Cell--100.0-100.0" : [False, False, -100.0, -100.0],
         "Cell-0.0-100.0" : [False, False, 0.0, -100.0],
         "Cell-100.0-100.0" : [False, False, 100.0, -100.0]}

Round_Count = 1

class Player:
    def __init__(self):

        self.IsGameOn = True
        self.PlayerMarker = T.Turtle()
        self.Scoreboard = T.Turtle()
        self.PlayerMarker.showturtle()
        self.PlayerMarker.shape("turtle")
        self.PlayerMarker.resizemode(rmode='user')
        self.PlayerMarker.shapesize(stretch_len=2, stretch_wid=2)
        self.PlayerMarker.penup()
        self.PlayerMarker.pensize(2)
        self.PlayerOneScore = 0
        self.PlayerTwoScore = 0
        self.Scoreboard.hideturtle()
        self.Scoreboard.penup()
        self.Scoreboard.setpos(0, 200)
        self.Scoreboard.write(arg=f"Player 1(Cross) : {self.PlayerOneScore}\nPlayer 2(Circle) : {self.PlayerTwoScore}", align="center", font=('Arial', 16, 'normal'))
        self.Scoreboard.setpos(0,250)
        self.Scoreboard.write(arg=f"Round : {Round_Count}", align="center", font=('Arial', 16, 'normal'))


    def MoveUp(self):

        if self.PlayerMarker.ycor() != 100 :
            self.PlayerMarker.setpos(self.PlayerMarker.xcor(), self.PlayerMarker.ycor() + 100)

    def MoveDown(self):

        if self.PlayerMarker.ycor() != -100:
            self.PlayerMarker.setpos(self.PlayerMarker.xcor(), self.PlayerMarker.ycor() - 100)

    def MoveRight(self):

        if self.PlayerMarker.xcor() != 100:
            self.PlayerMarker.setpos(self.PlayerMarker.xcor() + 100, self.PlayerMarker.ycor())


    def MoveLeft(self):

        if self.PlayerMarker.xcor() != -100:
            self.PlayerMarker.setpos(self.PlayerMarker.xcor() - 100, self.PlayerMarker.ycor())


    def MakeCircle(self):
        global Cells
        CurrentCoordinates = [self.PlayerMarker.xcor(), self.PlayerMarker.ycor()]
        try:
            if Cells[f"Cell-{CurrentCoordinates[0]}{CurrentCoordinates[1]}"][0] == False and Cells[f"Cell-{CurrentCoordinates[0]}{CurrentCoordinates[1]}"][1] == False:
                self.PlayerMarker.hideturtle()
                self.PlayerMarker.setpos(CurrentCoordinates[0], CurrentCoordinates[1] - 25)
                self.PlayerMarker.pendown()
                self.PlayerMarker.circle(25)
                self.PlayerMarker.penup()
                self.PlayerMarker.setpos(CurrentCoordinates[0], CurrentCoordinates[1])
                Cells[f"Cell-{CurrentCoordinates[0]}{CurrentCoordinates[1]}"][1] = True
                self.PlayerMarker.showturtle()
        except KeyError:
            print("Shape made while not on designated coordinate.")

    def MakeCross(self):
        global Cells
        CurrentCoordinates = [float(self.PlayerMarker.xcor()), float(self.PlayerMarker.ycor())]
        try:
            if Cells[f"Cell-{CurrentCoordinates[0]}{CurrentCoordinates[1]}"][0] == False and Cells[f"Cell-{CurrentCoordinates[0]}{CurrentCoordinates[1]}"][1] == False:
                self.PlayerMarker.hideturtle()
                self.PlayerMarker.setpos(CurrentCoordinates[0] - 25, CurrentCoordinates[1] - 25)
                self.PlayerMarker.pendown()
                self.PlayerMarker.setpos(CurrentCoordinates[0] + 25, CurrentCoordinates[1] + 25)
                self.PlayerMarker.penup()
                self.PlayerMarker.setpos(CurrentCoordinates[0] + 25, CurrentCoordinates[1] - 25)
                self.PlayerMarker.pendown()
                self.PlayerMarker.setpos(CurrentCoordinates[0] - 25, CurrentCoordinates[1] + 25)
                self.PlayerMarker.penup()
                self.PlayerMarker.setpos(CurrentCoordinates[0], CurrentCoordinates[1])
                self.PlayerMarker.showturtle()
                Cells[f"Cell-{CurrentCoordinates[0]}{CurrentCoordinates[1]}"][0] = True
        except KeyError:
            print("Shape made while not on designated coordinate.")



    def MakeShape(self):
        global Check
        if self.IsGameOn:
            if Check == 1:
                self.MakeCross()
                Check *= -1
            else:
                self.MakeCircle()
                Check *= -1

            self.VerticalityCheck()
            self.HorizontalCheck()
            self.DiagonalCheck()
            self.DrawCondition()

    def VerticalityCheck(self):
        Values = list(Cells.keys())
        for i in range(0,3):
            StartingCord = [Cells[Values[i]][2], Cells[Values[i]][3]]
            CheckCross = 0
            CheckCircle = 0
            for j in Values[i::3]:
                if Cells[j][0] == True and CheckCircle == 0:
                    CheckCross+=1
                elif  Cells[j][1] == True and CheckCross == 0:
                    CheckCircle+=1
                else:
                    break
            if CheckCross == 3:
                self.FinalVerticalLine(StartingCord[0], StartingCord[1])
                if(Round_Count%2 == 0):
                    self.PlayerOneScore+=1
                else:
                    self.PlayerTwoScore+=1
                self.Write()

            if CheckCircle == 3:
                self.FinalVerticalLine(StartingCord[0], StartingCord[1])
                if (Round_Count % 2 != 0):
                    self.PlayerOneScore += 1
                else:
                    self.PlayerTwoScore += 1
                self.Write()


    def HorizontalCheck(self):
        Values = list(Cells.keys())
        for i in range(0, 7, 3):
            StartingCord = [Cells[Values[i]][2], Cells[Values[i]][3]]
            CheckCross = 0
            CheckCircle = 0
            for j in Values[i:i+3]:
                if Cells[j][0] == True and CheckCircle == 0:
                    CheckCross += 1
                elif Cells[j][1] == True and CheckCross == 0:
                    CheckCircle += 1
                else:
                    break
            if CheckCross == 3:
                self.FinalHorizontalLine(StartingCord[0], StartingCord[1])
                if (Round_Count % 2 == 0):
                    self.PlayerOneScore += 1
                else:
                    self.PlayerTwoScore += 1
                self.Write()
            if CheckCircle == 3:
                self.FinalHorizontalLine(StartingCord[0], StartingCord[1])
                if (Round_Count % 2 != 0):
                    self.PlayerOneScore += 1
                else:
                    self.PlayerTwoScore += 1
                self.Write()

    def DiagonalCheck(self):
        Values = list(Cells.keys())
        for i in range(0, 3, 2):
            StartingCord = [Cells[Values[i]][2], Cells[Values[i]][3]]
            CheckCross = 0
            CheckCircle = 0
            if i == 0:
                for j in Values[i::4]:
                    if Cells[j][0] == True and CheckCircle == 0:
                        CheckCross += 1
                    elif Cells[j][1] == True and CheckCross == 0:
                        CheckCircle += 1
                    else:
                        break
            if i == 2:
                for j in Values[i:7:2]:
                    if Cells[j][0] == True and CheckCircle == 0:
                        CheckCross += 1
                    elif Cells[j][1] == True and CheckCross == 0:
                        CheckCircle += 1
                    else:
                        break
            if CheckCross == 3:
                self.FinalDiagonalLine(StartingCord[0], StartingCord[1])
                if (Round_Count % 2 == 0):
                    self.PlayerOneScore += 1
                else:
                    self.PlayerTwoScore += 1
                self.Write()

            if CheckCircle == 3:
                self.FinalDiagonalLine(StartingCord[0], StartingCord[1])
                if (Round_Count % 2 != 0):
                    self.PlayerOneScore += 1
                else:
                    self.PlayerTwoScore += 1
                self.Write()



    def FinalVerticalLine(self, Xcord, Ycord):
        self.PlayerMarker.color("red")
        self.PlayerMarker.hideturtle()
        self.PlayerMarker.width(width = 5)
        self.PlayerMarker.setpos(Xcord,Ycord)
        self.PlayerMarker.pendown()
        self.PlayerMarker.setpos(Xcord,Ycord*-1)
        self.PlayerMarker.color("black")
        self.DisablePlayer()



    def FinalHorizontalLine(self, Xcord, Ycord):
        self.PlayerMarker.color("red")
        self.PlayerMarker.hideturtle()
        self.PlayerMarker.width(width=5)
        self.PlayerMarker.setpos(Xcord,Ycord)
        self.PlayerMarker.pendown()
        self.PlayerMarker.setpos(Xcord*-1,Ycord)
        self.PlayerMarker.color("black")
        self.DisablePlayer()

    def FinalDiagonalLine(self, Xcord, Ycord):
        self.PlayerMarker.color("red")
        self.PlayerMarker.hideturtle()
        self.PlayerMarker.width(width=5)
        self.PlayerMarker.setpos(Xcord, Ycord)
        self.PlayerMarker.pendown()
        self.PlayerMarker.setpos(Xcord * -1, Ycord *-1)
        self.PlayerMarker.color("black")
        self.DisablePlayer()


    def DrawCondition(self):
        Flag = 0
        for i in Cells.values():
            if True in i:
                Flag+=1
        if Flag == 9:
            self.Write()
            self.DisablePlayer()


    def CellsReset(self):
        global Cells
        Cells = {"Cell--100.0100.0": [False, False, -100.0, 100.0],
                 "Cell-0.0100.0": [False, False, 0.0, 100.0],
                 "Cell-100.0100.0": [False, False, 100.0, 100.0],
                 "Cell--100.00.0": [False, False, -100.0, 0, 0],
                 "Cell-0.00.0": [False, False, 0.0, 0.0],
                 "Cell-100.00.0": [False, False, 100.0, 0.0],
                 "Cell--100.0-100.0": [False, False, -100.0, -100.0],
                 "Cell-0.0-100.0": [False, False, 0.0, -100.0],
                 "Cell-100.0-100.0": [False, False, 100.0, -100.0]}
        self.PlayerMarker.clear()


    def DisablePlayer(self):
        global Round_Count
        self.IsGameOn = False
        self.PlayerMarker.hideturtle()
        self.PlayerMarker.penup()
        Round_Count += 1


    def EnablePlayer(self):
        self.IsGameOn = True
        self.PlayerMarker.setpos(0, 0)
        self.PlayerMarker.pensize(width=2)
        self.PlayerMarker.showturtle()

    def Write(self):
        self.Scoreboard.setpos(0, 175)
        self.Scoreboard.write(arg="Press R to start a new round",
                              align="center",
                              font=("Arial", 8, "normal"))

    def NewRound(self):
        global Check
        self.Scoreboard.clear()
        self.Scoreboard.setpos(0, 200)
        if (Round_Count % 2 != 0):
            self.Scoreboard.write(arg=f"Player 1 (Cross) : {self.PlayerOneScore}\nPlayer 2 (Circle) : {self.PlayerTwoScore}",
                              align="center",
                              font=('Arial', 16, 'normal'))
        else:
            self.Scoreboard.write(
                arg=f"Player 1 (Circle) : {self.PlayerOneScore}\nPlayer 2 (Cross) : {self.PlayerTwoScore}",
                align="center",
                font=('Arial', 16, 'normal'))

        self.Scoreboard.setpos(0, 250)
        self.Scoreboard.write(arg=f"Round : {Round_Count}",
                              align="center",
                              font=('Arial', 16, 'normal'))
        if not self.IsGameOn:
            Check = 1
            self.CellsReset()
            self.EnablePlayer()