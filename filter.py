def fname(a):
    if a%2 ==0:
        return True
    else:
        return False
out = filter (fname,[2,6,8,10,5,1])
print(list(out))