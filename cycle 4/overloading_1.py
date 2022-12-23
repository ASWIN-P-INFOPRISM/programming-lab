class rectangle:

    def __init__(self):

        self.__length = int(input("Enter length : "))

        self.__width = int(input("Enter width : "))

    def find_area(self):

        self.area = self.__length * self.__width

        return self.area

    def __lt__(self,other):

        if(self.find_area() < other.find_area()):

            print(f"Area of 1st triangle is lower")

        else:

            print(f"Area of 2nd triangle is lower")

obj1 = rectangle()

print(f"Area of 1st rectangle : {obj1.find_area()}")

obj2 = rectangle()

print(f"Area of 1st rectangle : {obj2.find_area()}")

obj1 < obj2


