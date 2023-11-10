import random
resultHeads = 0
resultTails = 0
def findFlipResult():
    randomResult  = random.randrange(1,2)
    if randomResult == 1:
        flipResult = "Heads"
    elif randomResult == 2:
        flipResult = "Tails"
    return flipResult
numberOfFlips = int(input("How many flips of a coin do you want to do? "))
for i in range(numberOfFlips):
    flipResult = findFlipResult()
    print("Flip number " + str(i + 1) + " was: " + flipResult)
    if flipResult == "Tails":
        resultTails += 1
    elif flipResult == "Heads":
        resultHeads += 1
    