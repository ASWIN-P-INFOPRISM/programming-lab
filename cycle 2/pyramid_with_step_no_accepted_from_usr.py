def pyramid():

    step_no = int(input("Enter step number : "))

    for i in range(1,step_no):

        j = 1
        while j<=i :
            print(pow(i,j),end=" ")
            j+=1
        print("\n")


pyramid()
