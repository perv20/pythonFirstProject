import random

choices = ['rock', 'paper', 'scissor']
computer_choice = random.choice(choices)
user_choice = input("enter user choice [rock/paper/scissor]= ")
if user_choice == computer_choice:
    print('match tie!')
elif user_choice == 'rock':
    if computer_choice == 'paper':
        print('computer won')
    else:
        print('user won')

  elif user_choice == 'rock':
    if computer_choice == 'paper':
        print('computer won')
    else:
        print('user won')
elif user_choice == 'rock':
    if computer_choice == 'paper':
        print('computer won')
    else:
        print('user won')
