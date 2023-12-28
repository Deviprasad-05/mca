def sum (st,ev):
    if st==ev:
        return st+ sum(st+1,ev)
out=sum(1,5)
print(out)
