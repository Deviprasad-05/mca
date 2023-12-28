def char(a):
    if 'A'<='Z':
        return True
    else:
        return False
out =map(char,filter(char,'fdgfsdFDHAFDF'))
print(list(out))