class Employee:
    company = 'tcs'
    ceo     = 'Elon mask'

    def insert_member(self,name,age,sal,eid):
        self.name = name
        self.age = age
        self.sal = sal
        self.eid = eid
raju = Employee()
ramu = Employee()
raja = Employee()

Employee.insert_member(raju,'raju',22,30000,101)
Employee.insert_member(ramu,'ramu',23,40000,102)
raja.insert_member('RAJA',22,10,103)
    