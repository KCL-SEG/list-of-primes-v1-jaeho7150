"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    for num in range(1, numbers_of_primes + 1):
        for i in range(1, num):
            while num%i != 0:
                list.append(num)

    return list
