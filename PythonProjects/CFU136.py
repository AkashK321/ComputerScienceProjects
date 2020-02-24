from random import *

def craps1():
    scores = [0,0]
    roundTally = [0,0]
    numberOfRounds = int(raw_input("How many rounds do you want to play? "))
    print("Round tally: " + str(roundTally) + "\n" + "\n")
    for i in range (1,numberOfRounds+1):
        print("Round " + str(i))
        for x in range (0,2):
            raw_input("Player " + str(x+1) + " click enter to roll both dice")
            dice1 = randint(1,6)
            dice2 = randint(1,6)
            scores[x] = dice1 + dice2
            print("First roll: " + str(dice1) + "\n" + "Second roll: " + str(dice2))
            print("Player " + str(x+1) + " score: " + str(scores[x]) + "\n")
        if scores[0] > scores[1]:
            roundTally[0] = roundTally[0] + 1
        elif scores[1] > scores[0]:
            roundTally[1] = roundTally[1] + 1
        print("Round tally: " + str(roundTally) + "\n" + "\n")
    if roundTally[0] > roundTally[1]:
        print("Player 1 wins!")
    elif roundTally[1] > roundTally[0]:
        print("Player 2 wins!")
    else:
        print("It is a tie!")

    
def craps2():
    diceValues = [1,2,3,4,5,6]
    scores = [0,0]
    roundTally = [0,0]
    numberOfRounds = int(raw_input("How many rounds do you want to play? "))
    print("Round tally: " + str(roundTally) + "\n" + "\n")
    for i in range (1,numberOfRounds+1):
        print("Round " + str(i))
        for x in range (0,2):
            raw_input("Player " + str(x+1) + " click enter to roll both dice")
            dice1 = choice(diceValues)
            dice2 = choice(diceValues)
            scores[x] = dice1 + dice2
            print("First roll: " + str(dice1) + "\n" + "Second roll: " + str(dice2))
            print("Player " + str(x+1) + " score: " + str(scores[x]) + "\n")
        if scores[0] > scores[1]:
            roundTally[0] = roundTally[0] + 1
        elif scores[1] > scores[0]:
            roundTally[1] = roundTally[1] + 1
        print("Round tally: " + str(roundTally) + "\n" + "\n")
    if roundTally[0] > roundTally[1]:
        print("Player 1 wins!")
    elif roundTally[1] > roundTally[0]:
        print("Player 2 wins!")
    else:
        print("It is a tie!")

def scramble():
    words_set = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    var_picker = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    for i in range(0,8):
        var = choice(var_picker)
        var_picker.remove(var)
        print(words_set[var])
    
    

  
    
    