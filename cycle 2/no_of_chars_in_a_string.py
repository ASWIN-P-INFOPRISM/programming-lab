def character_frequency():

    text = input("Enter string : ")

    chars = list(text)

    print(chars)

    char_frequency = {}

    for char in chars :

        if char in char_frequency :

            char_frequency[char] += 1

        else:

            char_frequency[char] = 1

    print(char_frequency)

character_frequency()
     
