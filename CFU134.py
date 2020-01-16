from __future__ import print_function
import random

def food_id(food):
    # The data
    fruits = ['apple', 'banana', 'orange', "tomato", "kiwi"]
    citrus = ['orange']
    starchy = ['banana', 'potato', "kiwi"]
    # Check the category and report
    if food in fruits and not starchy:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy and fruits:
            return 'Starchy, Fruit'
        elif food in starchy and not fruits:
            return "Starchy, NOT Fruit"   
        else:
            return 'NOT Starchy, NOT Fruit'
            
def guess_once():
    secret = random.randint(1, 4)
    print ("I have a number between 1 and 4.")
    guess = int(raw_input("Guess: "))
    if guess > secret:
        print("Too high, my number was " + str(secret))
    if guess < secret:
        print("To low, my number was " + str(secret))
    else:
        print("Right, my number is ", guess, end="!\n")
        
def guess_game():
    i = 0
    secret = random.randint(1, 50)
    print("I have a number between 1 and 50 (to stop the game type stop)")
    guess = raw_input("Guess: ")
    if guess == "stop":
        print("Game over")
    else:
        i = 1
        while int(guess) != secret:
            if int(guess) > secret:
                print("Too high")
            elif int(guess) < secret:
                print("Too low")
            guess = raw_input("Guess: ")
            if guess == "stop":
                print("Game over")
                break
            i = i + 1
        if guess == "stop":
            pass
        else:
            print("You won in " + str(i) + " guesses")

# x = 0
# number = random.randint(1, 10)     
# def guessGameNoLoop():
#     print ("I have a number between 1 and 10.")
#     guess = int(raw_input("Guess: "))
#     if guess > number:
#         x = x + 1
#         print("Too high " + str(x))
#         if x != 5:
#             guessGameNoLoop()
#     elif guess < number:
#         x = x + 1
#         print("To low " + str(x))
#         if x != 5:
#             guessGameNoLoop()
#     elif guess == number:
#         print("You won")

    
       















