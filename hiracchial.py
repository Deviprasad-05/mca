class car:
    name="cars"

    def __init__(self,name,milage,price,colour):
        self.name=name
        self.milage=milage
        self.price=price
        self.colour=colour
class supra(car):
    pass
class bmw(car):
    pass
c1=supra("supra mk4",10,50000,"black")
c2=bmw("bmw m4",15,70000,"white")