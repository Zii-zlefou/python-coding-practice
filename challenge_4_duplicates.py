"""
Challenge 4: Find Duplicates

Problem: Write a function that finds all duplicate numbers in a list and returns them as a list.
Each duplicate should appear only once in the result.

Examples:
  find_duplicates([1, 2, 2, 3, 3, 3]) → [2, 3]
  find_duplicates([1, 2, 3, 4]) → []
  find_duplicates([5, 5, 5, 5]) → [5]
"""

def solution(numbers):
    """
    Find all duplicate numbers in the list.
    
    Args:
        numbers: List of integers
    
    Returns:
        List of duplicate numbers (each appearing once)
    """
    # Write your code here
    pass


# Test your solution
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 3, 3, 3], [2, 3]),
        ([1, 2, 3, 4], []),
        ([5, 5, 5, 5], [5]),
        ([1, 1, 2, 2, 3, 3], [1, 2, 3]),
        ([], []),
        ([7], []),
    ]
    
    for inputs, expected in test_cases:
        result = solution(inputs)
        # Sort both for comparison since order might vary
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        status = "✓" if result_sorted == expected_sorted else "✗"
        print(f"{status} solution({inputs}) = {result} (expected {expected})")
