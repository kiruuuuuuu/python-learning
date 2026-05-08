class check:
    def __init__(self,num):
        self.num=num
    def check_palindrome(self):
        i=1
        rev=0
        temp=self.num
        length=len(str(self.num))
        while i<=length:
            digit=temp%10
            rev=rev*10 + digit
            temp //= 10
            i+=1
        if rev==self.num:
            print(f'{self.num} is palindrome')
        else:
            print(f'{self.num} is not palindrome')

    def check_armstrong(self):
        i=1
        sumcubes=0
        temp=self.num
        length=len(str(self.num))
        while i<=length:
            digit=self.num%10
            sumcubes=sumcubes+digit**length
            temp //= 10
            i+=1
        if sumcubes==self.num:
            print(f'{self.num} is armstrong number')
        else:
            print(f'{self.num} is not armstrong number')

    def strongnumber(self):
        i=1
        sumfactorials=0
        temp=self.num
        length=len(str(self.num))
        while i<=length:
            digit=self.num%10
            factorial=1
            for j in range(1,digit+1):
                factorial=factorial*j
            sumfactorials=sumfactorials+factorial
            temp //= 10
            i+=1
        if sumfactorials==self.num:
            print(f'{self.num} is strong number')
        else:
            print(f'{self.num} is not strong number')


c1=check(153)
c1.check_palindrome()
c1.check_armstrong()
c1.strongnumber()

