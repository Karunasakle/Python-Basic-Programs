n=int(input("Enter four digit value to find reverse value: "))
remainder=1
rev=0
for i in range(len(str(n))):
   remainder=n%10
   rev=(rev*10)+remainder
   n=n//10
print("Reverse order of ",n,"is",rev)  