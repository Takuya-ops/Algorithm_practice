from math import factorial


def numberOfWaysToTraverseGraph(width, height):
    return factorial(width + height - 2) / factorial(width - 1) / factorial(height - 1)
