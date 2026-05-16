emp_details={101:{"name":"A","age":25,"dep":"accounting","salary":250000},
102:{"name":"B","age":28,"dep":"marketing","salary":300000},
103:{"name":"C","age":30,"dep":"devs","salary":200000}}

def add_emp(ids:int,name:str,age:int,dept:str,sal:int):
    emp_details[ids]={"name":name,"age":age,"dep":dept,"salary":sal}
def view_employees():
    if len(emp_details)==0:
        print("No emplyee available")
    print("     employee id     |     name     |     age     |     department     |     salary     |")
    for i in emp_details:
        print(i," "*(19-len(str(i))),'|',{emp_details[i]['name']}," "*(7-len(emp_details[i]['name'])),"|",{emp_details[i]['age']}," "*(8-len(str(emp_details[i]['age']))),"|",{emp_details[i]['dep']}," "*(13-len(emp_details[i]['dep'])),"|",{emp_details[i]['salary']}," "*(11-len(str(emp_details[i]['salary']))),"|")
def search_employee(ids:int):
    if ids in emp_details:
        print(emp_details[ids])
    else:
        print("employee not found")
flag=True
def main_menu():
    global flag
    print("-"*100)
    print("1. View all employees")
    print("2. Search employee")
    print("3. Add employee")
    print("4. Exit")
    ch=int(input("Enter your choise: "))
    if ch==1:
        view_employees()
    elif ch==2:
        try:
            a=int(input("Enter the id of the employee : "))
            search_employee(a)
        except:
            print("Enter valid id type")
    elif ch==3:
        try:
            ids=int(input("Enter the id of the employee : "))
            name=input("Enter employee's name : ")
            age=int(input("Enter employee's age : "))
            dept=input("Enter employee's department : ")
            sal=int(input("Enter the employee's salary : "))
            add_emp(ids,name,age,dept,sal)
            print("Employee added")
        except:
            print("Enter valid data type")
    elif ch==4:
        flag=False
while flag:
    main_menu()