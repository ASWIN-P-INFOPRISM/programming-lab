word = input("Enter a word : ")

word = list(word)

print(word[0])

for i in range(1,len(word)) :
    if(word[0] == word[i]):
        word[i] = "$"


word = ''.join(word)

print(word)
