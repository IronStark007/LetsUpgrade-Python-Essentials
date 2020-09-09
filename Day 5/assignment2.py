"""
Name:Ansari Mohammed Ali Nasim
Date:09/09/2020
Purpose-Python Essentials-Batch 7 Day 5 Assignment 2
"""


def checkprime(num):
    prime = 1
    for i in range(2, num):
        if num % i == 0:
            prime = 0
            return False
    if prime == 1:
        pass
    return True


if __name__ == '__main__':
    numlist = list(range(1, 2500))
    primelist = filter(checkprime, numlist)
    filterprime = primelist
    print(list(filterprime))
