# Initial list
words = ['jam', 'argue', 'elf', 'brown', 'dice', 'dingo']

# a) Add the word 'poster' to the end of the list.
words.append('poster')
print("a)", words)


# b) Add the word ‘bin’ between 'elf' and 'brown'
index_brown = words.index('brown')  # Find index of 'brown'
words.insert(index_brown, 'bin')
print("b)", words)

# c) Reverse the order of the list
words.reverse()
print("c)", words)

# d) Remove the word ‘dice’
words.remove('dice')
print("d)", words)

# e) Add the list ['table', 'brave', 'cat'] to the list of words
words.extend(['table', 'brave', 'cat'])
print("e)", words)

# f) Create a new list called newWords to hold 2nd, 3rd and 4th items of words list
newWords = words[1:4]
print("f)", newWords)

# g) Print out words list in UPPER CASE
upper_words = [w.upper() for w in words]
print("g)", upper_words)

# h) Print out words list in Title CASE
title_words = [w.title() for w in words]
print("h)", title_words)

# i) Print out last three items from the words list
last_three = words[-3:]
print("i)", last_three)
