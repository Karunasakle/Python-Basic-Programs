n=int(input("enter any no to cheak given no is palindrome or not: "))
temp=n
sum=0
while(n>0):
     r=n%10    
     sum=(sum*10)+r   
     n=n//10
if(temp==sum):
    print("num is palindrome")
else:
    print("num is not palindrome")    