from rsa import keygen, fullDecrypt
from rsaClient import sendMsg
import getchar
import csv
from colorama import init, Fore, Style

init()
getch = getchar._Getch()
partnerAddress = "127.0.0.1"
port = 12346
cifrasprimos = 4


def menu(opc):
    global partnerAddress
    global port
    global cifrasprimos
    # try:
    print("")
    if opc == "1":
        cifrasprimos = int(input("> "))
    elif opc == "2":
        partnerAddress = input("Ingrese la direccion: ")
        # port = int(input("Ingrese el puerto: "))
        if menu("+") and menu("-"):
            print(">" + Fore.GREEN + Style.BRIGHT + " Conexion Establecida!" + Style.RESET_ALL)
            print("")
        else:
            print(Fore.RED + Style.BRIGHT + "Servidor no disponible en este momento" + Style.RESET_ALL)

    elif opc == "-":
        pubkeyf = open('myRsaKeys/pubKey.csv', 'r')
        pubkey = list(csv.reader(pubkeyf))
        pubkeyf.close()
        pubkeystr = "||||--" + \
            str(pubkey).replace("[", "").replace("]",
                                                 "").replace(" ", "").replace("'", "")
        # print(pubkeystr)
        try:
            if sendMsg(pubkeystr, partnerAddress, port):
                return True
            else:
                return False
        except OSError:
            return False
        print("")
    elif opc == "+":
        privkeyf = open('myRsaKeys/privKey.csv', 'r')
        privkey = list(csv.reader(privkeyf))
        privkeyf.close()
        privkeystr = "|||||--" + \
            str(privkey).replace("[", "").replace("]",
                                                  "").replace(" ", "").replace("'", "")
        try:
            if sendMsg(privkeystr, partnerAddress, port):
                return True
            else:
                return False
        except OSError:
            return False
        print("")
    elif opc == "3":
        keygen(cifrasprimos, False)

        if menu("+") and menu("-"):
            print("Ingrese su mensaje:\n")
            msg = input("> ")
            try:
                sendMsg(msg, partnerAddress, port)
            except OSError:
                print("El host no esta disponible")
            print(">>> Mensaje enviado! >>>")
            print("")
        else:
            print(">" + Fore.RED + Style.BRIGHT + " Servidor no disponible" + Style.RESET_ALL)
            print("")
    elif opc == "4":
        privKeyf = open('myRsaKeys/privKey.csv', 'r')
        privKey = list(csv.reader(privKeyf))
        privKeyf.close()

        n = int(privKey[0][0])
        d = int(privKey[0][1])
        print("Ingrese el mensaje cifrado:\n")
        msjCifrado = input()
        print("")
        try:
            msjoriginal = fullDecrypt(n, d, msjCifrado)
            print("")
            print("El mensaje descifrado es:")
            print(">", msjoriginal)
            print("")
        except UnicodeDecodeError:
            print(
                "No se logro descifrar asegurese de que el mensaje este correctamente cifrado")
            print("")

    # except ValueError:
        # print("ValueError")


print("(!) El folder por defecto de las claves es myRsaKeys\n")
while True:
    print("-------Menu de opciones-------")
    print("")
    print("4) Descifrar un mensaje")
    print("0) Salir")
    print("")
    print("Seleccione una opcion:")
    opc = getch.impl()
    print(opc)
    if opc == "0":
        break
    menu(opc)
