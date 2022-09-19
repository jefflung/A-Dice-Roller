import random

class DiceRoller:
    num_of_dice = 0
    roll_sum = 0
    newList = []
    def  __init__(self, num_of_dice, roll_sum, n, newList):
        self.num_of_dice = num_of_dice
        self.roll_sum = roll_sum
        self.n = n
        self.newList = newList
    def roll(self):
        
        for x in range(self.num_of_dice):
            self.roll_sum += random.randint(1,6)
        return self.roll_sum
    def roll_many(self):
        
        for y in range(self.n):
            self.newList.append(self.roll())
        return self.newList
