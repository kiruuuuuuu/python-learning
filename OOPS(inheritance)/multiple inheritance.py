# multiple inheritance(more than one parent class and one child class)
# example of multiple inheritance

class grandfather:
    def land(self):
        print('grandfather has land')

class father:
    def bike(self):
        print('father has bike')

class son(grandfather, father):
    def laptop(self):
        print('son has laptop')

s1=son()
s1.land()
s1.bike()
s1.laptop()