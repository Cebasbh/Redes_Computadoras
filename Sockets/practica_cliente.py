# Cliente
import socket
from datetime import datetime

sock = socket.socket() 
host = socket.gethostname()
port = 60230  # Parametro de puerto a cambiar

sock.connect((host, port))
# Pedir el archivo
while True:
    x = input("¿Buenas tardes, qué deseas? \n\tPresiona 1 para recibir el txt de ejemplo\n\tPresiona 2 para recibir el jpg de ejemplo\n")
    if x == "1" or x == "2":
        sock.send(x.encode())
        # Nombres a cambiar
        if x == "1":
            print("Escogiste el texto. ")
            nuevo_nombre = f"Balbuena_{datetime.now().strftime('%H-%M-%S')}.txt"
        elif x == "2":
            print("Escogiste la imagen. ")
            nuevo_nombre = f"Balbuena_{datetime.now().strftime('%H-%M-%S')}.jpg"
        break
    else:
        print("Ingresa un valor valido por favor")
with open(nuevo_nombre, "wb") as archivo:
    print("Recibiendo datos")
    while True:
        data = sock.recv(1024)
        if not data:
            break 
        archivo.write(data)
print(f"Archivo obtenido! Guardado como {nuevo_nombre}")
sock.close()
input("Presiona Enter para salir...")
# netstat -noap tcp | findstr 60230