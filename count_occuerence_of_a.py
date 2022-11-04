lst_of_name = input("Enter names : ")

occuerence_of_a = {'a':0}

lst_of_name = lst_of_name.split(" ")

for name in lst_of_name :
    name = list(name)
    for letter in name :
        if(letter == 'a'):
            occuerence_of_a[letter] +=1
print("\n\n\n",occuerence_of_a)
