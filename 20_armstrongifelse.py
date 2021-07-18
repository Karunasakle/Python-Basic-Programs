n=int(input("Enter no to cheak no is armstrong or not: "))
temp=n
res=1
sum=0
while(n>0):
    digit=n%10
    res=digit**3
    sum=res+sum
    n=n//10
if(sum==temp):
    print("number is armstrong")
else:
    print("number is not armstrong") 
