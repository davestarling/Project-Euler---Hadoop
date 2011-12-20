"""Project Euler - Problem 3 Solution (Brute Force)"""

import time
from math import sqrt

start = time.time()

def isprime(n):
    for x in xrange(2, int(sqrt(n)) + 1):
        if not n % x:
            return False
    return True

def factors(n):
    yield 1
    i = 3 # start at 3
    while i <= sqrt(n) + 1:
        if n % i == 0: # can n be divided by i?
            if isprime(i):
                print '%s is a prime factor' % i
                yield i # if so, add to generator output
            n = n / i
        i += 2 # we started at 3, and we're only bothered about odd integers
    
    if n > 1:
        yield n

print '%s is the largest prime factor' % max(factors(600851475143))

print("Total Elapsed time: " + str(time.time()-start))