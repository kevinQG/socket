from socket import  *
from time import  sleep


#设置广播地址
dest = ('广播地址',9999)
s = socket(AF_INET,SOCK_DGRAM)
#设置能够发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
while True:
    sleep(2)
    s.sendto("HELLOWORLD".encode(),dest)

s.close()