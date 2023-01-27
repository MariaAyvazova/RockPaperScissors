import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

user_input = input('Choose [r]ock, [p]aper or [s]cissors: ')

if user_input == 'r':
    user_input = rock
elif user_input == 'p':
    user_input = paper
elif user_input == 's':
    user_input = scissors
else:
    raise SystemExit('Invalid input! Try again....')

computer_random_number = random.randint(1, 3)

computer_input = ''

if computer_random_number == 1:
    computer_input = rock
elif computer_random_number == 2:
    computer_input = paper
elif computer_random_number == 3:
    computer_input = scissors

if (user_input == rock and computer_input == scissors) \
        or (user_input == paper and computer_input == rock) or (user_input == scissors and computer_input == paper):
    print('You win!')
elif user_input == computer_input:
    print('Draw!')
else:
    print('You lose!')