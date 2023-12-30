class Employee:
    company = 'tcs'
    ceo     = 'Elon mask'

    def insert_member(obj,name,age,sal,eid):
        obj.name = name
        obj.age = age
        obj.sal = sal
        obj.eid = eid
raju = Employee()
ramu = Employee()

Employee.insert_member(raju,'raju',22,30000,101)
Employee.insert_member(ramu,'ramu',23,40000,102)
    