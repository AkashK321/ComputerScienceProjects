list1 = ["a","b", "c"]
list2 = ["_", "_", "_"]
random_guess= input("Enter a letter: ")
for x in range(0,3):
    if random_guess == list1[x]:
        list2[x] = list1[x]
        break

print(list2)
    