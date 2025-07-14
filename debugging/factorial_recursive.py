#!/usr/bin/python3
import sys

# ----------------------------------------
# Function: factorial
# Description:
#   Calculates the factorial of a given non-negative integer using recursion.
#
# Parameters:
#   n (int): A non-negative integer whose factorial is to be calculated.
#
# Returns:
#   int: The factorial of the input number.
# ----------------------------------------
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read input number from command line argument, compute factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)
