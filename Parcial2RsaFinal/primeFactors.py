import isPrime


def primefactors(n, primesList):
    if (isPrime.isprime(n)):
        return True
    factores = []
    i = 0

    try:
        while (i <= n):
            if (n % primesList[i] == 0):
                factores.append(primesList[i])
                n = n / primesList[i]
                i = -1
            i += 1
    except IndexError:
        return False
    return factores
