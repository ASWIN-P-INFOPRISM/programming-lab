nums = input("Enter integers seperated by space : ")

int_list = nums.split(" ")

int_list = list(map(int,int_list))

even_list = [element for element in int_list if element%2 != 0]

print("list of numbers that are not even : ",even_list)


