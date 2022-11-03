from datetime import date

start_year = date.today().year

end_year = int(input("Enter the last year : "))

print(f"Leap years between {start_year} and {end_year} : \n")

for year in range(start_year,end_year) :

    if (year % 4 == 0) and (year % 100 != 0) :

        print(year,"\n")

    elif (year % 400 == 0):

        print(year,"\n")
