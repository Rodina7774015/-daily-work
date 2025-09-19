import socket
from time import sleep

client=socket.socket()
# Подключения к localhost
client.connect(("127.0.0.1",3398))#Функция для подключения к серверу
print("Connected...")
sleep(4)
while True:
    message=input("Напишите сообщение : ")# Взаимодействие с сервером
    client.send(message.encode())#Для отправки данных  (в качестве параметра получает набор отправляемых данных)
    data=client.recv(1024)#Получаю ответ от сервера 
    print(data.decode())#Вывожу ответ от сервера 
    
client.close()
