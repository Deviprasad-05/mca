try:
    a=1/0
    d=(1,2)
    print(d[5])
except Exception:
    print('error handled')
finally:
    print('exception handled')

