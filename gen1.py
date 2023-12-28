def sample(a):
    for i in a:
        if type(i) in [list,set,str,tuple,dict]:
            yield len(i)
        else:
            yield i
out =(sample([1,[4,5,6],{27,8},'efg',{'a':1},9.1,12])) 
print(list(out))