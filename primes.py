"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    lower = 2
    upper = number_of_primes

    for num in range(lower, upper + 1):
        for i in range(2, num):
            if num % i == 0:
                break
            else:
                list.append(num)
                

    return list
