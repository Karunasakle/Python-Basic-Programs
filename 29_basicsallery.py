n=int(input("Enter basic salary: "))
if (n>0 and n<=15000):
    ta=(100*8)/n
    da=(100*4)/n
    gs=n+ta+da
    print("gross salary is ",gs)
elif(n>15000):
    ta=(100*10)/n
    da=(100*5)/n
    gs=n+ta+da  
    print("gross salary is ",gs) 
else:
    print("sorry! only accept positive value")    
   
