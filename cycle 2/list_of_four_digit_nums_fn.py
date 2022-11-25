from math import sqrt

def digits_are_even(digits):
    for digit in digits:
        if(digit%2 != 0):
            return False
    return True


def perfect_square(num):
    sr = int(sqrt(num))
    return sr*sr == num


def generate_lst(start,end):
        
    lst = []

    for i in range(start,end+1):

        digits = str(i)

        digits = list(digits)

        digits = list(map(int,digits))

        if(digits_are_even(digits)):

            if(perfect_square(i)):

                lst.append(i)

    return lst

def check_four_digit(start,end):
    
    if(len(str(start)) != 4 or len(str(end)) != 4):

        return False

    else:
        
        return True
    


start = int(input("Enter starting four digit number : "))

end = int(input("Enter ending four digit number : "))

if(check_four_digit(start,end)):

    lst = generate_lst(start,end)

    print(lst)

else:

    print("Invalid Input")

        
