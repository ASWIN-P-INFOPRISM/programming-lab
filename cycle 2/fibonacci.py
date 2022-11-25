def fibonacci(num):
    pre = 0
    current = 1
    print(f"fibonacci series of {num} : ")
    for i in range(num):
        print(pre)
        nth = pre+current
        pre = current
        current = nth
        




num = int(input("Enter a number : "))
fibonacci(num)
