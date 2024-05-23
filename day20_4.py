from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day20_5.txt") as data:
            self.high_score = int(data.read())
        # self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.display_score()
 
    def display_score(self): 
        self.clear()
        self.write(f"Score : {self.score} High score: {self.high_score}", align="center",
                   font=("Arial", 24, "normal"))

    def reset_(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day20_5.txt",mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.display_score() 


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game over...", align="center",
    #                font=("Arial", 24, "normal"))

    def increse_score(self):
        self.score += 1
        self.clear()
        self.display_score()
