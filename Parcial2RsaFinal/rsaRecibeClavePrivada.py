import socket
import csv


def startServer():
    port = 12348
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
    print("Listo para recibir claves en el puerto:", port)
    while True:
        connection, address = serversocket.accept()
        buf = connection.recv(8192)
        if len(buf) > 0:

            try:
                msg = buf.decode()
                privkeyf = open('myRsaKeys/privKey.csv', 'w')
                privkeyf.write(msg.replace("||||--", ""))
                privkeyf.close()
                print(address, ">>", msg)
            except UnicodeDecodeError:
                print("(!)")
        connection.close()


startServer()
