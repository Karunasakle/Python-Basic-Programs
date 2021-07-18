n=int(input("Enter num to cheak num is perfect or not: "))
temp=n
sum=0
i=1
while(i<n):
    if(n%i==0):
      print(i,end=" ")
      sum=sum+i
    i+=1 
print()
print("sum of factors is",sum)      
if(temp==sum):
    print("num is perfect")
else:
    print("num is not perfect")       
      
    
   
