import socket
from myRSA import fullEncrypt
import csv
from glob import glob


def sendMsg(msg, partnerAddress, port):
    n = 0
    e = 0

    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = partnerAddress
        clientsocket.connect((host, port))
        if not msg.startswith("||||--"):
            pubfile = glob('*.csv')[0]
            partnerPubKeyf = open(pubfile, 'r')
            partnerPubKey = list(csv.reader(partnerPubKeyf))
            partnerPubKeyf.close()

            n = int(partnerPubKey[0][0])
            e = int(partnerPubKey[0][1])

            msg = str(fullEncrypt(n, e, msg))
        # print(msg)
        msgencoded = msg.encode()
        clientsocket.send(msgencoded)
        clientsocket.close()

        clientsocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = partnerAddress
        clientsocket1.connect((host, port + 1))
        clientsocket1.send(msgencoded)
        clientsocket1.close()
        print(">>> Mensaje enviado! >>>")
    except ConnectionRefusedError:
        print("El receptor no esta listo para recibir el mensaje")
