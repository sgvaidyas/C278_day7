class Employee:
    def __init__(self,id):
        self.empId = id
        self.empName = input("Enter the Employee Name = ")
    def disp(self):
        print(str(self.empId) + "   " + self.empName)

emps = []

flag=True
while flag==True:
    print("1 Insert Employee 2 Display 3 Exit ")
    ch = int(input("Enter the choice = "))
    if ch==1:
        empid = int(input("Enter the employee id = "))
        checkSet = {True for e in emps if empid==e.empId}
        #here we do not have employee with given id in the list
        if(checkSet==set()):
            e = Employee(empid)
            emps.append(e)
        else:
            print("Employee with the id specified already exists ")
    elif 2:
        print("Records = ")
        for e in emps:
            e.disp()
    else:
        flag = False

