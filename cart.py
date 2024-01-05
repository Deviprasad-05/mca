
print('WELCOME TO AMAZON ')
products=int(input('please enter the number of product you want:- '))
category=int(input('please select 1-->TV \n 2-->mobile \n 3-->laptop'))
if category ==1:
    amount=products*10000
if category ==2:
    amount=products*5000
if category ==3:
    amount=products*20000
print(f'Hi  you have bookrd {products} products and total amount is {amount}')  
