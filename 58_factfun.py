def fact_find(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
    return fact

n=int(input("Enter num: "))
fact_find(n) 
print("outside factorial of num is ",fact_find(n))               