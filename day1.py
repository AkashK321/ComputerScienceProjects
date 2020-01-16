print("hello")

print("the number 5 squared " + str(5 * 5))

operator = raw_input("What operation (+,-) ")
num1 = raw_input("Enter 1st number ")
num2 = raw_input("Enter 2nd number ")
if operator == "+":
    print(int(num1)+int(num2))
if operator == "-":
    print(int(num1)-int(num2))