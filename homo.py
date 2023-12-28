def add_int(a,i=0):
    if len(a)-1==i:
        if a[i]%2==0:
          return a[i]
        else:
           return 0
    if a[i]%2==0:
       return a[i]+add_int(a,i+1)
    else:
       return add_int(a,i+1)
out=add_int(a=[4,5,6,7,8])
print(out)