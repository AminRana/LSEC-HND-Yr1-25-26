# Kelly Scott - 70311205

def a():
    for i in range(1,7):
        squares = []
        for j in range(1,5):
            squares.append(i**j)
        print(f"{i} = {squares[0]},{squares[1]},{squares[2]},{squares[3]}")

def b():
    count = 1
    for i in range(1, 6):
        numbers = []
        for i in range(10):
            numbers.append(count)
            count += 1
        print(numbers)

def c():
    count = 0
    for i in range(1,12):
        numbers = []
        for i in range(4):
            if count > 100:
                break
            numbers.append(count)
            count += 1
        count += 6
        print(numbers)

def d():
    for i in range(1, 11):
        mults = ""
        for j in range(1, 11):
            mults += f"{i}x{j} = {i*j} "
        print(mults)

d()

# Kelly Scott - 70311205