day=int(input("Enter Day(dd):"))
month=int(input("Enter Month(mm):"))
year=int(input("Enter Year(yyyy):"))

def function(month,year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        max_days1 = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days1 = 30
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        max_days1 = 29
    else:
        max_days1 = 28
    return max_days1

while True:
    max_days=function(month,year)
    if (day>0 and day<=max_days) and (month>0 and month<13):
        dd = str(day)
        mm = str(month)
        yyyy = str(year)
        if month < 10:
            mm = "0" + mm
        if day < 10:
            dd = "0" + dd
        given_date = dd + mm + yyyy
        reverse_date = given_date[::-1]
        if given_date == reverse_date:
            print(day,"/",month,"/",year,"date,is palindrome")
            break
        else:
            day=day+1
            if day>max_days:
                day=1
                month=month+1
                if month>12:
                    month=1
                    year=year+1

