def switch(day):
    week={
        1 : "Monday",
        2 : "Tuesday",
        3 : "Wednesday",
        4 : "Thursday",
        5 : "Friday",
        6 : "Saturday",
        7 : "Sunday"
    }
    return week.get(day)  
day=int(input("enter num to find days: "))
print(switch(day))