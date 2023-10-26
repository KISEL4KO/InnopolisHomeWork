inData = int(input('Введите любое число: '))

if inData == 0:
    print(inData, 'рублей')
elif inData == 1:
    print(inData, 'рубль')
elif inData < 5:
    print(inData, 'рубля')
else: print(inData, 'рублей')
