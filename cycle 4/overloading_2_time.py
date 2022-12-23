class time:

    def __init__(self):

        self.__hour = int(input("Enter hour : "))
        self.__minute = int(input("Enter minute : "))
        self.__second = int(input("Enter second : "))

        print(f"You have entered : {self.__hour}hours {self.__minute}minutes {self.__second}seconds")

    def __add__(self,other):

        sum_hour = self.__hour + other.__hour
        sum_minute = self.__minute + other.__minute
        sum_second = self.__second + other.__second

        if(sum_second > 60):

            sum_minute = sum_minute + (sum_second // 60)
            sum_second = sum_second % 60

        if(sum_minute > 60):

            sum_hour = sum_hour + (sum_minute // 60)
            sum_minute = sum_minute % 60

        if(sum_hour > 24):

            sum_hour = sum_hour // 24

            sum_hour = sum_hour + (sum_hour % 24)

        print(f"{sum_hour}hours {sum_minute}minutes {sum_second}seconds")


t1 = time()

t2 = time()

t1 + t2

        
            
            
