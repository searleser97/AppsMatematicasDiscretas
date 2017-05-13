# link primos https://www.alpertron.com.ar/googol.pl
# primo de 20 cifras: 10168938831019335571
# 20 cifras: 10791359168819853983
# 19 cifras: 1063107780316202539
# 18 cifras: 100055128505716009
# 17 cifras: 10022390619214807
# 15 cifras: 112582705942171

from math import sqrt
# from numba import jit


# @jit(target='cpu')
def isprime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n == 1:
        return False

    i = 5
    w = 2
    j = 1
    sqrtn = int(sqrt(n))
    while i <= sqrtn:
        j += 1
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


if __name__ == '__main__':
    print(isprime(int(input())))
