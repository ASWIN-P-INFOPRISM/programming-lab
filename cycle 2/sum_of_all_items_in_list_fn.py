
def listSum(numbers) :
    sum = 0
    for element in numbers :
        sum += element
    print(f"sum of all elements in the list : {sum}")

numbers = input("enter numbers with each element seperated by space : ").split()
numbers = list(map(int,numbers))
listSum(numbers)
    
