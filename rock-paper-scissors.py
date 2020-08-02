import random

print('')
print('Welcome to the game rock-paper-scissors.')
print('If you want to play press:')
print('1 for rock')
print('2 for paper')
print('3 for scissors')

def User_Option():
    user_option = input('Choose your number (1,2,3): ')
    if user_option in ['1']:
        user_option = '1'
    elif user_option in ['2']:
        user_option = '2'
    elif user_option in ['3']:
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
        elif computer_option == '3':
            print('player: rock, computer: scissors. You win.')


    elif user_option == '2':
        if computer_option == '1':
            print('player: paper, computer: rock. You win.')
        elif computer_option == '2':
            print('player: paper, computer: paper. You tied.')
        elif computer_option == '3':
            print('player: paper, computer: scissors. You lose.')


    elif user_option == '3':
        if computer_option == '1':
            print('player: scissors, computer: rock. You lose.')
        elif computer_option == '2':
            print('player: scissors, computer: paper. You win.')
        elif computer_option == '3':
            print('player: scissors, computer: scissors. You tied.')

#user_choice = input('Play again? [y/n]')
#if user_choice in ['y']:
#    pass
#elif user_choice in ['n']:
#    exit()
