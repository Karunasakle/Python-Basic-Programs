n=int(input("Enter any num to cheak given no is armstrong or not: "))
sum=0
temp=n
while(n>0):
     r=n%10
     sum=sum+(r*r*r)
     n//=10
if(temp==sum):
    print("num is armstrong")
else:
    print("num is not armstrong")        