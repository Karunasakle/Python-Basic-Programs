num=int(input("Enter num to cheak num is prime or not: "))
for i in range(2,num):
    if num%i==0:
        print(num,"is not prime number.")
        break;
else:
    print(num,"is prime number")   
