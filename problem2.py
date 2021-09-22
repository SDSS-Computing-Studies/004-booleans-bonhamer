#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
N = float(input("Enter a number"))
if N == int(N):
    print("This number is an integer")
elif N == float(N):
    print("This number is not a integer")