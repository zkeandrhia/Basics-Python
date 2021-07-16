def fizz_buzz(n):
    if n % 3 == 0:
        print('Fizz!')
    elif n % 5 == 0:
        print('Buzz!')
    elif n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz!')
    else:
       print(n) 
n = 126
fizz_buzz(n)