
num1 = 0

for num1 in range(100):
    print(num1 + num1 - num1 * num1)

############### აქ გავაკეთე არითმეტიკური ოპერაციები

num = int(input("Enter First number: "))

for num in range(11):

    print(num)


    ############# აქ ვთხოვე მომხმარებელს რომ შეეყვანა პირველი ციფრი და ციკლში ამოვარდებოდა 10



####  მომხმარებელს შემოვატანინე 
# ორ რიცხვი ხოლო ამის შემდეგ for loop - ის გამოყენებით გამოვატანინე ამ რიცხვებს შორის ჯამი და ნამრავლი

num2 = int(input("Enter First Number: "))
num3 = int(input("Enter Second Number: "))


for nums in range(37):
    print(nums + num2 * num3 * num2)


#########


programming_educations = ["Goa", "Novatori", "Bitcamp"]

for x in programming_educations:
    print(x)


##########


for x in "Goal Oriented Academy":
    print(x)

##########

programming_educations = ["Goa", "Novatori", "Bitcamp"]

for x in programming_educations:
    print(x)

    if x == "Novatori":
        break

    ########

for x in programming_educations:
    print(x)

    if x == "Novatori":
        break
    print(x)


    ######


programming_educations = ["Goa", "Novatori", "Bitcamp"]

for x in programming_educations:
    print(x)

    if x == "Bitcamp":
        continue
   

