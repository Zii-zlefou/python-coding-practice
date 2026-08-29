"""
Challenge 1: Sum of Numbers

Problem: Write a function that returns the sum of all numbers in a list.

Examples:
  sum_list([1, 2, 3, 4]) → 10
  sum_list([10, 20, 30]) → 60
  sum_list([]) → 0
"""

def solution(numbers):
    """
    Return the sum of all numbers in the list.
    
    Args:
        numbers: List of integers
    
    Returns:
        Sum of all numbers
    """
    # Write your code here
    pass


# Test your solution
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], 10),
        ([10, 20, 30], 60),
        ([], 0),
        ([5], 5),
        ([-1, -2, -3], -6),
    ]
    
    for inputs, expected in test_cases:
        result = solution(inputs)
        status = "✓" if result == expected else "✗"
        print(f"{status} solution({inputs}) = {result} (expected {expected})")
