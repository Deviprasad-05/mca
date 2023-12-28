def sample(a):
    if a%5==0 and a%3==0:
        return True
    else:
        return False
out=filter(sample,range(1,200))
print(list(out))