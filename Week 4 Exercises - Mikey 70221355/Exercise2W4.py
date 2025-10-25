# Mikey Talbot (70221355)

#Exercise 2: Store regent college London into col string variable like below and answer the
#questions and/or write syntax for questions (a) to (f) col= regent college London.

col = "regent college London"
#a) Remove leading and trailing whitespaces from string col and store it as a new string, col2:
print("")
col2 = (col.strip())
print(col2)
print("")
#b) Convert lowercase of col2:
print("")
print(col2.lower())
print(col2)
print("")
#c) Convert title case of col2:
print("")
print(col2.title())
print("")
#d) Convert upper case of col2:
print("")
print(col2.upper())
print("")
#e) Find college word into col2:
print("")
print(col2.find('college'))
print("")
#f) Replace college by university into col2:
print("")
print(col2.replace('col', 'university:'))
print("")
#g)Check col2 isalpha() to see it is a string of characters or not:
print("")
print(col2.isalpha())
print("")