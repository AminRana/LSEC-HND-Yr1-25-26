# Mikey Talbot (70221355)

import random

#4a) On Exercise 3a, you have written a program to calculate grades. Modify this program to check first
#whether the given input mark is within the range of 0 and 100 using an outer if statement. If the input mark is
#within the range, then the inner if-else statement will calculate and display correct grades only.
print("")
mark = int(input("What is your mark? "))
if 0 <= mark <= 100:
    if mark > 74:
        print("Grade is Distinction")
    elif mark>60 and mark<74:
      print("grade is Merit!")
    elif mark>40 and mark<59:
        print("grade is Pass.")
    elif mark>0 and mark<39:
        print("grade is Fail.")
    else:
        print("Invalid mark! Please input a number between 0 and 100.")
    print("")

#4b) Write a program to add two input numbers. The program will first check whether the inputs are
#characters or integer numbers using outer if statement. If both inputs are number, then the program will add
#them up and check total is less or more than 100.
    print("")
    num1 = input("What is your first number? ")
    num2 = input("What is your second number? ")
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    total = num1 + num2
    print("The total is: ", total)

    if total>100:
        print("The total is more than 100.")
    elif total<100:
        print("The total is less than 100.")
    else:
        print("The total is equal to 100.")
else:
    print("Error: You input not a valid number!")
    print("")

#4c) Modify Exercise 3c to check first whether the user input is between 1 and 4 or not
#(creating an outer if statement) and if input within range, then put rest codes
#(what you have done for 3c) under inner if statement.
    print("")
    print("menu option:")
    print("1.Add")
    print("2.Search")
    print("3.Update")
    print("4.Delete")
    print("")
    option2 = int(input("What would you like to do? "))
    if 1 <= option2 <= 4:
        if option2 == 1:
            print("Added")
        elif option2 == 2:
            print("Searched")
        elif option2 == 3:
            print("Updated")
        elif option2 == 4:
            print("Deleted")
    else:
        print("Invalid option")
    print("")

#4d) Write a program to generate a random number between 1 and 5, then ask user to type his guess and
#compare his guess with generated random number. If the guess is correct, then repeat the process
#(generate random number, ask user to type his guess and compare them), otherwise, stop the program.
    print("")
while True:
    answer = random.randint(1,5)
    guess = int(input("What is your guess from 1 - 5? "))
    if guess == answer:
        print("Correct! The number has been randomly generated. again.")
    else:
        print("Incorrect! The correct number was "+ str(answer) +"!")
        break
    print("")

#4e)Write a program to calculate odd/even number from a given number. After taking an input from the user,
#the program first will check whether it is within the range of 100 or not. If it is within the range of 100, it will
#calculate odd or even number only.The program will display messages correctly.
    print("")
    num = int(input("What is your number? "))
    if 0 <= num <= 100:
         if num % 2 == 0:
             print("The number is even.")
         else:
             print("The number is odd.")
    else:
        print("Invalid number!")
    print("")