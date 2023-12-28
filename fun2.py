def fact():
    a=int(input('enter a num:- '))
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    print(fact)
fact()