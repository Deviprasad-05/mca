a=10
def outer():
    b=20
    def inner():
        nonlocal b
        c=20
        b=100
        print(b)
        print(a)
    print(b)
    inner()
    print(b)
outer()
