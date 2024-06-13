# Conditional Statements in Python
# Conditional statements are used to perform different actions based on different conditions.

# Python supports the following conditional statements:
""" 
1. if statement: An if statement consists of a boolean expression followed by one or more statements.

2. if...else statement: An if statement can be followed by an optional else statement, which executes when the boolean expression is false.

3. if...elif...else statement: An if statement can be followed by an optional elif statement and another if statement, which is executed when the boolean expression is true.

4. Nested if statement: You can use one if or else if statement inside another if or else if statement(s).

5. Single statement suites: If the suite of an if clause consists only of a single line, it may go on the same line as the header statement.

6. Short Hand If: If you have only one statement to execute, you can put it on the same line as the if statement.

7. Short Hand If...Else: If you have only one statement to execute, one for if, and one for else, you can put it all on the same line.

8. Pass Statement: if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

9. The assert statement: The assert statement is used to continue the execution if the given condition is True. If the condition is False, it raises an AssertionError exception with an optional error message.

10. The return statement: The return statement is used to exit a function and go back to the caller. It can also be used to return a value from a function.

11. The break statement: The break statement is used to exit a loop prematurely. When the break statement is encountered inside a loop, the loop is terminated immediately, and the program control resumes at the next statement following the loop.

Syntax of conditional statements in Python

if - elif - else (syntax)

        if condition: # if the condition is true then the block of code inside the if statement will be executed.
            # block of code  
        elif condition:  # if the condition is true then the block of code inside the elif statement will be executed.
            # block of code
        else:           # if the condition is false then the block of code inside the else statement will be executed.
            # block of code   

        
"""

age = input("Enter your age: ")
age = int(age)

if (age >= 18):
    print("You are eligible to vote and may apply for a driving license.")
    print("can drive")
elif(age >= 16):
    print("You are eligible to apply for a driving license.")
    print("cannot drive")
else:
    print("You are not eligible to vote or apply for a driving license.")
    print("cannot drive")

# what is the differnce between if and elif?
# if the condition is true then the block of code inside the if statement will be executed.
# if the condition is false  then only  the block of code inside the elif statement will be executed.
# if the condition is false then the block of code inside the else statement will be executed.

# Indentation in Python
# Python uses indentation to define a block of code. A block of code starts with indentation and ends with the first unindented line. The amount of indentation is up to you, but it must be consistent throughout that block.
