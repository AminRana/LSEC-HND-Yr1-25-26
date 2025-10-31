# Testing lower case and upper cases

col = " regent college London "


col2 = col.strip()
print("a)", col2)

 
print("b)", col2.lower())


print("c)", col2.title())



print("d)", col2.upper())

print("e)", col2.find("college"))

print("f)", col2.replace("college", "university"))

print("g)", col2.isalpha())
