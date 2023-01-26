"""
    A simple logic integration.
"""


def factorial(n: int) -> int:
    """ Calculate factorial by recursive solution. """
    if n < 1:
        return 1
    return factorial(n - 1) * n
