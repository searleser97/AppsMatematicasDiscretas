from myRSA import keygen, fullDecrypt, fullEncrypt
from rsaClient import sendMsg
import getchar
import csv
from glob import glob

getch = getchar._Getch()
partnerAddress = "192.168.0.23"
port = 12346


def menu(opc):
    global partnerAddress
    global port
    try:
        print("")
        if opc == "1":
            n = int(input("Ingrese el numero maximo de cifras para los primos: "))
            keygen(n, False)
            print("Las claves se encuentran en la carpeta myRsaKeys del mismo directorio")
        elif opc == "2":
            partnerAddress = input("Ingrese la direccion: ")
            port = int(input("Ingrese el puerto: "))
            print("Operacion Exitosa!")
        elif opc == "3":
            print("Ingrese su mensaje:\n")
            msg = input("> ")
            try:
                sendMsg(msg, partnerAddress, port)
            except OSError:
                print("El host no esta disponible")
            print("")
        elif opc == "4":
            pubfile = glob('*.csv')[0]
            partnerPubKeyf = open(pubfile, 'r')
            partnerPubKey = list(csv.reader(partnerPubKeyf))
            partnerPubKeyf.close()

            n = int(partnerPubKey[0][0])
            e = int(partnerPubKey[0][1])
            print("Ingrese su mensaje:\n")
            msg = input("> ")
            print("Su mensaje cifrado es:\n")
            print("------------------------------")
            print(fullEncrypt(n, e, msg))
            print("------------------------------")
            print("")
        elif opc == "5":
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
        elif opc == "6":
            pubkeyf = open('myRsaKeys/pubKey.csv', 'r')
            pubkey = list(csv.reader(pubkeyf))
            pubkeyf.close()
            pubkeystr = "||||--" + \
                str(pubkey).replace("[", "").replace("]",
                                                     "").replace(" ", "").replace("'", "")
            print(pubkeystr)
            try:
                sendMsg(pubkeystr, partnerAddress, port)
                print("Clave publica enviada!")
            except OSError:
                print("El servidor no esta disponible")
            print("")
    except ValueError:
        print("ValueError")


print("(!) El folder por defecto de las claves es myRsaKeys")
while True:
    print("-------Menu de opciones-------")
    print("1) Generar par de claves")
    print("2) Establecer la direccion y puerto del receptor del mensaje")
    print("3) Enviar Mensaje con la clave publica del archivo partnerKey.csv")
    print("4) Cifrar un mensaje")
    print("5) Descifrar un mensaje")
    print("6) Compartir Clave Publica")
    print("0) Salir")
    print("Seleccione una opcion:")
    opc = getch.impl()
    print(opc)
    if opc == "0":
        break
    menu(opc)
