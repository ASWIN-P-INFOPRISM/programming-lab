
lst1 , lst2, lst3 = list(),[], []
lst1 = input("Enter elements to list 1 : ")
lst2 = input("Enter elements to list 2 : ")

lst1 = lst1.split(" ")
lst2 = lst2.split(" ")

if(len(lst1) == len(lst2)):
    print(f"\nBoth list have a length of {len(lst1)}.")
else:
    print("\nBoth list have different lengths.")

lst1 = list(map(int,lst1))
lst2 = list(map(int,lst2))

sum1 = sum(lst1)
sum2 = sum(lst2)

print(f"sum of elements of list 1 : {sum1}")
print(f"sum of elements of list 2 : {sum2}")

for i in lst1 :
    for j in lst2 :
        if(i == j):
            lst3.append(i)

if(len(lst3)):
    print(f"Same elements in both list are {lst3}")
else:
    print("no elements are repeating")
            

