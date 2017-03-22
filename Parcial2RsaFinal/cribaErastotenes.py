from math import sqrt


def cribaEr(N):
    arr = [None] * (N + 1)
    primos = []

    arr[2] = True
    arr[3] = True

    i = 5
    w = 2

    while (i <= N):
        arr[i] = True
        i += w
        w = 6 - w

    i = 5
    sqrtn = int(sqrt(N))
    while (i <= sqrtn):
        if(arr[i]):
            h = 5
            while (i * h <= N):
                arr[i * h] = False
                h += 1
        i += w
        w = 6 - w

    for k in range(N):
        if (arr[k]):
            primos.append(k)
    return primos
