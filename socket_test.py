from socket import  *
s = socket()
print(s.type)
#设置端口可立即重用
#设置套接字选项
#level 设置选项的类型  SOL_SOCKET
#optname 子类选项
#value 要设置的值
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#获取套接字的值
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))
s.bind(('127.0.0.1',6666))
#获取套接字绑定的地址
print(s.getsockname())
s.listen(5)
C,addr = s.accept()
#获取连接套接字的地址
print(C.getpeername())
data = C.recv(1024)
print(data)

C.close()
s.close()
