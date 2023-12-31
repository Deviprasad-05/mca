class add3:
    @staticmethod
    def add(a,b,c):
        return a+b+c
class add2:
    @staticmethod
    def add(a,b):
        return a+b
class add(add3,add2):
    pass
    
class sub2:
    @staticmethod
    def sub(a,b):
        return a-b
class cal(add,sub2):
    pass

obj = cal()
