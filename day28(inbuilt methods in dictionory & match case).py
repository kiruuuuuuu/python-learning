# inbuilt methods in dictionory
# get method

data={'ename':'smith','sal':98000}
print(data.get('ename'))

# update method
data={'ename':'smith','sal':98000}
data.update({'sal':98500})
print(data)  # {'ename': 'smith', 'sal': 98500}


data={'ename':'smith','sal':98000}
data.update({'job':'analyst'})
print(data)  # {'ename': 'smith', 'sal': 98000, 'job': 'analyst'}


# item method

data={'ename':'smith','sal':98000}
print(data.items()) # dict_items([('ename', 'smith'), ('sal', 98000)])

# keys method
data={'ename':'smith','sal':98000}
print(data.keys()) # dict_keys(['ename', 'sal'])

# values method

data={'ename':'smith','sal':98000}
print(data.values()) # dict_values(['smith', 98000])



# # match case
# example 1


num=int(input('enter a number'))
match num:
    case 1:
        print('you entered one')
    case 2:
        print('you entered two')
    case _:
        print('you entered other numbers')


# example 2

day=input('enter a day number(1-7): ')
match day:
    case '1':
        print('Monday')
    case '2':
        print('Tuesday')
    case '3':
        print('Wednesday')
    case '4':
        print('Thursday')
    case '5':
        print('Friday')
    case '6':
        print('Saturday')
    case '7':
        print('Sunday')
    case _:
        print('Invalid day number')

# example 3

data={'ename':'smith','sal':98000}
key=input('enter a key to search: ')    
match key:
    case 'ename':
        print('Employee Name:',data['ename'])
    case 'sal':
        print('Employee Salary:',data['sal'])
    case _:
        print('Key not found in dictionary')

# example 4

balance=97000
while True:
    print('bank menu')
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')
    choice=eval(input('enter your choice: '))
    match choice:
        case 1:
            print(f'your balance is {balance}')
        case 2:
            amount=float(input('enter amount to deposit: '))
            if amount>0:
                balance+=amount
                print(f'{amount} deposited successfully. New balance: {balance}')
            else:
                print('Invalid deposit amount')
        case 3:
            amount=float(input('enter amount to withdraw: '))
            if amount<=balance and amount>0:
                balance -= amount
                print(f'{amount} withdrawn successfully. New balance: {balance}')
            else:
                print('Invalid withdrawal amount or insufficient balance')
        case 4:
            print('Thank you for using our banking services.')
            break
        case _:
            print('Invalid choice. Please try again.')