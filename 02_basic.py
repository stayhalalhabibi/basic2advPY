print("salam sharif")

pass1 = input("Enter the password : ")
if pass1 == "intel":
    print("welcome to stayhalal world")
else:
    print("wrong password)")

print("done")   

# marks of the students
marks = int(input("Enter the number : "))
grade =  ""
if marks > 90:
    grade = "A+"
elif marks >  80:
    grade = " A "
elif marks >  70:
    grade = "B "
elif marks >  60:
    grade = "C "
elif marks >  50:
    grade = "D "
elif marks >  40:
    grade = "E "
else:
    grade = "F"

print(f"the studemt go the {marks} marks and {grade} grade")