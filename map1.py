def length(a):
    if type(a) in [list,tuple,set,dict]:
        return len(a)
    else:
        return a
out =map(length,[1,(4,5),[7.8],{1:2}])
print(list(out))