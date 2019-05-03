from socket import  *

s = socket()
s.connect(('192.168.32.1',8888))
filename = s.recv(1024).decode()

f = open('E:\python\ '+filename,'wb')

while True:
    data = s.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
s.close()