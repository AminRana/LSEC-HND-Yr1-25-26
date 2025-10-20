col = "   regent college London   "

# a) Remove leading and trailing whitespaces
col2 = col.strip()
print(col2)

# b) Convert lowercase of col2
print(col2.lower())

# c) Convert title case of col2
print(col2.title())

# d) Convert upper case of col2
print(col2.upper())

# e) Find "college" word in col2
print(col2.find("college"))

# f) Replace "college" by "university" in col2
print(col2.replace("college", "university"))

# g) Check if col2 is alphabetic
print(col2.isalpha())
