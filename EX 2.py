# (A) outer loop for numbers 1 to 6
for i in range(1, 7):
    powers = []
    for j in range(1, 5):
        powers.append(i ** j)
    print(f"{i} = {', '.join(map(str, powers))}")
    
# (B)print numbers from 1 to 50.
total_numbers = 50

numbers_per_line = 10

for line in range(0, total_numbers, numbers_per_line):
    # loop through numbers in a line
    for num in range(line + 1,line + numbers_per_line + 1):
        print(num, end=' ')
    print() # move to next line

# (c) loop through starting numbers of each row.
for start in range(0, 101, 10):
    #loop through 4 numbers in each row.
    for i in range(4):
        if start + i > 100:
            break
        print(start + i, end=' ')
    print() #move to the next row.

# (D) outer loop for numbers 1 to 10

for i in range(1, 11):
    print(f"{i}=", end=' ')
    # Inner loop for multiplying i by 1 to 10
    for j in range(1, 11):
        print(f"{i}×{j}={i*j}", end=' ')
    print() 

