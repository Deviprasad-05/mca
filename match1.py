num1 =int(input('enter a num1:- '))
num2 =int(input('enter a num2:- '))
operator =int(input('enter a operator:- '))
match operator:
    case 1:
        print('add')
        num=num1+num2
    case 2:
        print('sub')
        num=num1-num2
    case 3:
        print('mul')
        num=num1*num2
    case 4:
        print('div')
        num=num1/num2
print(num)

