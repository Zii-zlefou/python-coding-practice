"""
Challenge 5: FizzBuzz

Problem: Write a function that returns a list where:
  - Numbers divisible by 3 are replaced with "Fizz"
  - Numbers divisible by 5 are replaced with "Buzz"
  - Numbers divisible by both 3 and 5 are replaced with "FizzBuzz"
  - Other numbers stay as strings of the number itself

Examples:
  fizzbuzz(15) → ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
  fizzbuzz(5) → ['1', '2', 'Fizz', '4', 'Buzz']
"""

def solution(n):
    """
    Generate FizzBuzz sequence from 1 to n (inclusive).
    
    Args:
        n: The upper limit (inclusive)
    
    Returns:
        List of strings following FizzBuzz rules
    """
    # Write your code here
    pass


# Test your solution
if __name__ == "__main__":
    result = solution(15)
    expected = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    status = "✓" if result == expected else "✗"
    print(f"{status} FizzBuzz(15):")
    print(f"   Got:      {result}")
    print(f"   Expected: {expected}")
    
    # Test a smaller case
    result2 = solution(5)
    expected2 = ['1', '2', 'Fizz', '4', 'Buzz']
    status2 = "✓" if result2 == expected2 else "✗"
    print(f"\n{status2} FizzBuzz(5):")
    print(f"   Got:      {result2}")
    print(f"   Expected: {expected2}")
