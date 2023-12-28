def fname(a):
    out=0
    for i in a:
        if type(a) in [int,float,complex,bool]:
            out+=1
out =filter(fname,[1,3+2j,False,2,5,{2.3},(2,3,4),{3:5},(2,3,5)])
print(list(out))