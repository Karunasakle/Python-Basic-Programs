n=int(input("Enter no to cheak no is palindrome or not: "))
temp=n
rev=0
while(n!=0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if(rev==temp):
    print("number is palinfrome")
else:
    print("number is not palindrome")        