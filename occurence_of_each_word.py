line_of_text = input("Enter a line of text : ")

word_list = line_of_text.split(" ")

word_count = {}


#LOGIC
for word in word_list :
    if word in word_count :
        word_count[word] +=1
    else:
        word_count[word] = 1

        
print(word_count)
