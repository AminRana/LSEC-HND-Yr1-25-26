# program to calculate simple interset

# Get input from user
principal = float(input("Enter the capital amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the number of years: "))

# Calculate interest
interest = (principal * rate * time) / 100

# Display the result
print(f"The total interest after {time} years is: {interest:.2f}")
