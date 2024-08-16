"""
if condition: {true/False}
    statement
else
if
elif
else
"""

admin = 'admin'
pwd = 'pass123'
userid = input('enter userid= ')
password = input('enter password= ')
if userid == admin and password == pwd:
    print('login successful')
else:
    print('uid or password incorrect')
