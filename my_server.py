import socket
import time
def main():
    serever=socket.socket()

    serever.bind(("127.0.0.1",3398)) # он будет прослушивать подключения.
    serever.listen(5)
    print("Server start")

    while  True:
        con,_=serever.accept()
        while True:
            data = con.recv(1024)
            print(f"ОН:{data.decode()}")
            mess=input("ТЫ:")
            con.send(mess.encode())
        con.cloes()
        
    serever.close()

main()
# import socket
 
# server = socket.socket()            # создаем объект сокета сервера
# hostname = socket.gethostname()
# print(hostname)     # получаем имя хоста локальной машины
# port = 12345                        # устанавливаем порт сервера
# server.bind((hostname, port))       # привязываем сокет сервера к хосту и порту
# server.listen(5)                    # начинаем прослушиваение входящих подключений
 
# print("Server starts")
 
# con, addr = server.accept()     # принимаем клиента
# print("connection: ", con)
# print("client address: ", addr)
 
# message = "Hello Client!"       # сообщение для отправки клиенту
# con.send(message.encode())      # отправляем сообщение клиенту
# con.close()                     # закрываем подключение
 
# print("Server ends")
# server.close()