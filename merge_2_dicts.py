dict1 = {}
dict2 ={}
dict3 = {}

n = int(input("Enter number of items for the dictonary : "))

for i in range(n) :
    key = input("enter key : ")
    value = int(input("enter value : "))
    dict1[key] = value

print("\n\n")

for i in range(n) :
    key = input("enter key : ")
    value = int(input("enter value : "))
    dict2[key] = value

print("\n\n")

dict3 = {**dict1,**dict2}

for k,v in dict3.items() :
    if k in dict1 and k in dict2 :
        dict3[k] = [v,dict1[k]]


print("After merging : ",dict3)
