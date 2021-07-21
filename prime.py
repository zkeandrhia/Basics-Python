# all prime numbers are greater than 1
#first try
print('Finding Prime numbers of your own range!\n ')

first = int(input('Enter the First number in range: '))

print("\nPrime numbers between", first, "are:\n")

for numbers in range (first + 1):
    if numbers > 1:
        for a in range (2, numbers):
            if (numbers % a) == 0:
                break
        else:
            print(numbers)
    

