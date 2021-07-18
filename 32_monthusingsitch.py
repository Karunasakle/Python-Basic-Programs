def month(num): 
    switcher={
        1 : "January",
        2 : "Feburary",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December",
    }
    return switcher.get(num)
num= int(input("Enter num betwen 1 to 12 for finding Month name: "))
print(num,' month is a '+month(num))    