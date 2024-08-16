maths= int(input('enter the marks of maths='))
eng= int(input('enter the marks of hindi='))
phy= int(input('enter the marks of phy='))

Average = (maths + eng + phy)/3

if Average >= 90:
    print('Grade A')
elif Average >= 80 and < 90:
    print('Grade B')
elif Average >= 80 and < 90:
    print('Grade C')
elif Average < 70:
    print('Grade D')
else:
    print('Invalid Grade')