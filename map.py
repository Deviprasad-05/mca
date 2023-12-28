def double(a):
    if a%2==0:
          return a*a
    if a%2!=0:
         return a*a*a
out =map(double,[1,2,3,4,5,6])
print(list(out))