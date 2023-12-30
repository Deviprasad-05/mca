class Grand:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class parent(Grand):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c=c
        self.d=d
class child(parent):
    def __init__(self,a,b,c,d,e,f):
        super().__init__(a,b,c,d)
        self.e=e
        self.f=f
obj=child(10,20,30,40,50,60)                                                                                                                                                   ''