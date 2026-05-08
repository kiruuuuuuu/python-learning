# constructor method (__init__) is a special method in python classes that is 
# automatically called when an object of the class is created. It is used to 
# initialize the attributes of the class with specific values.


class Student:
    sno=1
    sname='kiran'
    age=20
    course='python'
    location='bangalore basavanagudi'
obj=Student()

print(obj.sno)
print(obj.sname)
print(obj.age)
print(obj.course)
print(obj.location)




# constructor method 
class Student:
    location='Bangalore Basavanagudi'
    def __init__(self, sno, name, age, course):
        self.sno = sno
        self.name = name
        self.age = age
        self.course = course

obj = Student(1, "Kiran J", 20, "Python")
print(obj.sno)
print(obj.name)
print(obj.age)
print(obj.course)
print(obj.location)


# create a class called employee with the following attributes
# name salary dept use the __init__ method 
# to initialize these values when an object is created add a method display details to print
# create 2 objects and display their details

class employee:
    def __init__(self, name, salary, dept):
        self.name = name
        self.salary = salary
        self.dept = dept

    def display_details(self):
        print('employee details')
        print('----------------')
        print(f"Name: {self.name}")
        print(f'Salary: {self.salary}')
        print(f'Department: {self.dept}')

emp1 = employee("kiran", 50000, "developer")
emp2 = employee("vidya", 60000, "test engineer")

emp1.display_details()
emp2.display_details()


# wap to create class person to display name and age of the person using constructor method
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print('person details')
        print('----------------')
        print(f"Name: {self.name}")
        print(f'Age: {self.age}')


p1 = person("smith", 30)
p2 = person("martin", 25)

p1.display_details()
p2.display_details()



# wap to display bank name ,customer name and balance using constructor method
class bank:
    bankname="SBI"
    def __init__(self, customer_name, balance):
        self.customer_name = customer_name
        self.balance = balance

    def display_details(self):
        print('bank details')
        print('----------------')
        print(f'Customer Name: {self.customer_name}')
        print(f'Balance: {self.balance}')
        print(f'Bank Name: {self.bankname}')


b1 = bank("smith", 10000)
b2 = bank("martin", 15000)

b1.display_details()
b2.display_details()



# wap to display multiple customer information by taking user input using constructor method
class bank:
    bankname="SBI"
    def __init__(self, customer_name, balance):
        self.customer_name = customer_name
        self.balance = balance

    def display_details(self):
        print('bank details')
        print('----------------')
        print(f'Customer Name: {self.customer_name}')
        print(f'Balance: {self.balance}')
        print(f'Bank Name: {self.bankname}')

num=int(input("Enter the number of customers: "))
accounts = []
for i in range(num):
    print(f"Enter details for customer {i+1}:")
    name = input("Enter customer name: ")
    balance = float(input("Enter balance: "))
    account = bank(name, balance)
    accounts.append(account)

for account in accounts:
    account.display_details()




# wap for atm sceanario using constructor method
class bankname:
    def __init__(self,name,pin,balance):
        self.name=name
        self.pin=pin
        self.balance=balance
    def check_pin(self):
        try:
            enter_pin=int(input('Enter your pin: '))
            raise ValueError('invalid pin')
        except ValueError as e:
            print(e)
            return False
    def deposit(self):
        amount=float(input('Enter the amount to deposit: '))
        if amount>0:
            self.balance+=amount
            print(f'Amount {amount} has been deposited successfully.\n Current balance: {self.balance}')
        else:
            print('Invalid amount. Please enter a valid amount.')
    def withdraw(self):
        amount=float(input('Enter the amount to withdraw: '))
        if amount<=self.balance:
            self.balance-=amount
            print(f'Amount {amount} has been withdrawn successfully.\n Current balance: {self.balance}')
        else:
            print('Invalid amount or insufficient balance. Please enter a valid amount.')

    def display_details(self):
        print('bank details')
        print('----------------')
        print(f'Customer Name: {self.name}')
        print(f'Balance: {self.balance}')

customer1=bankname('kiran',1234,10000)
customer1.deposit()
customer1.withdraw()
customer1.display_details()



# types of constructor method
# 1. default constructor: a constructor that takes no parameters and initializes the attributes with default values.
# 2. user defined constructor: a constructor that takes parameters and initializes the attributes with specific values provided by the user.
# 2.1 parameterized constructor: a constructor that takes parameters and initializes the attributes with specific values provided by the user.
# 2.2 non parameterized constructor: a constructor that takes no parameters and initializes the attributes with specific values provided by the user.


# example of default constructor

class employee:
    def read(self,ename='smith', salary=50000):
        self.ename=ename
        self.salary=salary
    def display(self):
        print('employee details')
        print('----------------')
        print(f'Employee Name: {self.ename}')
        print(f'Salary: {self.salary}')

e1=employee()
e1.read('martin', 60000)
e1.display()

e2=employee()
e2.read()
e2.display()



# example for parameterized constructor

class employee:
    def __init__(self, ename, salary):
        self.ename = ename
        self.salary = salary

    def display(self):
        print('employee details')
        print('----------------')
        print(f'Employee Name: {self.ename}')
        print(f'Salary: {self.salary}')

emp1 = employee('kiran', 50000)
emp2 = employee('vidya', 60000)
emp1.display()
emp2.display()

# exmaple for non parameterized constructor

class employee:
    def __init__(self):
        pass
    def display(self):
        print('employee details')
        print('----------------')
        print(f'Employee Name: {self.ename}')
        print(f'Salary: {self.salary}')

emp1 = employee()
emp1.ename = 'kiran'
emp1.salary = 50000
emp1.display()



emp2 = employee()
emp2.ename = 'vidya'
emp2.salary = 60000
emp2.display()
