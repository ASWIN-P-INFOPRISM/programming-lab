wrd1 = input("Enter a word : ")
wrd2 = input("Enter another word : ")

new_word = wrd1.replace(wrd1[0],wrd2[0])+" "+wrd2.replace(wrd2[0],wrd1[0])

print("After swapping first character of both word : ",new_word)