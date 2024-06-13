# grade student bsed on marks
marks = int(input("Enter the marks: "))
if (marks >= 90):
    grade = "Grade A"
elif (marks >= 80 and marks < 90):
    grade = "Grade B"
elif (marks >= 70 and marks < 80):
    grade = "Grade C"
elif (marks >= 60 and marks < 70):
    grade = "Grade D"
else:
    grade = "Grade F"
print("Grade is ", grade)
