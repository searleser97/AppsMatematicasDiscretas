import socket
from myRSA import fullDecrypt
import csv


def startServer():
    port = 12346
    host = "127.0.0.1"

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))
        host = s.getsockname()[0]
    except socket.gaierror:
        print("No hay conexion a internet,")
        host = input("Ingrese la ip del servidor manualmente")

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((host, port))
    serversocket.listen(3)
    print("ip del Servidor:", host)
    print("Listo para recibir mensajes en el puerto:", port)
    while True:
        connection, address = serversocket.accept()
        buf = connection.recv(8192)
        if len(buf) > 0:
            privKeyf = open('myRsaKeys/privKey.csv', 'r')
            privKey = list(csv.reader(privKeyf))
            privKeyf.close()

            n = int(privKey[0][0])
            d = int(privKey[0][1])
            try:
                msg = buf.decode()
                if msg.startswith("||||--"):
                    print(address, ">>", msg)
                    pubkeyf = open('partnerKey.csv', 'w')
                    pubkeyf.write(msg.replace("||||--", ""))
                    pubkeyf.close()
                    print("<<<> Clave publica actualizada <>>>")
                else:
                    msg = fullDecrypt(n, d, msg)
                    print(address, ">>", msg)
            except UnicodeDecodeError:
                print("(!)")
        connection.close()


startServer()
