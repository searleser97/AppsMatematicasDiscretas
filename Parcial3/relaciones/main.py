import csv
import getchar
from colorama import init, Fore, Style

init()
getch = getchar._Getch()

datos = []
campos = ["Nombre", "Edad", "No. de hermanos",
          "Delegacion", "Estatura", "Peso"]


def imprimeRelacion1(campo):
    global datos
    global campos
    campo = campo - 1
    print(Fore.GREEN + Style.BRIGHT)
    print("xRy <-->", campos[campo] + "(x) <=", campos[campo] + "(y)")
    print(Style.RESET_ALL)
    for i in range(len(datos)):
        for j in range(len(datos)):
            if not i == j:
                if datos[i][campo] <= datos[j][campo]:
                    print("(", datos[i][campo], "<=",
                          datos[j][campo], ")", end="")
                    print("--(", datos[i][0], "<=", datos[j][0], ")")


def imprimeRelacion2(campo):
    global datos
    global campos
    campo = campo - 1
    print(Fore.GREEN + Style.BRIGHT)
    print("xRy <-->", campos[campo] + "(x) =", campos[campo] + "(y)")
    print(Style.RESET_ALL)
    for i in range(len(datos)):
        for j in range(len(datos)):
            if not i == j:
                if datos[i][campo] == datos[j][campo]:
                    print("(", datos[i][campo], "=",
                          datos[j][campo], ")", end="--")
                    if not campo == 0:
                        print("(", datos[i][0], "=", datos[j][0], ")")
                    else:
                        print("")


def imprimeRelacion3():
    global datos
    global campos
    camposquecoinciden = [None] * 6
    coincidencias = 0
    print(Fore.GREEN + Style.BRIGHT)
    print("xRy <--> (x) coincide en 2 campos con (y)")
    print(Style.RESET_ALL)
    for i in range(len(datos)):
        for j in range(len(datos)):
            if not i == j:
                for k in range(6):
                    if datos[i][k] == datos[j][k]:
                        camposquecoinciden[coincidencias] = k
                        coincidencias += 1
            if coincidencias == 2:
                print(Fore.BLUE + Style.BRIGHT, datos[i][0], Style.RESET_ALL,
                      "coincide con",
                      Fore.BLUE + Style.BRIGHT, datos[j][0], Style.RESET_ALL, "en:")
                print("\t>", campos[camposquecoinciden[0]],
                      "y en", campos[camposquecoinciden[1]])
                print("\t", datos[i][camposquecoinciden[0]],
                      "=", datos[j][camposquecoinciden[0]])
                print("\t", datos[i][camposquecoinciden[1]],
                      "=", datos[j][camposquecoinciden[1]])
            coincidencias = 0


def imprimeRelaciones(campo):
    global datos
    datosf = open('datos.csv', 'r')
    datos = list(csv.reader(datosf))
    datosf.close()
    campo = int(campo)
    imprimeRelacion1(campo)
    imprimeRelacion2(campo)
    imprimeRelacion3()


if __name__ == "__main__":
    print("Programa que describe relaciones explicitamente acorde al campo seleccionado")
    while True:
        print("")
        print("----------Campos a relacionar----------")
        print("1) Nombre")
        print("2) Edad")
        print("3) No. de hermanos")
        print("4) Delegacion")
        print("5) Estatura")
        print("6) Peso")
        print("")
        print("Presione '0' para salir")
        print("")
        print("Seleccione un campo para describir las relaciones explicitamente:")
        campo = getch.impl()
        print(campo)
        if campo == "0":
            break
        imprimeRelaciones(campo)
