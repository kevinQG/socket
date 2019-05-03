from socket import  *

#接收，查看，返回客户端请求内容
def handleClient(connfd):
    request = connfd.recv(1024)
    # print('******')
    # print(request)
    # print('******')
    request_lines = request.splitlines()
    for line in request_lines:
        print(line.decode())

    try:
        f = open('index.html')
    except IOError:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n" #空行
        response += '''
                    sorry
                    '''
    else:
        response = "HTTP/1.1 200 OK \r\n"
        response += '\r\n'
        response += f.read()
    finally:
        connfd.send(response.encode())


#创建套接字，调用handleclient完成功能
def main():
  #创建TCP套接字
  sockfd = socket()
  sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
  sockfd.bind(('0.0.0.0' ,8000))
  sockfd.listen()
  while True:
      print("Listen the port 8000...")
      connfd,addr = sockfd.accept()
      #处理浏览器发来的请求
      handleClient(connfd)
      connfd.close()

if __name__ =="__main__":
    main()