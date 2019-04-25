import random

wheel = set(range(0,37))
wheel.add('00')
red = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
black = set(range(1,37)) - red
green ={0,'00'}
even = set(range(2,37,2))
odd = set(range(1,37)) - even
small = set(range(1,19))
great = set(range(19,37))
propertys = {'red':red, 'black':black, 'even':even, 'odd':odd, 'small':small, 'great':great, 'green':green}

money = int(input('How many $ want to play: '))
bet = int(input("Give your bet: "))
pred = input('Give mi the next number propertys: ')

while bet != 0:
    try:
        propertys[pred]
        num = random.choice(list(wheel))
        flag = False
        print(num)

        for k in propertys:
            if num in propertys[k]:
                #print(k)
                if pred == k:
                    flag = True
        if flag == True:
            money += bet
            print('Win!\n')

        else:
            money -= bet
            print('Loose!\n')
            if money <= 0:
                break

        bet = int(input("Give your bet: "))
        if bet != 0:
            pred = input('Give mi the next number propertys: ')

    except KeyError:
        print('You should select from the real propertys!')
        pred = input('Give mi the next number propertys!\n')
        bet = int(input("Give your bet: "))
