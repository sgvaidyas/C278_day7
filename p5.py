class Employee:
    def __init__(self):
        self.empId = int(input("Enter the id = "))
        self.empName = input("Enter the Employee Name = ")
        self.sal = int(input("Enter the sal = "))

e1 = Employee()
e2 = Employee()
emps = []
emps.append(e1)
emps.append(e2)

minsal = min(e.sal for e in emps)
print(minsal)
