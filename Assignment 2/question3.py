def sumOfDoubleEvenPlace(number):
    doubleEvenPlace = list(number)
    doubleEvenPlace.reverse()
    doubleEvenPlace = doubleEvenPlace[1::2]
    doubleEvenPlace = list(map(int, doubleEvenPlace))
    return sum(getDigit(x*2) for x in doubleEvenPlace)

def sumOfOddPlace(number):
    oddPlace = list(number)
    oddPlace.reverse()
    oddPlace = oddPlace[0::2]
    oddPlace = list(map(int, oddPlace))
    return sum(oddPlace)

def getDigit(number):
    number = list(str(number))
    number = list(map(int, number))
    return sum(number)

def isValid(number):
    cardLength = len(number)
    if cardLength <=16 and cardLength >=13:
        if (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0:
            print('Card is valid')
        else:
            print('Card is not valid')
    else:
        print('Card is not valid')

cardNum = (input('Enter card number to be validated: '))
isValid(cardNum)