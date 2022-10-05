"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    list.append(2)
    num = 3
    while len(list) < number_of_primes:
        while num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
                else:
                    list.append(num)

    return list
