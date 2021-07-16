user = input('Enter a number: ')
user2 = input('Enter Second Number: ')
if user < user2:
    print(f'{user2} is greater than {user}.')
elif user > user2:
    print(f'{user} is greater than {user2}.')
else:
    print('Tied!')