def febonacci(n):
    a=0
    b=1
    sum=0
    count=1
    print("Fibonacci series: ",end=" ")
    while(count<=n):
        print(sum,end=" ")
        count=count+1
        a=b
        b=sum
        sum=a+b
n=int(input("Enter the value for print fabonacci series: "))   
febonacci(n)