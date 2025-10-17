# String in Python

# 1 store the string in a variable named col

col = "Regent college London"
print(col[0:6])
print(col[0],col[7],col[15])
print(col[7:14])
print(col[2:6]+col[10:12])
print(col[-3:])
print(col[0:6],col[15:21])

# 2 Functions with string in Python

col = " regent college London "
col2 = col.strip()
col2 = col2.lower()
print(col2)

col = " regent college London "
col2 = col.strip()
col2 = col2.title()
print(col2)

col2 = col2.upper()
print(col2)

col2 =col2.lower()
position = col2.find("college")
print(position)

