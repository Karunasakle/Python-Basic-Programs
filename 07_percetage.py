M=int(input("Enter marks of maths: "))
C=int(input("Enter marks of Chemistry: "))
P=int(input("Enter marks of physics: "))
H=int(input("Enter marks of hindi: "))
E=int(input("Enter marks of english: "))
sum = (M+C+P+H+E)
print("The total sum of all marks is: ",sum)
percentage=(sum/500)*100
print("The percentage is:",percentage,"%")