lst = [1,2,3,4,5,6,7,8,9,10]

lst2 = [element for element in lst if element%2 == 0]\

lst3 = [element for element in lst if element>5]

lst4 = [element*element for element in lst] 

print(f"even numbers in the list : {lst2}")
print(f"numbers greater than 5 : {lst3}")
print(f"Squares of elements in list : {lst4}")

word = input("Enter a word : ")

wordList = list(word)

vowels = ['a','e','i','o','u']

vowelsFromWord = [element for element in word if element in vowels]

print(vowelsFromWord)

ordValues = [ord(element) for element in wordList]

print(ordValues)
