#! /usr/bin/env python3
import AlgoritmoDivision
import isPrime
import AlgoritmoExtendidoEuclides
import primeFactors
import cribaErastotenes
import mcm
import CriteriosDivisibilidad

import primos
import miller
import CambioDeBase
import congruencias
from myRSA import keygen
from ExpBinaria import expBinaria

import getchar
from colorama import init, Fore, Style

getch = getchar._Getch()
init()
print("Cargando...")
primes = cribaErastotenes.cribaEr(999999)


def menu(opc):
    print("")
    try:
        if opc == "1":

            N = int(input("Ingrese numero a probar: "))
            print("")
            print("--> ", isPrime.isprime(N))

        elif opc == "2":

            a = int(input("Ingrese a: "))
            b = int(input("Ingrese b: "))
            print("")
            q, r = AlgoritmoDivision.DivisonConResiduo(a, b)
            if q == False:
                print(r)
            else:
                print("q = ", q, " r = ", r)

        elif opc == "3":

            a = int(input("Ingrese a: "))
            b = int(input("Ingrese b: "))
            print("")
            mcd, x, y = AlgoritmoExtendidoEuclides.euclidesExtendido(a, b)
            print("MCD(", a, ",", b, ") = ", mcd, " = ",
                  a, "(", x, ") + ", b, "(", y, ")")

        elif opc == "4":

            n = int(input("Ingrese el numero a factorizar en primos: "))
            print("")
            factores = primeFactors.primefactors(n, primes)

            if factores == True:
                print("Es Primo")
                return 1
            elif factores == False:
                print(Fore.RED + Style.BRIGHT + "Error: " +
                      Style.RESET_ALL + "Numero fuera del rango de la criba")
                return 1
            factores.append(0)
            unique = []
            exponentes = []
            cuenta = 1

            for i in range(len(factores) - 1):
                if (factores[i] not in unique):
                    unique.append(factores[i])
                if (factores[i] == factores[i + 1]):
                    cuenta += 1
                else:
                    exponentes.append(cuenta)
                    cuenta = 1

            for k in range(len(unique)):
                print(unique[k], "^", exponentes[k], end=" ")
                if (k != len(unique) - 1):
                    print(" * ", end=" ")

        elif opc == "5":

            a = int(input("Ingrese a: "))
            b = int(input("Ingrese b: "))
            print("")
            print("MCM(", a, ",", b, ") = ", mcm.mcm(a, b))

        elif opc == "6":

            n = int(input("Ingrese N: "))
            print("")
            for i in range(2, 21):
                lodividio = CriteriosDivisibilidad.divisibilidad(n, i)
                if (lodividio):
                    print(Fore.GREEN + Style.BRIGHT + str(i) +
                          " -->", lodividio, Style.RESET_ALL)
                else:
                    print(i, "-->", lodividio)

        elif opc == "a":

            N = int(input("Ingrese numero a probar: "))
            print("")
            print("--> ", miller.is_prime(N))

        elif opc == "b":

            N = int(input("Ingrese N: "))
            print("")

            primeList = primos.cribaPrimos(N)
            file = open('primos.txt', 'w')

            for item in primeList:
                file.write("%s , " % item)

            file.close()
            print(
                "Los numeros primos se encuentran en el archivo primos.txt del actual directorio")

        elif opc == "c":

            n = int(input("Ingrese numero en base 10: "))
            base = int(input("Ingrese la base a convertir: "))
            print("")
            result = CambioDeBase.Base10_BaseN(n, base, True)
            print(n, " en base ", base, " = ", result)

        elif opc == "d":

            base = int(input("Ingrese la base del numero a convertir: "))
            n = 0

            if (base > 10):
                n = input("Ingrese el numero en base " +
                          str(base) + " separado por comas: ")
            else:
                n = input("Ingrese el numero en base " + str(base) + ": ")

            result = CambioDeBase.BaseN_Base10(base, n, True)
            print("")
            print(n, " en base 10 = ", result)

        elif opc == "e":
            n = int(input("Ingrese N: "))
            x = int(input("Ingrese X: "))
            print("")
            print(CriteriosDivisibilidad.criterio(n, x))
        elif opc == "f":
            n = int(input("Ingrese N: "))
            m = int(input("Ingrese m: "))
            k, x = congruencias.reduce(n, m)
            print("k = ", k)
            print("x = ", x)
        elif opc == "g":
            a = int(input("Ingrese a: "))
            b = int(input("Ingrese b: "))
            m = int(input("Ingrese m: "))
            print("")
            congruencias.solucionCongruencia(a, b, m)
        elif opc == "h":
            x = int(input("Ingrese x: "))
            exp = int(input("Ingrese Exp: "))
            clase = int(input("Ingrese la clase: "))
            print("")
            result = expBinaria(x, exp, clase, True)
            print("Resultado = ", result)
        elif opc == "i":
            n = int(input("Ingrese N: "))
            print("")
            keygen(n, True)
        else:
            print(Fore.YELLOW + Style.BRIGHT + "(!) " + Style.RESET_ALL +
                  "La opcion seleccionada no existe, intente de nuevo...")
            return 0
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "Error: " + Style.RESET_ALL +
              "El valor introducido no fue valido, intente de nuevo...")
        menu(opc)
    except ZeroDivisionError:
        print(Fore.RED + Style.BRIGHT + "Error: " + Style.RESET_ALL +
              "Modulo o Division por cero, intente con un valor diferente de cero")
        menu(opc)

while True:

    opc = ""

    print("------------------------------------------------")
    print("Menu de opciones:")
    print("------------------------------------------------")
    print("1) Checar si un numero es primo")
    print("2) Calcular el residuo (r) y el numero (q) para a/b")
    print("3) Calcular x & y para cumplir con ax + by = MCD(a,b)")
    print("4) Calcular los factores primos de un numero 'N'")
    print("5) Calcular el MCM(a,b)")
    print("6) Checar si el 2,..,20 divide a un numero 'N' por criterios de divisibilidad")
    print("")
    print("a) Checar si un numero es primo por el algoritmo de Miller Rabin")
    print("b) Obtener primos en un rango [2 - N]")
    print("c) Convertir un numero base 10 a base N")
    print("d) Convertir un numero base N a base 10")
    print("e) Obtener criterio de divisibilidad hasta 'X' posiciones para un numero N")
    print("f) Obtener la solucion mas pequeña, dada una solucion general de congruencias")
    print("g) Obtener el proceso de solucion a una congruencia ax = b mod m")
    print("h) Obtener un numero X elevado a un Exp en clase M con Exponenciacion Binaria")
    print("i) Obtener el proceso de creacion de claves RSA con primos(p y q) de N cifras")
    print("")
    print("-Teclee '0' para salir")
    print("")
    print("Ingrese el numero o la letra de la opcion a ejecutar:")
    print("")
    opc = getch.impl()
    print(">>", opc)

    if opc == "0":
        print("")
        print("----> Hasta pronto! <----")
        print("")
        break
    else:
        key = 's'
        while key == 's' or key == 'S':
            if menu(opc) == 0:
                break
            print("")
            print(Fore.CYAN + "Desea continuar? s/n:" + Style.RESET_ALL)
            key = getch.impl()
            print(key)
