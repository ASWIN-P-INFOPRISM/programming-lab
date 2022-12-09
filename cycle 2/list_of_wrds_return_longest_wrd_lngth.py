words = input("Enter words seperated by space : ")

words = words.split(" ")

words_dict = {}

for word in words :

    words_dict[word] = len(word)

v = list(words_dict.values())
 
# taking list of car keys in v
k = list(words_dict.keys())
 
print((k[v.index(max(v))])," = ",max(v))
    
