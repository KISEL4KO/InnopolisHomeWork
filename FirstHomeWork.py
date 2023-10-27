inData = input('Введите любое число: ')

checkNum = float(inData)
if checkNum / 1 :
    if inData[-1] == '0':
        print(inData, 'рублей')
    elif inData[-1] == '1':
        print(inData, 'рубль')
    elif inData[-1] < '5':
        print(inData, 'рубля')
    else:
        print(inData, 'рублей')
else: print('Error')
