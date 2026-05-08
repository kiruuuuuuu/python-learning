# hierarchical inheritance(one parent class and multiple child classes)



# example of hierarchical inheritance

class father:
    def property(self):
        print('father has property')

class son(father):
    def bike(self):
        print('son has bike')   

class daughter(father):
    def car(self):
        print('daughter has car')   


s1=son()
s1.property()
s1.bike()
d1=daughter()
d1.property()
d1.car()

