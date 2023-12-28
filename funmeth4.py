def add_int(arr):
    out=0
    for i in arr:
        if type(i) == int:
            out+=i
    print(out)
add_int([1,2,'a','b',5,4,])
add_int([5,9,'s'])