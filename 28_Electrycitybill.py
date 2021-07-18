unitf=int(input("Enter first month unit: "))
unitl=int(input("Enter last month unit: "))
tunit=unitl-unitf
print("total units is ",tunit)
if(tunit<=150):
    bill=tunit*4
    print("Electricity bill charges is 4rs/unit is ",bill)
elif(tunit>=151 and tunit<=300):
    bill=tunit*6
    print("Electricity bill charges 6rs/unit is ",bill)
elif(tunit>=301 and tunit<=500):
    bill=tunit*8
    print("Electricity billcharges 8rs/unit is ",bill)
elif(tunit>500):
     bill=tunit*10
     print("Electricity billcharges 10rs/unit is ",bill)
else:
    print("you entered zero units.")
