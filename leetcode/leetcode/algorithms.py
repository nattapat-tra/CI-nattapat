def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    s = s.lower()  # Convert to lowercase
    s = ''.join(c for c in s if c.isalnum())  # Remove non-alphanumeric characters
    return s == s[::-1]  # Check if the string is equal to its reverse

def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b