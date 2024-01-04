class RajuIntereption(Exception):
    pass
try:
    a=input('enter a string:- ')

    if a[0] in 'aeiouAEIOU':
          raise RajuIntereption ('first char should not be a vowel')
    
except RajuIntereption:
     print('error handled')