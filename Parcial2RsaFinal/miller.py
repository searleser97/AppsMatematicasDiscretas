# 100048601294495909823278047075249701532169758133671146372533
# 50Digitos:10001483086651246409081018999851691334875359091899
# 103Digitos:1626001770908798196892860017709087981968928600177090879819689286001770908798196892860017709087981968767
from random import randrange


def is_prime(p):
    k = 100
    if p % 2 == 0:
        return False

    phi = p - 1
    d = phi
    r = 0

    while (d % 2 == 0):
        d = int(d / 2)
        r += 1

    for i in range(k):
        a = randrange(2, p - 2)
        exp = pow(a, d, p)
        if (exp == 1 or exp == p - 1):
            continue

        for j in range(r - 1):
            exp = pow(exp, 2, p)
            if exp == 1:
                return False
            if exp == p - 1:
                break

        else:
            return False

    return True


def is_prime1(n, k=100):
    # http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    if n <= 3:
        return n == 2 or n == 3
    neg_one = n - 1

    # write n-1 as 2^s*d where d is odd
    s, d = 0, neg_one
    while not d & 1:
        s, d = s + 1, d >> 1
    assert 2 ** s * d == neg_one and d & 1

    for i in range(k):
        a = randrange(2, neg_one)
        x = pow(a, d, n)
        if x in (1, neg_one):
            continue
        for r in range(1, s):
            x = x ** 2 % n
            if x == 1:
                return False
            if x == neg_one:
                break
        else:
            return False
    return True
