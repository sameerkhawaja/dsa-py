def getPoints(input):
    inputList = input.split('|')
    winners = set(" ".join(inputList[0].split()).split())
    numbers = " ".join(inputList[1].split()).split()

    result = 0
    for number in numbers:
        if number in winners:
            if result == 0:
                result = 1
            else:
                result *= 2
    return result

def getCardNumber(input):
    cardNumber =  input.split(" ")[-1]
    return cardNumber

def main():
    result = 0
    with open('./advent_of_code/test.txt', 'r') as openfile:
        for line in openfile:
            lineSplit = line.split(':')

            cardNumber = getCardNumber(lineSplit[0])
            points = getPoints(lineSplit[1])

            print(f"Points won for card {cardNumber}: {points}")

            result += points

    return result


print(main())

