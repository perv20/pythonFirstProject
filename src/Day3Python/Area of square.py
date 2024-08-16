"""
1- area of square = length * length
2- area of circle= pie * radius * radius

"""
aos = int(input('enter length= '))
aoc = int(input("enter radius = "))
user_choice = input("enter choice [ aos aoc]= ")
if user_choice == 'aos':
    print("area of square = ", aos * aos)
elif user_choice == 'aoc':
    print("area of circle= ", 3.147 * aoc * aoc)
else:
    print('invalid')