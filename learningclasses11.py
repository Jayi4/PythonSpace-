#!/usr/bash/python3

class Mariokartplayer:
    def __init__ (self, name, karttype):
        self.name = name
        self.karttype = karttype
        self.score = 0
        self.item = None

# this is the display when someone tires to the print the object
    def __str__(self):
        return self.name

    def scorechange(self, condition):
        if condition == "coin":
            self.score += 10
        elif condition == "finishline":
            self.score += 100
        elif condition == "pushopponent":
            self.score += 25
        else:
            self.score += 5

    def main():
        print("Learning about classes with Mario Kart")
        yoshi = Mariokartplayer("Yoshi", "50cc")

        print(player1)  ## this reveals the def __str__:
        print(player1.name)
        print(player1.karttype)
        print(player1.score)
        print(player1.item)

        ## in our game... player1 just touched a coin
        player1.scorechange("coin")
        print(player1.score)
        palyer1.scorechange("finishline")
        print(player1.score)
        player1.scorechange ("pollywollydoodle")
        print(player1.score)
        
        ## in our game... player1 just added to their score
        player1.score += 100
        print(player1.score)
        player1.score += 100
        print(player1.score)

#class: data template created for clarity in tracking copious amounts of data
#init: initializer

