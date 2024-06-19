# Pass Statement in Python
# Pass is a null statement in Python. Nothing happens when it is executed. It is used as a placeholder.
# Syntax:
# pass
# Example:
"""
for i in range(10):
    # empty block 

print("End of program")
"""
# Output: it will say indentation error beacuse the block is empty.
# IndentationError: expected an indented block
# so we use pass statement to avoid this error.
# Example:
for i in range(10):
    pass
if True:
    pass
print("Some useful code")