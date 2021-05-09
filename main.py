from dice import Dice

dice = Dice()
flag = True
prompt = 'Do you want to roll the dice? (Yes/No)\n'

while flag:
    
    a = input(prompt)
    
    if a.lower() == 'y' or a.lower() == 'yes':
        print (dice.dice_rolling())
    elif a.lower() == 'n' or a.lower() == 'no':
        flag = False
    else:
        print ('Sorry, I didn\'t understand that answer.')

print ('See you later!')
