"""
Write a program that takes an integer argument and returns all the primes between 1 and that integer.
Example:

Input: 18
Return: [2, 3, 5, 7, 11, 13, 17]

Hint: Exclude the multiples of primes
"""

def is_prime(n):
    """Brute force check if a number `n` is prime."""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def enumerate_primes(n):
    return [i for i in range(2, n) if is_prime(i)]


# Test cases
assert is_prime(2)
assert is_prime(3)
assert not is_prime(4)
assert is_prime(5)
assert not is_prime(6)
assert is_prime(7)
assert not is_prime(8)
assert not is_prime(9)
assert not is_prime(10)
assert is_prime(11)


assert enumerate_primes(18) == [2, 3, 5, 7, 11, 13, 17]
