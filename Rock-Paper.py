import sys
import random
import utils
#from utils import validate
print ('Welcome to the game of Rock, Paper, Scissors')
#print('Enter your name')
player_name = input ('Enter your name ')
other_player_name = input('Enter the other player name (optional)')
print ('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_choice = int (input ('Enter your choice '))
if utils.validate(player_choice):
    #print ('into the functions')
    
    computer_hand = random.randint (0,2)
    #print(random.randint(0,2))
    utils.print_hands(player_choice, player_name)
    if other_player_name == '':
        utils.print_hands (computer_hand)
    else:
        utils.print_hands(computer_hand,  other_player_name)

    #print (computer_hand)   
    print (utils.judge (player_choice, computer_hand))
else:
    print('Enter a valid choice')

