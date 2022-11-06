def gcd_fn(num1, num2) :
    print(num1,num2)
    if(num2 == 0):
        return num1
    else:
        return gcd_fn(num2,num1%num2)

num1 = int(input("Enter num1 : "))

num2 = int(input("Enter num2 : "))

gcd_num = gcd_fn(num1, num2)
print(gcd_num)