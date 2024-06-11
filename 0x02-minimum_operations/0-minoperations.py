#!/usr/bin/python3
"""This module has the code"""


def minOperations(n):
    """This is what was missing"""
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
