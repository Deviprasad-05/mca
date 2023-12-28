def upper(a):
    if 'A' <=a<= 'Z':
        return True
    else:
        return False
out =filter(upper,'ghdABC')
print(list(out))