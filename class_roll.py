from diceroller import DiceRoller

result = []
test = DiceRoller(4,6,8,result)
test.roll()
print(test.roll())
test.roll_many()
print(result)
        
