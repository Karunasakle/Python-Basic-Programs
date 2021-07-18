n=int(input("enter any num for print reverse order of given num: "))
rev=0
remainder=1
for i in range(len(str(n))):
    remainder=n%10
    rev=rev*10+remainder
    n//=10
print("reverse order is",rev)