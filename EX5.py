# Sample colours list
colours = ['red', 'green', 'red', 'blue', 'yellow', 'pink', 'blue', 'green', 'blue', 'white']

# Ask user for input
item = input("Enter the colour to count: ").lower()  # convert to lowercase for consistency
count = colours.count(item)
print(f"The colour '{item}' appears {count} time(s) in the list.")
