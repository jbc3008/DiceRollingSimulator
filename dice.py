import random

class Dice():
    """This class simulates a dice... probably"""
    
    def __init__(self):
        self.dice_sides = {
            1: '+---------+\n|         |\n|    o    |\n|         |\n+---------+',
            2: '+---------+\n|      o  |\n|         |\n|  o      |\n+---------+',
            3: '+---------+\n|    o    |\n|    o    |\n|    o    |\n+---------+',
            4: '+---------+\n|  o   o  |\n|         |\n|  o   o  |\n+---------+',
            5: '+---------+\n|  o   o  |\n|    o    |\n|  o   o  |\n+---------+',
            6: '+---------+\n|  o   o  |\n|  o   o  |\n|  o   o  |\n+---------+',
        }
        
        
    def dice_rolling(self):
        """Rolls the dice."""
        result = random.randint(1, 6)
        string = self.dice_sides[result]
        
        return (string)
