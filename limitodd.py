def show_Numbers():
    user = int(input('Input number > '))
    for x in range(user):
        if x % 2 == 0:
            print(x , 'EVEN')
        elif x % 2 == 1:
            print(x, 'ODD')
            
show_Numbers()