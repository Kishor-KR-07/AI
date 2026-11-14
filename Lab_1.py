name=input("Enter Student name: ")
n=int(input("Enter number of subjects: "))
total=0
for i in range(1,n+1):
    marks=int(input(f"Enter marks of subject {i}: "))
    total+=marks
per=total/n
if per>=90:
    grade='A+'
    performance='Outstanding'
elif per>=80:
    grade='A'
    performance='Excellent'
elif per>=70:
    grade='B'
    performance='Very Good'
elif per>=60:
    grade='C'
    performance='Good'
elif per>=50:
    grade='D'
    performance='Average'
else:
    grade='F'
    performance='Needs improvement'
print("\n--Academic Performance--")
print("Student name :",name)
print("Total marks :",total)
print("Percentage :",per)
print("Grade :",grade)
print("Performance :",performance)