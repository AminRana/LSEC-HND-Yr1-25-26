for i in range(1,7):
    print(f"{i} = {i}, {i**2}, {i**3}, {i**4}")

    
num = 1
for row in range (5):
    for col in range (10):
        print(num, end=" ")
        num +=1
    print()
    

for i in range(0, 101, 10):
    for j in range(i, i + 4):
        if j <= 100:
            print(j, end=" ")
    print()        

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i}*{j}={i*j}", end="\t")
        print()
