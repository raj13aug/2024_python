letters = ["a","b","c","d"]

#add
letters.append('z')
letters.insert(0,"q")

print(letters)

#remove
letters.pop()
letters.remove("b")
del letters[0:1]

print(letters)


letters.clear()

print(letters)