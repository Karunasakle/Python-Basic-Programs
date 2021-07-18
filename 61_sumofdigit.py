def sum_ofdigit(num):
    sum=0
    rem=1
    while(num>0):
       rem=num%10
       sum=sum+rem
       num//=10
    print(sum)
    return sum
num=int(input("Enter no: "))
sum_ofdigit(num)    
sum_ofdigit(num)
    