eng=int(input("Enter English marks: "))
hindi=int(input("Enter Hindi marks: "))
maths=int(input("Enter Maths marks: "))
science=int(input("Enter Science marks: "))
socials=int(input("Enter Social Sceince marks: "))
total=eng+hindi+maths+science+socials
print("Total marks: ",total)
per=total*100/500
print("percentage: ",per)
if (per>=60 and per<=100):
    print("Grade A")
elif(per>=50 and per<=60):
    print("Grade B")
elif(per>=40 and per<=50):
    print("Grade C")
elif(per>=35 and per<=40):
    print("Grade D")
else:
    print("sorry!! you are fail.")    

