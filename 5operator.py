""" Operators in Python 
Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.
For example:
>>> 2 + 3

Here, + is the operator that performs addition. 2 and 3 are the operands and 5 is the output of the operation.
Types of Operators

Python language supports the following types of operators.
    
        Arithmetic Operators
        Comparison (Relational) Operators
        Assignment Operators
        Logical Operators
        Bitwise Operators
        Membership Operators
        Identity Operators
Let us discuss them one by one.
Arithmetic Operators
Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.
Operator	Meaning	Example
+	Addition	Adds values on either side of the operator.	a + b = 30
-	Subtraction	Subtracts right hand operand from left hand operand.	a – b = -10
*	Multiplication	Multiplies values on either side of the operator	a * b = 200
/	Division	Divides left hand operand by right hand operand	b / a = 2
%	Modulus	Divides left hand operand by right hand operand and returns remainder	b % a = 0
**	Exponent	Performs exponential (power) calculation on operators	a**b =10 to the power 20
//	Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed.	9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0

Comparison Operators
Comparison operators are used to compare values. It returns either True or False according to the condition.
Operator	Meaning	Example
==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
!=	If values of two operands are not equal, then the condition becomes true.	(a != b) is true.
>	If the value of the left operand is greater than the value of the right operand, then the condition becomes true.	(a > b) is not true.
<	If the value of the left operand is less than the value of the right operand, then the condition becomes true.	(a < b) is true.
>=	If the value of the left operand is greater than or equal to the value of the right operand, then the condition becomes true.	(a >= b) is not true.
<=	If the value of the left operand is less than or equal to the value of the right operand, then the condition becomes true.	(a <= b) is true.

Assignment Operators
Assignment operators are used in Python to assign values to variables.
a = 5 is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.
There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same. It is equivalent to a = a + 5.
Operator	Example	Equivalent to
=	a = 5	a = 5
+=	a += 5	a = a + 5
-=	a -= 5	a = a - 5
*=	a *= 5	a = a * 5
/=	a /= 5	a = a / 5
%=	a %= 5	a = a % 5
//=	a //= 5	a = a // 5
**=	a **= 5	a = a ** 5
&=	a &= 5	a = a & 5
|=	a |= 5	a = a | 5
^=	a ^= 5	a = a ^ 5
>>=	a >>= 5	a = a >> 5
<<=	a <<= 5	a = a << 5

Logical Operators
Logical operators are the and, or, not operators.
Operator	Meaning	Example
and	True if both the operands are true	x and y
or	True if either of the operands is true	x or y
not	True if operand is false (complements the operand)	not x

Bitwise Operators
Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.
For example, 2 is 10 in binary and 7 is 111.
In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)
Operator	Meaning	Example
&	Bitwise AND	x & y = 0 (0000 0000)
|	Bitwise OR	x | y = 14 (0000 1110)
~	Bitwise NOT	~x = -11 (1111 0101)
^	Bitwise XOR	x ^ y = 14 (0000 1110)
>>	Bitwise right shift	x>> 2 = 2 (0000 0010)
<<	Bitwise left shift	x<< 2 = 40 (0010 1000)

Membership Operators
Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples. There are two membership operators as explained below:

Operator	Meaning	Example
in	True if value is found in the sequence	5 in x, here 5 is in the sequence of x
not in	True if value is not found in the sequence	5 not in x, here 5 is not in the sequence of x

Identity Operators
Identity operators compare the memory locations of two objects. There are two Identity operators explained below:

Operator	Meaning	Example
is	True if the operands are identical (refer to the same object)	x is True
is not	True if the operands are not identical (do not refer to the same object)	x is not True

Precedence and Associativity of Operators
The precedence of operators determines the order they are applied when evaluating an expression. Operators with higher precedence are applied first.
Associativity defines the order in which operators of the same precedence are applied.
For example, the expression 5 + 7 * 3 is calculated as 5 + (7 * 3) because the * operator has higher precedence than the + operator.
The associativity of the + and * operators is left-to-right, so the * operator is applied first.
The precedence and associativity of operators in Python are listed in the following table.
Category	Operator	Associativity
Postfix	() [] .	Left to right
Unary	+ - ~	Right to left
Arithmetic	**	Right to left
Multiplication * / % //	Left to right
Addition + -	Left to right
Shift	>> <<	Left to right
Bitwise AND	&	Left to right
Bitwise OR	|	Left to right
Comparison	< <= > >=	Left to right
Equality	== !=	Left to right
Logical AND	and	Left to right
Logical OR	or	Left to right
Conditional	 if else	Right to left
Assignment	= += -= *= /= %= //= **= &= |= ^= >>= <<=	Right to left
Comma	,	Left to right
This table lists the precedence and associativity of all the operators in Python.


"""

# Arithmetic Operators
a = 2
b = 3

sum = a + b
diff = a - b
product = a * b
division = a / b
modulus = a % b
exponent = a ** b

print("sum is ", sum)
print("difference is ", diff)
print("product is ", product)
print("division is ", division)
print("modulus is ", modulus)
print("exponent is ", exponent)


# Comparison Operators / Relational Operators
a = 2
b = 3
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Assignment Operators
a = 2
b = 3
a += b  # a = a + b
print(a)
a -= b  # a = a - b
print(a)
a *= b # a = a * b
print(a)
a /= b # a = a / b
print(a)
a %= b  # a = a % b
print(a)
a //= b # a = a // b
print(a)
a **= b  # a = a ** b
print(a)
a = 2
a &= b  # a = a & b
print(a)
a |= b      # a = a | b
print(a)
a ^= b         # a = a ^ b
print(a)
a >>= b     # a = a >> b
print(a)
a <<= b      # a = a << b
print(a)

# Logical Operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)

# Bitwise Operators
a = 10
b = 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

# Membership Operators
x = 'Hello world'
print('H' in x)
print('h' not in x)

# Identity Operators
x = 5
y = 5
print(x is y)
print(x is not y)

# Precedence and Associativity of Operators
# Category	Operator	Associativity
# Postfix	() [] .	Left to right
# Unary	+ - ~	Right to left
# Arithmetic	**	Right to left
# Multiplication * / % //	Left to right
# Addition + -	Left to right
# Shift	>> <<	Left to right
# Bitwise AND	&	Left to right
# Bitwise OR	|	Left to right
# Comparison	< <= > >=	Left to right
# Equality	== !=	Left to right
# Logical AND	and	Left to right
# Logical OR	or	Left to right
# Conditional	 if else	Right to left
# Assignment	= += -= *= /= %= //= **= &= |= ^= >>= <<=	Right to left
# Comma	,	Left to right
# This table lists the precedence and associativity of all the operators in Python.


