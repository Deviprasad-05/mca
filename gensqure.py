def cal(a,b):
    for i in range(a,b+1):
        yield i*i
out =cal(5,15)
print(list(out))
