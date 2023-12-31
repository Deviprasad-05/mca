class add:
    @staticmethod
    def add(a,b):
        return a+b
    
class sub:
    @staticmethod
    def sub(a,b):
        return a-b
class cal(add,sub):
    pass

obj = cal()
obj.add(2,3)
obj.sub(5,6)
