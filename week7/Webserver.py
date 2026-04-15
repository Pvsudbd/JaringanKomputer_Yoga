from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 6758
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Ready to serve...")

while True:
    print('Waiting for connection...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()

        print(message.splitlines()[0])

        filename = message.split()[1]
        print("File:", filename)

   
        f = open(filename[1:])
        outputdata = f.read()

    
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

     
        connectionSocket.send(outputdata.encode())

        connectionSocket.close()

    except IOError:
        print("404 Not Found")

        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())

        connectionSocket.close()

serverSocket.close()
sys.exit()