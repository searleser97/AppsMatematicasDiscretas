import AlgoritmoExtendidoEuclides


def reduce(n, m):
    x = 0
    k = 0
    if (n > 0):
        while (True):
            x = n + m * k
            if (n + m * (k - 1) < 0):
                break
            k -= 1
    else:
        while(True):
            x = n + m * k
            if (x >= 0):
                break
            k += 1
    return k, x


def solucionCongruencia(a, b, m):
    mcd, x, y = AlgoritmoExtendidoEuclides.euclidesExtendido(a, m)
    solucion = b * x
    print("MCD(", a, ",", m, ") = ", mcd, " = ",
          a, "(", x, ") + ", b, "(", y, ")")
    print("")
    print("X = ", b, "(", x, ") + ", m, "k")
    print("")
    print("X = ", solucion, " + ", m, "k")
    print("")
    k, solucionminima = reduce(solucion, m)
    print("k = ", k)
    print("")
    print("X = ", solucionminima)
    return solucionminima
