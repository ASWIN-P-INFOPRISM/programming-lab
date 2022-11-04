input_from_user = input("Enter integers seperated by white space : ")

lst = input_from_user.split(" ")

lst = list(map(int,lst))

lst = ["over" if element > 100  else element for element in lst]

print(lst)

