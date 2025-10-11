# - Kelly (70311205) - #

import math

def e1():
    number1 = float(input("Type 1st number: "))
    number2 = float(input("Type 2nd number: "))

    total = number1 + number2
    multiplied = number1 * number2

    print(f"Total of two numbers is {total : .2f}")
    print(f"Multiplication of two numbers is {multiplied : .2f}")

def e2():
    radius = float(input("Type radius of the cylinder: "))
    height = float(input("Type height of the cylinder: "))

    volume = math.pi * (radius**2) * height

    print(f"Volume of of the cylinder is {volume : .2f}")

def e3():
    capital = float(input("Type amount of your capital: "))
    rate = float(input("Type yearly interest rate: "))
    num = int(input("Type number of years: "))

    interest = (capital * rate * num) / 100

    print(f"Total interest: {interest : .2f}")

def e4():
    name = input("Type your name: ")
    age = float(input("Type your age in years: "))
    age_in_days = int(age * 365)

    print(f"{name}'s is {age_in_days} days old")

def e5():
    base = float(input("Type any number or base: "))
    expon = int(input("Type any integer number as power: "))
    power = base**expon

    print(f"{base} to the power of {expon} is {power : .2f}")

def e6():
    number = int(input("Type any number as dividend: "))
    divider = int(input("Type any number as divider: "))

    remainder = number // divider

    print(f"{remainder} is the remainder dividing {number} by {divider}")

def e7():
    name = input("Type your name: ")
    age = input("Type your age: ")
    friend_name = input("Type your friend's name: ")
    friend_age = input("Type your friend's age: ")
    print(f"{name}'s age is {age}")
    print(f"{friend_name}'s age is {friend_age}")

def run():
    print("E1:")
    e1()
    print("----------")
    print("E2:")
    e2()
    print("----------")
    print("E3:")
    e3()
    print("----------")
    print("E4:")
    e4()
    print("----------")
    print("E5:")
    e5()
    print("----------")
    print("E6:")
    e6()
    print("----------")

run()

# - Kelly (70311205) - #