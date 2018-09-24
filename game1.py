again=0
while again==0:


    from random import randint

    lowerBound = 0
    upperBound = 9

    threeRandomNumbers = []
    threeRandomNumbers.append(randint(lowerBound, upperBound))
    threeRandomNumbers.append(randint(lowerBound, upperBound))
    threeRandomNumbers.append(randint(lowerBound, upperBound))

    userInput = []

    for i in range(3):
        userInput.append(int(input('Please enter number ' + str(i + 1) + ' : ')))

    ordererd = [i for i, j in zip(threeRandomNumbers, userInput) if i == j]

    disOrdered = set(userInput).intersection(threeRandomNumbers)
    if len(disOrdered) == 3:
        again=1
        print("you win")
    elif len(ordererd) < 3 and len(disOrdered) != 0:
        print("match")
    elif len(disOrdered) < 3 and len(disOrdered) != 0:
        print("close")
    else:

        print("nope")


