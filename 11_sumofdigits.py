n=int(input("enter no to find sum of digit: "))
sum=0
for i in range(len(str(n))):
    num=n%10
    sum=sum+num
    n//=10
print(" sum of digit",sum)    