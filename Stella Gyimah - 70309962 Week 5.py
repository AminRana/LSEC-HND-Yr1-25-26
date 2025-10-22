#Exercise 1

col="regent college london"

print(col[0:7])     
print(col[0] + col[7] + col[15])
print(col[7:14])
print(col[2:6] + col[10:12])
print(col[18:21])
print(col[0:6] + col[14:21])

#Exercise 2

col2=col.strip()

print(col2)
print(col2.lower())
print(col2.title())
print(col2.upper())
print(col2.find("college"))
print(col2.replace("college", "university"))
print(col2.isalpha())

#Exercise 3

# 3a)
mark=int(input("enter your mark:"))

if mark>74:
 print("distinction")
elif mark>=60:
 print("merit")
elif mark>=40:
 print("pass")
else:
 print("fail")


# 3b)  
word=int(input("enter a word:"))
length=len("word")

if length<=3:
 print("too short word")   
elif length<=8: 
 print("small word")
elif length<=12: 
 print("big word") 
else:
 print("too big word")


# 3c) 
print("1.add\n2.search\n3.update\n4.delete")
choice=int(input("enter your choice(1-4:"))

if choice==1:
 print("added")
elif choice==2:
 print("searched")
elif choice==3:
 print("updated")
elif choice==4:
 print("deleted")
else:
 print("invalid choice")


# 3d)
profession=input("Enter your profession:").lower()

if profession=="teacher":
 print("£25 per hour")
elif profession=="doctor":
 print("£60 per hour")
elif profession=="lawyer":
 print("£200 per hour")
elif profession=="driver":
 print("£15 per hour")
else:
 print("profession not found")


# 3e)
salary=float(input("enter yearly gross salary:"))

if salary<=12570:
 tax=0
elif salary<=50270:
 tax=(salary-12570)*0.20
elif salary<=125140:
 tax=(50270-12570)*0.20+(salary-50270)*0.40
else:
 tax=(50270-12570)*0.20+(125140-50270)*0.40+(salary-125140)*0.45

net_salary=salary-tax
print("tax:", round(tax, 2))
print("net salary:", round(net_salary, 2))


# Exercise 4

# 4a)
mark=int(input("enter mark:"))

if 0<=mark<= 100:
 if mark>74:
  print("distinction")
elif mark>=60:
 print("merit")
elif mark>=40:
 print("pass")
else:
 print("fail")
 print("invalid mark, must be between 0 and 100")



# 4b)
a=input("enter first value:")
b=input("enter second value:")

if a.isdigit()and b.isdigit():
 total=int(a)+int(b)
if total<100:
 print("total is less than 100:", total)
else:
 print("total is 100 or more:", total)
 print("invalid input, numbers only")


# 4c)
 print("1.add\n2.search\n3.update\n4.delete")
num=int(input("enter number(1–4):"))

if 1<=num<=4:
 if num==1:
  print("added")
elif num==2:
 print("searched")
elif num == 3:
 print("updated")
elif num==4:
 print("deleted")
else:
 print("invalid option")



# 4d)
import random

while True:
 rand=random.randint(1, 5)
guess=int(input("guess a number between 1 and 5:"))
if guess==rand:
 print("correct! let's try again.")
else:
 print("Wrong guess! Game over.")   



# 4e)
num=int(input("enter a number:"))

if 0<=num<=100:
 if num % 2==0:
  print(num, "is even")
else:
 print(num, "is odd")
 print("Number must be between 0 and 100")






























 
