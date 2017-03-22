from miller import is_prime1
from AlgoritmoExtendidoEuclides import euclidesExtendido
from random import randrange, seed, shuffle
from fractions import gcd
import bitarray
import csv

myAbc = []
encryptedList = []
asciichars = ""


def randPrime(N):
    start = 10**(N - 1)
    stop = 10**N
    p = 1
    while not is_prime1(p):
        p = randrange(start, stop)
    return p


def keygen(N, printProcess):
    d = -1
    while True:
        p1 = randPrime(N)
        p2 = randPrime(N)
        n = p1 * p2
        phin = (p1 - 1) * (p2 - 1)
        e = randrange(n)
        while not gcd(e, phin) == 1:
            e = randrange(n)
        mcd, d, y = euclidesExtendido(e, phin)
        if d > -1:
            if pow(pow(65, e, n), d, n) == 65:
                if printProcess:
                    print("p =", p1)
                    print("q =", p2)
                    print("n =", n, "=", p1, "*", p2)
                    print("phi(n) =", phin, "= (", p1, "- 1 )(", p2, "- 1 )")
                    print("")
                    print("e =", e)
                    print("MCD(", e, ",", phin, ") =", mcd, "=", "e(", d, ") + phi(n)(", y, ")")
                    print("")
                    print("Clave Publica:")
                    print("")
                    print("n =", n)
                    print("e =", e)
                    print("(", n, ",", e, ")")
                    print("")
                    print("Clave Privada:")
                    print("")
                    print("n =", n)
                    print("d =", d)
                    print("(", n, ",", d, ")")
                break
    publickey = [n, e]
    privatekey = [n, d]

    pubkeyf = open('myRsaKeys/pubKey.csv', 'w')
    pubkeyf.write(str(publickey[0]) + "," + str(publickey[1]))
    pubkeyf.close()

    privkeyf = open('myRsaKeys/privKey.csv', 'w')
    privkeyf.write(str(privatekey[0]) + "," + str(privatekey[1]))
    privkeyf.close()
    return publickey, privatekey


def encrypt(n, e, msj):
    msj = list(msj)
    arrCifrados = []
    for i in range(len(msj)):
        ba = bitarray.bitarray()
        ba.fromstring(msj[i])
        lista = ba.tolist()
        bitstr = ""
        for i in range(len(lista)):
            bitstr += str(int(lista[i]))
        # print(bitstr)
        bitsInt = int(bitstr, 2)
        charsCifrados = pow(bitsInt, e, n)
        arrCifrados.append(charsCifrados)
    return arrCifrados


def hideList(l):
    setAbcsCifrado()
    global myAbc
    global encryptedList
    strl = ""

    for i in range(len(l)):
        strl += myAbc[encryptedList.index(l[i])]

    return strl


def unhideList(strcifrado):
    setAbcsDecifrado()
    global myAbc
    global encryptedList
    strcifrado = list(strcifrado)
    encryptedChars = []
    for i in range(len(strcifrado)):
        encryptedChars.append(encryptedList[myAbc.index(strcifrado[i])])
    return encryptedChars


def fullDecrypt(n, d, msjCifrado):
    charsList = unhideList(msjCifrado)
    msjOriginal = ""
    for i in range(len(charsList)):
        charbits = "{0:8b}".format(pow(int(charsList[i]), d, n))
        bitslist = []
        for j in range(len(list(charbits))):
            if charbits[j] == "1":
                bitslist.append(True)
            else:
                bitslist.append(False)
        msjOriginal += bitarray.bitarray(bitslist).tostring()
    return msjOriginal


def setAbcsDecifrado():
    global myAbc
    global asciichars
    global encryptedList

    myAbc = []

    pubkeyf = open('myRsaKeys/pubKey.csv', 'r')
    pubkey = list(csv.reader(pubkeyf))
    pubkeyf.close()

    n = int(pubkey[0][0])
    e = int(pubkey[0][1])

    for i in range(126, 31, -1):
        myAbc.append(chr(i))
        

    seed(e)
    shuffle(myAbc)

    for i in range(32, 127):
        asciichars += chr(i)

    encryptedList = encrypt(n, e, asciichars)
    printRel(False)


def setAbcsCifrado():
    global myAbc
    global asciichars
    global encryptedList

    myAbc = []

    partnerPubKeyf = open('myRsaKeys/pubKey.csv', 'r')
    partnerPubKey = list(csv.reader(partnerPubKeyf))
    partnerPubKeyf.close()
    n = int(partnerPubKey[0][0])
    e = int(partnerPubKey[0][1])

    for i in range(126, 31, -1):
        myAbc.append(chr(i))

    seed(e)
    shuffle(myAbc)
    for i in range(32, 127):
        asciichars += chr(i)

    encryptedList = encrypt(n, e, asciichars)
    printRel(True)


def fullEncrypt(n, e, msj):
    return hideList(encrypt(n, e, msj))


def printRel(cifrando):
    global myAbc
    global asciichars
    global encryptedList

    lista = list(asciichars)
    for i in range(94):
        if cifrando:
            print(lista[i], ">", encryptedList[i], ">", myAbc[i])
        else:
            print(myAbc[i], ">", encryptedList[i], ">", lista[i])
# cifrado = fullEncrypt(12021967, 5355657, 'abcde', )
# print(cifrado)
# fullDecrypt(12021967, 4253193, cifrado)
# print('a,b,c,d,e')

# pubkey = 12021967,5355657
# privkey = 12021967,4253193

# cifrado:
# cifrado = pow(100,2884121304541360085,23894856835346686363)
# print(cifrado)
# cifrado: 16402887743323699339
# decifrado:
# print(pow(cifrado,11075612278415345429,23894856835346686363))

# cifrado:
# cifrado = pow(10,5355657,12021967)
# print(cifrado)
# hh = cifrado % 27
# decifrado = pow(hh,4253193,12021967)
# print(decifrado)
