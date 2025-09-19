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
