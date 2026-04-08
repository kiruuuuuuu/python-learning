# nested if statement

# wap to check the given number is positive or negative or zero and also check whether the number is even or odd
num=97
if num>0:
    print('number is positive')
    if num%2==0:
        print('number is even')
    else:
        print('number is odd') # number is odd
elif num<0:
    print('number is negative')
else:
    print('zero')  # number is zero


# wap to check the given year is leap year or not and also check year is even or odd
year=2024
if (year%400==0) or(year%4==0 and year%100!=0):
    print(f'{year} is a leap year')
    if year%2==0:
        print(f'{year} is an even year')
    else:
        print(f'{year} is an odd year') # 2024 is a leap year and 2024 is an even year
else:
    print(f'{year} is not a leap year')

# wap to check 2nd largest number among 3 numbers
a,b,c=95,96,97
if a>b and a>c:
    if b>c:
        print(f'{b} is the 2nd largest number')
    else:
        print(f'{c} is the 2nd largest number') # 95 is the 2nd largest number
elif b>c and b>a:
    if a>c:
        print(f'{a} is the 2nd largest number')
    else:
        print(f'{c} is the 2nd largest number') # 96 is the 2nd largest number
else:
    if a>b:
        print(f'{a} is the 2nd largest number')
    else:
        print(f'{b} is the 2nd largest number') # 97 is the largest number and 96 is the 2nd largest number

#  wap to find 3rd lowest number among 3 numbers
a,b,c=95,96,97
if a<b and a<c:
    if b<c:
        print(f'{b} is the 3rd lowest number')
    else:
        print(f'{c} is the 3rd lowest number')
elif b<a and b<c:
    if a<c:
        print(f'{a} is the 3rd lowest number')
    else:
        print(f'{c} is the 3rd lowest number')
else:
    if a<b:
        print(f'{a} is the 3rd lowest number')
    else:
        print(f'{b} is the 3rd lowest number') # 95 is the lowest number and 96 is the 3rd lowest number


# wap to perform check balance,deposit & withdraw and exit operation using nested if

balance=1000
print('welcome to the atm')
print('atm menu')
print('1.check balance')
print('2.deposit amount')
print('3.withdraw amount')
print('4.exit')
choice=int(input('enter your choice'))
if choice==1:
    print(f'{balance} is your current balance')
elif choice==2:
    amount=int(input('enter the amount to be deposited'))
    if amount>0:
        balance=balance+amount
        print(f'{amount} has been sucussfully deposied and updated balance is rs :{balance}')
    else:
        print('deposit amount should be greater than zero')
elif choice==3:
    withdraw=int(input('enter amount to withdraw'))
    if withdraw<=balance:
        balance=balance-withdraw
        print(f'{withdraw} amount has been sucussfully withdrawed and updated balace is rs :{balance}')
    else:
        print('insufficient balance')
elif choice==4:
    print('thank you for using atm')
else:
    print('invalid choice')



# wap to book ticket in book my show condition is first it should ask teater name 
# then it should display movies avilable & it should display ticket price 
# & it should ask do you want to confirm booking


print('welcome to book my show')
teater_name=input('enter the name of the teater(PVR/INOX)')
if teater_name=='PVR' or teater_name=='INOX':
    if teater_name=='PVR':
        print('movies name available at PVR')
        movie1='avatar: way of water'
        movie2='the batman'
        ticket_price1=550
        ticket_price2=450
    else:
        print('movies name available at INOX')
        movie1='mission impossible'
        movie2='KGF chapter 2'
        ticket_price1=550
        ticket_price2=650
    print(f'1.{movie1}')
    print(f'2.{movie2}')

    movie_choice=input('enter the number to your chosen movie(1/2)')
    if movie_choice==1 or movie_choice==2:
        if movie_choice==1:
            selected_movie=movie1
            ticket_price=ticket_price1
        else:
            selected_movie=movie2
            ticket_price=ticket_price2
        print(f'you have selected {selected_movie}')
        print(f'ticket price rs : {ticket_price}')
        confirmation=input('do you want to confirm the booking (yes/no)')
        if confirmation=='yes':
            print(f'your ticket for {selected_movie} has been booked sucussfully')
        else:
                print(f'ticket booking has been cancelled')
    else:
        print(f'invalid movie choice please try again')
else:
    print(f'sorry teater not avilable')

