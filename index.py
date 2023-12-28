def index_vowel(a):
    out=[]
    i=0
    while i<len(a):
        if a[i] in 'aeiouAEIOU':
            out=out+[i]
        i=i+1
    return out
out=index_vowel("happy new year")
print(out)