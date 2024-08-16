"""
when we have to match multiple conditions then use elif

1- we have to print calculation on the basis of user choice
take the input of two numbers from user and give the choice + -

"""
num_1 = int(input('enter num_1= '))
num_2 = int(input('enter num_2= '))
user_choice = input('enter operation [+ - * /]=')
if user_choice == '+':
    print('addition of =' , num_1 + num_2)
elif user_choice == '-':
    print('subs=', num_2-num_1)
elif user_choice == '*':
    print('mult=', num_1 * num_2)
elif user_choice == '/':
    print('div=', num_1 / num_2)
else:
    print('invalid no.')

