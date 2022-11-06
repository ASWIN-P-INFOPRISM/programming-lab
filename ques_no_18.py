clr1 = input("enter name of colours for list 1 : ")
clr2 = input("enter name of colours for list 2 : ")

clr1 = clr1.split(" ")
clr2 = clr2.split(" ")

clr3 = set(clr1).difference(clr2)



print("colours not in list 2  : ")
print(clr3)