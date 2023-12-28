def length(a):
    if type(a) in [list,tuple,set,str]:
        return len(a)
    else:
        return a
a=[len(i) for i in ["abcd",{1:2},[4,5,6],{4,7},(6,7,8)]]
print(a)
    