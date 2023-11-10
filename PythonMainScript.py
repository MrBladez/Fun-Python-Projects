import random
resultHeads = 0
resultTails = 0
def findFlipResult():
    randomResult  = random.randrange(1,3)
    if randomResult == 1:
        flipResult = "Heads"
    elif randomResult == 2:
        flipResult = "Tails"
    return flipResult
numberOfFlips = int(input("How many flips of a coin do you want to do? "))
for i in range(numberOfFlips):
    flipResult = findFlipResult()
    if flipResult == "Tails":
        resultTails += 1
    elif flipResult == "Heads":
        resultHeads += 1
tailsPercent = round(resultTails / numberOfFlips, 3)
headsPercent = round(resultHeads / numberOfFlips, 3)
print("Number of tails flips was: " + str(resultTails))
print("Number of heads flips was: " + str(resultHeads))
print("Percent of tails flips was: " + str(tailsPercent) + " and percent of heads was: " + str(headsPercent) + " .")

    