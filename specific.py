try:
    a=1/0
    print(a)
except (TypeError,ZeroDivisionError):
    print('error handled')
except ValueError:
    print('can not type cast string to dict')
finally:
    print('exception handled')

def sum(a,b):
      return a+b
print(sum(2,3))