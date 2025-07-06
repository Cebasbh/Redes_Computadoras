# Servidor
import socket

s = socket.socket()
s.bind(("",60230)) # Parametro de puerto a cambiar
s.listen(6) # Parametro de conexiones simultaneas a cambiar

print("El socket está escuchando... ")

while True:
    com, addr = s.accept()
    print(f"Conexión recibida de {addr}")
    data = com.recv(1024).decode()
    print(f"Paquete pedido {data}")
    #Parametro de nombres de archivos a cambiar
    if data == "1":
        file_name = "apellido_paterno.txt"
    elif data == "2":
        file_name = "apellido_paterno.jpg"
    
    with open(file_name, "rb") as archivo:
        while True:
            l = archivo.read(1024)
            if not l:
                break
            com.send(l)
    print(f"Terminó de enviar {file_name}") 
    com.send(b"Gracias por visitar! ")
    com.close()
# netstat -noap tcp | findstr 60230