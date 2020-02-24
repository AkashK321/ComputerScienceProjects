from __future__ import print_function
from random import *


def binary_search():
    number = randint(1,6000)
    
    guess = 3000
    numberOfGuess = 1
    
    print(str(number) + "\n")
    
    while guess != number:
        lastGuess = guess
        if guess < number:
            guess = ((number - guess)/2) + guess
        if guess > number:
            guess = guess - ((guess - number)/2)  
        numberOfGuess += 1
        if guess == lastGuess:
            if guess < number:
                guess += 1
            if guess > number:
                guess -= 1
        print (str(guess))
        
    print("\n" + str(numberOfGuess))
    
def insertion_sort():
    array = [2,1,7,8,4,10,25,14,13,100,54]
    i = 0
    for i in range(1, len(array)):
        item = array[i]
        x = i-1
        while x>=0 and item < array[x]:
            array[x+1] = array[x]
            x -= 1
        array[x+1] = item
    print(array)

def bubble_sort():
    def sort_integers():
        numberList = raw_input("Give a list of numbers seperated by spaces: ")
        array = map(int, numberList.split())
        print("Starting array: ", array)
        i = 0
        if len(array) > 1:
            while True:
                if i >= (len(array)-1):
                    i -= (len(array)-1)
                if array[i] == array[i+1]:
                    pass
                elif array[i] > array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i]
                i += 1
                if array == sorted(array):
                    break
                # if array == [1,1,2,3,4,5,5]:
                #     break
        # print("The end result: ", array)
        print("The end result: ", array)
    def sort_characters():
        characterString = raw_input("Input a string of characters: ")
        print("\n")
        array = list(characterString)
        print("Starting list:"),
        for z in range(0, len(array)):
            print(str(array[z]), end="")
        print("\n")
        ASCIIarray = []
        sortedArray = []
        i = 0
        for z in array:
            ASCIIvalue = ord(z)
            ASCIIarray.append(ASCIIvalue)
        while True:
                if i >= (len(ASCIIarray)-1):
                    i -= (len(ASCIIarray)-1)
                if ASCIIarray[i] == ASCIIarray[i+1]:
                    pass
                elif ASCIIarray[i] > ASCIIarray[i+1]:
                    ASCIIarray[i], ASCIIarray[i+1] = ASCIIarray[i+1], ASCIIarray[i]
                i += 1
                for x in ASCIIarray:
                    character = chr(x)
                    print(character, end="")
                print("")
                if ASCIIarray == sorted(ASCIIarray):
                    break
        for x in ASCIIarray:
            value = chr(x)
            sortedArray.append(value)
        print("\n")
        print("Sorted list:"),
        for z in range(0, len(sortedArray)):
            print(sortedArray[z], end="")
    sort_characters()

def quick_sort():
    def partition(arr, low, high):
        i = (low-1)
        pivot = arr[high]
        
        for j in range(low, high):
            
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)
        
    def sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            sort(arr, low, pi-1)
            sort(arr, pi+1, high)
    arr = [1,6,3,10,16,13,11]
    n = len(arr)
    sort(arr, 0, n-1)
    print("The sorted array is: "),
    for z in range(0, n-1):
        print(str(arr[z]) + ", "),
    print(arr[n-1])



         
        



