#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Function Description:
    This function computes the factorial of a given non-negative integer n recursively.
    The factorial of a number n (denoted as n!) is the product of all positive integers 
    less than or equal to n.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input integer n.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


f = factorial(int(sys.argv[1]))
print(f)
