def test_prime(n):
    for i in range(2,n):
        if(n % i == 0):
            print("num is not prime")
            break;
    else:
        print("num is prime")
n=int(input("Enter num to cheak prime or not: ")) 
test_prime(n)                   
    