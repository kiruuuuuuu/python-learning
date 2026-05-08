# multilevel inheritance(multiple parent classes and one child class)
# example of multilevel inheritance

class father:
    def money(self):
        print('father has money')
class mother:
    def gold(self):
        print('mother has gold')

class son(father, mother):
    def laptop(self):
        print('son has laptop')

s1=son()
s1.money()
s1.gold()
s1.laptop()