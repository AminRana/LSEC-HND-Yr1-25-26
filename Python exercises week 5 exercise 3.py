words = ['jam', 'argue', 'elf', 'brown', 'dice', 'dingo']
print(words)

words.append('poster')
print(words)

words.insert(words.index('brown'), 'bin')
print(words)

words.reverse()
print(words)

if 'dice' in words:
    words.remove('dice')
    print(words)
    
words.reverse()
print(words)

words.extend(['table', 'brave', 'cat'])
print(words)

newWords = words[1:4]
print(newWords)

print("UPPER CASE:", [w.upper() for w in words])

print("Title Case:", [w.title() for w in words])

print(words[-3:])
