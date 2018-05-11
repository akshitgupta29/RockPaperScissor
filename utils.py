def validate (choice):
    if choice > 3 or choice < 0:
        return False
    return True

def print_hands (hand, name = 'Guest'):
    hands = ['Rock', 'Paper', 'Scissors']
    print (name  +' picked '+hands[hand])

def judge (player, computer):
    if player == computer:
        return 'Draw'
    elif player == 0 and computer == 1:
        return 'Lose'
    elif player == 1 and computer == 2:
        return 'Lose'
    elif player == 2 and computer == 0:
        return 'Lose'
    else:
        return 'Win'

def input_user_name():
    player_name = input ('Enter your name: ')
    return player_name

def input_user_name_1(count):
    player_name = input ('Enter your name for the '+str(count) + ' time: ') 
    return player_name
    
def name_validate(name):
    if name == '' or name == ' ':
        return True
    else:
        return False
