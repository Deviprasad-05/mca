class sample:
    __a=10
    b=40
    def __init__(self,c,d):
        self.__c = c
        self.d =d
    def __update_c(self,new):
        self.c=new 
class child(sample):
    pass