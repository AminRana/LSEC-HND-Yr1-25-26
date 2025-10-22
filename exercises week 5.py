# Exercise 1

# 1a)
s=input("enter a word:")
vowels="aeiouAEIOU"
for ch in s:
    if ch in vowels:
        print(ch, "-> vowel")
    else:
        print(ch, "-> not vowel")

# 1b)
total=sum(range(2, 21, 2))
print("sum of even numbers up to 20 =", total)

# 1c)
while True:
    print("\nMENU\n1.Add\n2.Search\n3.Update\n4.Delete\n5.Quit")
    try:
        choice=int(input("Choose(1-5):"))
    except ValueError:
        print("Numbers only please.")
        continue
    if choice==1:
        print("Added")
    elif choice == 2:
        print("Searched")
    elif choice==3:
        print("Updated")
    elif choice==4:
        print("Deleted")
    elif choice==5:
        print("Bye!")
        break
    else:
        print("Invalid option")

# 1d) 
n=int(input("Enter a number to test prime:"))
if n<2:
    print("Not prime")
else:
    is_prime=True
    for d in range(2, int(n**0.5)+1):
        if n % d==0:
            is_prime=False
            break
    print("Prime" if is_prime else "Not prime")

# 1e
limit = int(input("List primes up to:"))
for x in range(2, limit + 1):
    prime=True
    for d in range(2, int(x ** 0.5) + 1):
        if x % d==0:
            prime=False
            break
    if prime:
        print(x, end=" ")
print()

# 1f) Times table for a given number (1 to 10)
t=int(input("Times table for:"))
for i in range(1, 11):
    print(f"{t} x {i} = {t*i}")


# Exercise 2 

# 2a) 
for n in range(1, 7):
    print(f"{n} = {n}, {n**2}, {n**3}, {n**4}")

# 2b) 
num=1
for row in range(5):
    line=[]
    for _ in range(10):
        line.append(str(num))
        num+=1
    print(" ".join(line))

# 2c) 
for start in range(0, 101, 10):
    row=[str(start + k) for k in range(4)]
    print(" ".join(row))

# 2d)
for n in range(1, 11):
    print("-" * 42)
    print(f"{n}=", end=" ")
    for i in range(1, 11):
        print(f"{n}x{i}={n*i}", end=" ")
    print()
print("-" * 42)


# Exercise 3

words=['jam', 'argue', 'elf', 'brown', 'dice', 'dingo']

# 3a) Append 'poster'
words.append('poster')

# 3b)
idx=words.index('elf') + 1
words.insert(idx, 'bin')

# 3c) 
words.reverse()

# 3d)
if 'dice' in words:
    words.remove('dice')

# 3e)
words.extend(['table', 'brave', 'cat'])

# 3f)
newWords=words[1:4]

# 3g)
print([w.upper() for w in words])

# 3h) Print list in Title Case
print([w.title() for w in words])

# 3i) 
print("Last three:", words[-3:])

print("words=", words)
print("newWords=", newWords)



# Exercise 4 
nums=[3, 7, 19, 2, 8, 3, 9, 1, 6]

# 4a) 
nums.append(4)

# 4b) 
i2=nums.index(2)
nums.insert(i2+1, 23)

# 4c) 
print("5th to 7th:", nums[4:7])

# 4d) 
nums.extend([3, 6, 9, 12])

# 4e) 
nums.reverse()

# 4f) 
if len(nums)>3:
    del nums[3]

# 4g)
nums.sort(reverse=True)

# 4h)
print("Odd numbers:", [x for x in nums if x % 2==1])

# 4i) 
print("Total=", sum(nums))
print("nums=", nums)

# Exercise 5
colours=['red','green','red','blue','yellow','pink','blue','green','blue','white']
target=input("Which item should I count?").strip().lower()
count=sum(1 for c in colours if c.lower()==target)
print(f"{target} appears {count} time(s).")

# Exercise 6
items=["apple", "banana", "cherry"]
while True:
    print("\n1.Display\n2.Add\n3.Delete\n4.Quit")
    choice=input("Choose:").strip()
    if choice == "1":
        print("Items:", items)
    elif choice=="2":
        val=input("Add what?").strip()
        if val:
            items.append(val)
            print("Added.")
    elif choice=="3":
        val=input("Delete which item?").strip()
        if val in items:
            items.remove(val)
            print("Deleted.")
        else:
            print("Not found.")
    elif choice=="4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")


# Exercise 7

import random
fruits=["apple", "banana", "mango", "orange", "kiwi", "grape"]
score=0
while True:
    idx=random.randint(0, len(fruits)-1)
    secret=fruits[idx]
    guess=input(f"Guess the fruit (index {idx}):").strip().lower()
    if guess==secret.lower():
        score+=1
        print("Correct! Score:", score)
        again=input("Play again?(y/n):").strip().lower()
        if again !="y":
            break
    else:
        print(f"Wrong.It was'{secret}'.Final score:{score}")
        break

# Exercise 8
qa = [
    ("What is 2+2?", "4"),
    ("How many days in a week?", "7"),
    ("Python keyword to end a loop?", "break"),
    ("Largest planet in our solar system?", "jupiter"),
    ("Binary of decimal 1?", "1"),
    ("Opposite of 'True' in Python?", "false"),
    ("Result of 3*3?", "9"),
    ("First month of the year?", "january"),
    ("Abbrev. for Artificial Intelligence?", "ai"),
    ("Creator of Python (first name)?", "guido"),
]

random.shuffle(qa)
score=0
for q, a in qa:
    ans=input(q + " ").strip().lower()
    if ans==a.lower():
        print("✓Correct")
        score+=1
    else:
        print(f"✗ Wrong (answer:{a})")
print(f"Your score:{score}/{len(qa)}")

