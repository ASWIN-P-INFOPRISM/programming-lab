word = input("enter a word : ")

#word[0], word[len(word)-1] = word[len(word)-1] , word[0]

start = word[0]

end = word[-1]

word = end+word[1:-1]+start 



#word[0].replace(word[0],word[len(word)-1])

print("after replacing first and last character : ",word)
