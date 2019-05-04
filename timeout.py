from socket import  *
import  time

s = socket()
s.bind(('127.0.0.1',6666))
s.listen(5)

#设置套接字的超时检测
s.settimeout(20)

while True:
    print("Waiting from connect...")
    try:
        confd,addr = s.accept()
    except timeout:
        print("time out....")
        continue

    print("Connect from",addr)

    while True:
        data = confd.recv(1024).decode()
        if not data:
            break
        print(data)
    confd.close()
s.close()
