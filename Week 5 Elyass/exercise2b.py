# Exercise 2(b) – print 1 to 50 in 5 rows

num = 1
for row in range(5):
    for col in range(10):
        print(num, end=" ")
        num += 1
    print()
