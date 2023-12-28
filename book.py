print('Welcome to BOOK MY SHOW')
name=input('please enter your name:- ')
seats=int(input('please enter the number of seats you want:- '))
category=int(input('please select 1-->diamand \n 2-->gold \n 3-->silver'))
if category ==1:
    amount=seats*200
if category ==2:
    amount=seats*150
if category ==3:
    amount=seats*100
print(f'Hi {name} you have bookrd {seats} seats and total amount is {amount}')