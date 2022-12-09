def all_factors(num):

    print(f"All factors of {num} are : ",end=" ")

    for i in range(1,num+1):

        if(num%i == 0):

            print(i,end=" ")

num = int(input("Input a number : "))

all_factors(num)

