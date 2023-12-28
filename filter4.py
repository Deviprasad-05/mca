def data(a):
    if a%2!=0:
        return True
    else:
        return False
def squre(b):
    return b**2
out =map(data,range(1,100))
print(list(out))
    
