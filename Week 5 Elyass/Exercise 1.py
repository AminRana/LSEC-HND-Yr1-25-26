# Exercise 1(a) – Check if each character in a string is a vowel

text = input("Enter a word or sentence: ")

for ch in text:
    if ch.lower() in ["a", "e", "i", "o", "u"]:
        print(ch, "is a vowel")
    else:
        print(ch, "is not a vowel")
