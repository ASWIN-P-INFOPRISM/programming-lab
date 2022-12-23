class rectangle:

    def __init__(self,a,b):

        self.length = a
        self.breadth = b

    def area(self):

        return self.length*self.breadth

    def perimeter(self):

        return 2*(self.length + self.breadth)


len1 = int(input("Enter length of 1st rectangle : "))

bre1 = int(input("Enter breadth of 1str rectangle : "))

len2 = int(input("Enter length of 2nd rectangle : "))

bre2 = int(input("Enter breadth of 2nd rectangle : "))

rec1 = rectangle(len1,bre1)

rec2 = rectangle(len2,bre2)

area1 = rec1.area()

perimeter1 = rec1.perimeter()

area2 = rec2.area()

perimeter2 = rec2.perimeter()

print("\n\nArea of 1st triangle : ",area1)

print("Perimeter of 1st triangle : ",perimeter1)

print("Area of 2nd triangle : ",area2)

print("Perimeter of 2nd triangle : ",perimeter2)

if(area1 > area2):
    print(f"Area of Triangle 1 is greater")
else:
    print(f"Area of Triangle 2 is greater")
