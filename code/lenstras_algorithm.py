from math import sqrt
from random import randint
from exponentiation_modulo_n import pmod

def prime_sieve(n): 
    sieve = [True] * (n // 2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2 :: i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]

def fermat(p, n):
    mod = pmod(p, n - 1, n)
    if mod == 1:
        return True
    else:
        return False

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def lenstra(n):
    while gcd(n, 3) != 1:
        n /= 3

    while gcd(n, 2) != 1:
        n /= 2

    if fermat(2, n):
        return n

    x_1 = randint(1, n)
    y_1 = randint(1, n) 

    g = n    
    while g == n:
        b = randint(1, n)
        c = (y_1 * y_1 - x_1 * x_1 * x_1 - b * x_1) % n
        g = gcd(4 * b * b * b + 27 * c * c, n)
    
    if g > 1:
        return g
