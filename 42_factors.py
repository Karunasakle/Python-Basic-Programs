n=int(input("Enter num for find factors of given num: "))
i=1
while(i<=n):
    if(n%i==0):
      print(i,end=" ")
    i+=1
   