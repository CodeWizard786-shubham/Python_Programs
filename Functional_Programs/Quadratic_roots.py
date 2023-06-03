"""
@Author: shubham shirke
@Date: 2022-06-02 21:03:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-02 21:20:30
@Title : calculate roots of quadratic equation.
"""

from math import sqrt

def find_quadratic_roots(a, b, c):
    """
    Description: This function calculates the roots of a quadratic equation using the quadratic formula.
    Parameters: a, b, c are the coefficients of the quadratic equation.
    Returns:  root_1 and root_2 of the quadratic equation.
    """
    delta = b * b - 4 * a * c

    root_1 = (-b + sqrt(delta)) / (2 * a)   #formula for finding first root
    root_2 = (-b - sqrt(delta)) / (2 * a)   #formula for finding second root

    return root_1, root_2


a=int(input("Enter value of a for quadratic equation : "))
b=int(input("Enter value of b for quadratic equation: "))
c=int(input("Enter value of c for quadratic equation: "))
root_1,root_2 = find_quadratic_roots(a,b,c)

#Print
print(f"Quadratic Equation : {a}*x*x+{b}*x+{c}")
print(f"Therefore the roots of the quadratic equation are:{root_1} and {root_2}")






