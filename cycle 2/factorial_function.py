def factorial(num):
    factorial = 1
    for i in range(1,num+1) :
        factorial *= i
    return factorial



num = int(input("Enter a number : "))
factorial = factorial(num)
print(f"factorial is {factorial}")
