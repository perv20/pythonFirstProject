import random

num_list = [1,2,3,4]
user_choice = int(input('enter user choice (1 - 4)= '))
comp_choice = random.choice(num_list)
if user_choice == comp_choice:
    print('number matched', user_choice, comp_choice)
else:
        print('invalid no.', user_choice, comp_choice)
