def descifrar(strCifrada):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(abc)):
        print(i, abc[i])
    result = [None] * 8
    print(len(result))
    strCifrada = strCifrada.split(",")
    for alfa in range(27):
        for beta in range(27):
            for i in range(8):
                pos = (((int(strCifrada[i]) - beta) % 27) * alfa) % 27
                result[i] = abc[pos]
            str1 = ''.join(result)
            print(str1, "beta =", beta, "alfa =", alfa)
            print("")
    return result


strCifrada = input()
descifrar(strCifrada)
