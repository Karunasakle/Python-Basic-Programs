n=int(input("Enter Three digit num to find beggest digit: "))
f=n//100
print("first digit is ",f)
m=(n//10)%10
print("second digit is ",m)
l=(n%10)%10
print("third digit is ",l)
if (f>m)and(f>l):
    print("First digit is greater")
elif(m>l)and(m>f):
    print("Second digit is greater")
else:
    print("Third digit is greater")        