# Mikey Talbot (70221355)

#3a) Write a program to calculate and print a student's grade based on given input mark.
#If mark is above 74, grade is Distinction.
#If mark is between 60 and 74, then grade is Merit.
#If mark is between 40 and 59, then grade is Pass.
#If mark is between 0 and 39, then grade is Fail.
print("")
mark = int(input("What is your mark? "))
if mark > 74:
  print("Grade is Distinction")
elif mark >60 and mark <74:
  print("grade is Merit!")
elif mark >40 and mark <59:
  print("grade is Pass.")
elif mark >0 and mark <39:
  print("grade is Fail.")
else:
  print("Wrong input mark!")
print("")

#3b) Write a program to calculate the number of characters from a user's string input. If the number
#of characters is  between 1 and 3, between 4 and 8, between 9 and 12, and more than 12 then display results
#too short word, small word, big word and too big word respectively.
print("")
word = str(input("What is your input? "))
length = len(word)
if 1 <= length <= 3:
    print("too short word")
elif 4 <= length <= 8:
    print("small word")
elif 9 <= length <= 12:
    print("big word")
elif length > 12:
    print("too big word")
else:
    print("Wrong input!")
print("")

#3c) Write a program to display a menu option. Then it will ask you to type a number between
#1 and 4. If 1, 2, 3 and 4 are typed, the program displays "Added", "Searched", "Updated" and "Deleted"
#messages respectively. The menu option looks like:
#1. Add
#2. Search
#3. Update
#4. Delete
print("")
print("menu option:")
print("1.Add")
print("2.Search")
print("3.Update")
print("4.Delete")
print("")
option = int(input("What would you like to do? "))
if option == 1:
    print("Added")
elif option == 2:
    print("Searched")
elif option == 3:
    print("Updated")
elif option == 4:
    print("Deleted")
else:
    print("Invalid option")
print("")

#3d) Write a program to display hourly rate for 4 different professions.
#The program will ask user to type a profession and then display the hourly rate of the profession.
#The hourly rate of teacher, doctor, lawyer and driver is £25, £60, £200 and £15 respectively.
print("")
profession = input("What is your profession? ")
if profession == "teacher":
    print("Hourly rate of teacher is £25")
elif profession == "doctor":
    print("Hourly rate of doctor is £60")
elif profession == "lawyer":
    print("Hourly rate of lawyer is £200")
elif profession == "driver":
    print("Hourly rate of driver is £15")
else:
    print("Invalid profession")
print("")

#3e) Write a program to calculate yearly tax and net salary from the input of a yearly gross salary.
#For the program, yearly tax rate is given below:
#Up to £12,570 no tax is required
#Between £12,571 and £50,270 20% tax
#Between £50,271 and £125,140 40% tax
#Above £125,141 45% tax
print("")
salary = int(input("What is your salary? £"))
if salary <= 12570:
    print("no tax is required")
elif 12571 <= salary <= 50270:
    print("20% tax is required")
elif 50271 <= salary <= 125140:
    print("40% tax is required")
elif salary > 125141:
    print("45% tax is required")
else:
    print("Wrong input!")
print("")