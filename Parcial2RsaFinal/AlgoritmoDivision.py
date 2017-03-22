
def DivisonConResiduo(a, b):

    q = 0
    r = 0
    if b <= 0:
        return False, "El Algoritmo de la division no funciona para b <= 0"
    if a > 0:
        while (b * q <= a):
            r = a - (b * q)
            if (r == 0 or b * (q + 1) > a):
                break
            q += 1
    else:
        while (r <= 0):
            r = a - (b * q)
            if (r >= 0):
                break
            q -= 1

    return q, r
