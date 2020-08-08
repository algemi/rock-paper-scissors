import random

computer_wins = 0
player_wins = 0

print('')
print('Welcome to the game rock-paper-scissors.')
print('If you want to play press:')
print('1 for Rock')
print('2 for Paper')
print('3 for Scissors')

def User_Option():
    user_option = input('Choose option (1,2,3): ')
    if user_option in ['1', 'Rock', 'rock', 'R', 'r']:
        user_option = '1'
    elif user_option in ['2', 'Paper', 'paper', 'P', 'p']:
        user_option = '2'
    elif user_option in ['3', 'Scissors', 'scissor', 'S', 's']:
        user_option = '3'
    else:
        print('Invalid. Try again.')
        User_Option()
    return user_option

def Computer_Option():
    computer_option = random.randint(1,3)
    if computer_option == 1:
        computer_option = '1'
    elif computer_option == 2:
        computer_option = '2'
    elif computer_option == 3:
        computer_option = '3'
    return computer_option

while True:
    user_option = User_Option()
    computer_option = Computer_Option()

    if user_option == '1':
        if computer_option == '1':
            print('player: rock, computer: rock. You tied.')
        elif computer_option == '2':
            print('player: rock, computer: paper. You lose.')
            computer_wins += 1
        elif computer_option == '3':
            print('player: rock, computer: scissors. You win.')
            player_wins += 1

    elif user_option == '2':
        if computer_option == '1':
            print('player: paper, computer: rock. You win.')
            player_wins += 1
        elif computer_option == '2':
            print('player: paper, computer: paper. You tied.')
        elif computer_option == '3':
            print('player: paper, computer: scissors. You lose.')
            computer_wins += 1

    elif user_option == '3':
        if computer_option == '1':
            print('player: scissors, computer: rock. You lose.')
            computer_wins += 1
        elif computer_option == '2':
            print('player: scissors, computer: paper. You win.')
            player_wins += 1
        elif computer_option == '3':
            print('player: scissors, computer: scissors. You tied.')

    print('')
    print('player wins: ' + str(player_wins))
    print('computer wins: ' + str(computer_wins))
    print('')

    user_option = input('Play again? (yes/no) ')
    if user_option in ['yes', 'Yes', 'y', 'Y', '1', '2', '3', '']:
        pass
    elif user_option in ['No', 'no']:
        break
    else:
        break
