lst, positiveList = list(), []

lst = input("Enter integers to list with each element seperated by commas : ")

lst = lst.split(" ")
lst = list(map(int,lst))
for element in lst :
    if(element>0):
        positiveList.append(element)

print(f"positive integers = {positiveList}")
