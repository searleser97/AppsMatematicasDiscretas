def euclidesExtendido(a, b):
    if (a > 0 and b == 0):
        return a, 1, 0
    if (a == 0 and b == 0):
        return False, False, False
    residuo = -1

    xprevio = 1
    yprevio = 0

    x = 0
    y = 1
    while residuo != 0:
        q = int(a / b)
        residuo = a % b
        a = b
        b = residuo
        auxx = xprevio - q * x
        xprevio = x
        x = auxx
        auxy = yprevio - q * y
        yprevio = y
        y = auxy
    return a, xprevio, yprevio


while True:
    try:
        a, b = map(int, input().split())
        gcd, x, y = euclidesExtendido(a, b)
        print(x, y, gcd)
    except:
        break
