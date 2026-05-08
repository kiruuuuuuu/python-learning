# inheritance is an object oriented programming concept in python
# where one class aquires the properties and behaviors of another class
# the class that inherits is called the child class or subclass
# the class that is inherited from is called the parent class or superclass
# inheritance helps in code reusablity
# we can perform method overriding in inheritance(same method name but different implementation in child class)

# types of inheritance in python
# 1. single level inheritance
# 2. multilevel inheritance
# 3. multiple inheritance
# 4. hierarchical inheritance
# 5. hybrid inheritance 

# 1. single level inheritance(one parent class and one child class)
# example of single level inheritance
class father:
    def bike(self):
        print('father has bike')
class son(father):
    def laptop(self):
        print('son has laptop')

s1=son()
s1.bike()
s1.laptop()