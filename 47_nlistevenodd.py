listA = []
# Input number of elemetns
n = int(input("Enter number of elements in the list : "))
# Enter elements separated by comma
listA = list(map(int,input("Enter the numbers : ").strip().split(',')))[:n]
print("The entered list is: \n",listA)
even_count=0
odd_count=0
for n in listA:
    if(n%2==0):
        even_count+=1
    else:
        odd_count+=1
print("Even numbers in the list: ",even_count)
print("Odd numbers in the list: ",odd_count)            
