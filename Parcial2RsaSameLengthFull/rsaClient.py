import socket
from rsa import fullEncrypt
import csv
from colorama import init, Fore, Style

init()


def sendMsg(msg, host, port):
    n = 0
    e = 0
    if not (msg.startswith("||||--") or msg.startswith("|||||--")):
        partnerPubKeyf = open('myRsaKeys/pubKey.csv', 'r')
        partnerPubKey = list(csv.reader(partnerPubKeyf))
        partnerPubKeyf.close()

        n = int(partnerPubKey[0][0])
        e = int(partnerPubKey[0][1])

        msg = str(fullEncrypt(n, e, msg))
        print("")
        print("Su mensaje cifrado es:")
        print("----------------------------------")
        print(Fore.GREEN + Style.BRIGHT + msg + Style.RESET_ALL)
        print("----------------------------------")

    msgencoded = msg.encode()

    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((host, port))
        clientsocket.send(msgencoded)
        clientsocket.close()
        return True
    except ConnectionRefusedError:
        return False
