# Write a program to calculate and print a student's grade based on given input mark.
#If mark is above 74, grade is Distinction. If mark is
# between 60 and 74, then grade is Merit. If mark is between 40 and 59, then grade is
# Pass. If mark is between 0 and 39, then grade is Fail.

marks = int(input("Insert your marks: "))

if marks > 74:
    marks = ("Distinction")
    print (f"Well Done! your grade is {marks}")
elif 60 <= marks <= 74:
    marks = ("Merit")
    print (f"Well Done! Your grade is {marks}")
elif 40 <= marks <= 59:
    marks = ("Pass")
    print (f"Well Done! Your grade is {marks}")
elif 0 <= marks <= 39:
    marks = ("Fail")
    print(f"Unfortunately, your grade is {marks}, you'll getem next time")