"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    curr_num = 1
    while len(list) < number_of_primes:
        if curr_num > 1:
            for i in range(2, curr_num):
                if curr_num % i == 0:
                    break
                else:
                    list.append(curr_num)
        else:
            print(f'Prime numbers are greater than 1')
        curr_num += 1

    return list
