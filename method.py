class Sbi:
    branch = 'palamaner'
    ifsc = 'sbi00026'
    manager = 'jagan'
    loc     = 'chittoor'

    def __init__(self,name,mob,act,pan,bal):
        self.name = name 
        self.mobile = mob
        self.account = act 
        self.pan = pan 
        self.balence = bal

    def credit(self,amt):
        self.balence+=amt
    def debit(self,amt):
        self.balence-=amt

    def update_mob(self,mob):
        self.mobile=mob

    @classmethod
    def change_mgr(cls,new):
        cls.manager = new
        
    @staticmethod
    def add(a,b):
        return a+b

chandra = Sbi('nara chandra',9087654321,77097654,'CBN790876N',1)
lokesh = Sbi('nara lokesh',9876543210,78954090,'VHN8693088J',2)
                                 