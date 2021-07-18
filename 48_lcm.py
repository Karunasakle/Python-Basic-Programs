num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
if(num1 > num2):
    max= num1
else:
    max= num2
while(True):
    if(max % num1 == 0 and max % num2 == 0):
        print("LCM is",max)
        break;
    max=max+1    


