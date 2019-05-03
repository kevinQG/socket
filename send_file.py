from socket import  *
from time import  sleep
s = socket()

s.bind(('0.0.0.0',8888))
s.listen(5)
c,addr = s.accept()
print("Connect from",addr)

f = open('311560.jpg','rb')
c.send('311560.jpg'.encode())
sleep(0.1)
while True:
    data = f.read(1024)
    if not data:
        break
    c.send(data)

f.close()
c.close()
s.close()