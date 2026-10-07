import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    weighted_sum = 0
    for i in range(len(x)):
        weighted_sum += x[i] *p[i]
    return float(weighted_sum)