choice = input("Please enter operation (+, -, *, /): ")

num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

if choice == '+':
    print(num1 + num2)
elif choice == '-':
    print(num1 - num2)
elif choice == '*':
    print(num1 * num2)
elif choice == '/':
    print(num1 / num2)
else:
    print("Invalid Operation")


i = 1

while i <= 100:
    print(i)

    i = i + 1 ### აქ დავბეჭდე რიცხვები 1 დან 100 ის ჩათვლით while loop ის დახმარებით

    ########


i = 1

while i <= 10:
    print(i)

    i = + 1


    #######


print("Enter the number between 1,3 or 6")
num = int(input(""))

message = "Please choose the numbers in the selection"



if num == 1:
    print("Monday")

elif num == 3:
    print("Wednesday")

elif num == 6:
    print("Saturday")

    
else: print(message)


#######


budget = 10

budget = int(input("Enter your budget: "))

if budget == 10:
    print("Not enough money for specific thing")

elif budget <= 10:
    print("You can buy specific thing")


########

age = int(input("Enter your age: "))

if age <= 5:
    print("You are Child")

elif age <= 11:
    print("You are Teenager ")

elif age <= 18:
    print("You are adult")  


############

num = int(input('Enter a number: '))

if (num %10) == 0:
    print("The number is even")

else: print("The provided number is odd")