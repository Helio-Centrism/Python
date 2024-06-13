# Nesting in Conditional Statements
# Nesting means putting one conditional statement inside another conditional statement.

# Example 1: Nesting of if...elif...else statement

age = input("Enter your age: ")
age = int(age)

if (age >= 18):
    print("You are eligible to vote and may apply for a driving license.")
    if (age >= 21):
        print("You can also drink alcohol.")
    else:
        print("You cannot drink alcohol.")
        #here the inner if statement is executed only if the outer if statement is true.
elif(age >= 16):
    print("You are eligible to apply for a driving license.")
    print("cannot drive")
else:
    print("You are not eligible to vote or apply for a driving license.")
    print("cannot drive")
# In the above example, the if statement is nested inside the elif statement. If the condition of the outer if statement is true, then the inner if statement will be executed. If the condition of the outer if statement is false, then the elif statement will be executed.
