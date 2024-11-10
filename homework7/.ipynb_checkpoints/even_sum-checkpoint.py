# File: even_sum.py
import numpy as np
def sum_even_numbers(numbers):
    """
"Calculates sum of even numbers from given list or array"
    """
    sum = np.sum(num for num in numbers if num % 2 == 0)
    return sum