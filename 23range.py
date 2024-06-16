# range() function
#Range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
#Syntax:
# range(start, stop, step?)

# start: Optional. An integer number specifying at which position to start. Default is 0
# stop: Required. An integer number specifying at which position to stop (not included).
# step: Optional. An integer number specifying the incrementation. Default is 1

# Example:

print(range(20))  # range(0, 20)

seq = range(20)

for i in seq:
    print(i)

for j in range(2, 11 ,1): # 
    print(j) 