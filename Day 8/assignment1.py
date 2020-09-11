"""
Name:Ansari Mohammed Ali Nasim
Date:11/09/2020
Purpose-Python Essentials-Batch 7 Day 8 Assignment 1
Program - Finding Factorial of a number by taking input with decorator
"""


def enterinp(inp):
    def calculate():
        x = int(input("Enter a Number to find Facotorial:\n"))
        inp(x)
    return calculate


@enterinp
def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    print(f"Factorial of {n} is -", fac)


factorial()
