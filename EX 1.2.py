# Program to check if a number is prime or not.#

num = int(input("Enter a number: "))

# 1 and numbers less than 1 are not prime

if num <= 1:
    print(num, "is not a prime number.")
else:
    is_prime = True # assume it is prime.

    #check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break # no need to check further


    # print result
    if is_prime:
        print(num, "is a prime number.")

    else:
        print(num, "is not a prime number.")


# Program to display all prime numbers up to a certain number.

limit = int(input("Enter the upper limit: "))

print("Prime number up to", limit, "are:")

for num in range(2, limit + 1): # numbers from 2 to limit
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


# program to display multiplication table for a given number.

num = int(input("Enter a number: "))

print("\nMultiplication Table for", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
