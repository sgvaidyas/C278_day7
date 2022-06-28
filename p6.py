class Employee:
    def __init__(self):
        self.empId = int(input("Enter the id = "))
        self.empName = input("Enter the Employee Name = ")
        self.sal = int(input("Enter the sal = "))
    def __str__(self):
        s = " EMPID  = "+ str(self.empId)
        s += "\t EMPNAME = "+self.empName
        s += "\t EMPSAL = "+str(self.sal)
        return s


e1 = Employee()
e2 = Employee()
e3 = Employee()
emps = []
emps.append(e1)
emps.append(e2)
emps.append(e3)

minsal = min(e.sal for e in emps)
min_sal_emps = list(filter(lambda emp: emp.sal == minsal, emps))
for m in min_sal_emps:
    print(m)
