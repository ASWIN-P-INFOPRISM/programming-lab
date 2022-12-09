def star_pattern(num):

    for i in range(1,num+1):

        for j in range(i) :

            print("*",end=" ")

        print(end="\n")


    for i in range(num-1,0,-1):

        for j in range(i):

            print("*",end=" ")

        print(end="\n")

num = int(input("Input a number : "))

star_pattern(num)

