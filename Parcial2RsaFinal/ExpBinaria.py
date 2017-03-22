def expBinaria(x, exp, clase, printProcess):
    Expbase2 = "{0:b}".format(exp)
    if printProcess:
        print("")
        print(Expbase2)
        print("")
    Expbase2 = list(Expbase2)
    result = x
    expvariable = 2
    result = pow(result, 2, clase)
    if printProcess:
        print(x, "^", expvariable, "=", result, "mod", clase)
    lastpos = len(Expbase2) - 1
    for i in range(1, lastpos):
        if (Expbase2[i] == "1"):
            result = pow(result * x, 2, clase)
            expvariable = (expvariable + 1) * 2
            if printProcess:
                print(x, "^", expvariable, "=", result, "mod", clase)
        else:
            result = pow(result, 2, clase)
            expvariable = expvariable * 2
            if printProcess:
                print(x, "^", expvariable, "=", result, "mod", clase)

    if (Expbase2[lastpos] == "1"):
        result = (result * x) % clase
        expvariable += 1
        if printProcess:
            print(x, "^", expvariable, "=", result, "mod", clase)

    return result
