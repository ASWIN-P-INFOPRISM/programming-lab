lst = [1,2,3,4,5,6,7,8,9,10,-1,-33,-45,-9,-54]

positive_list = [element for element in lst if element>0]

square_of_nums = [element*element for element in lst] 

print(f"Positive list of numbers : {positive_list}")
print(f"Squares of elements in list : {square_of_nums}")

word = input("Enter a word : ")

wordList = list(word)

vowels = ['a','e','i','o','u']

vowelsFromWord = [element for element in word if element in vowels]

print(vowelsFromWord)

ordValues = [ord(element) for element in wordList]

print(ordValues)
