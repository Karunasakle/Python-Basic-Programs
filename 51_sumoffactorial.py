n=int(input("enter num: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact,end=" ")
print("fact of",n,"is",fact)    