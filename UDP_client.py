from socket import  *
import  sys




HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST,PORT)

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input("消息:")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    data,addr = sockfd.recvfrom(1024)
    print("从服务端收到：",data.decode())

sockfd.close()