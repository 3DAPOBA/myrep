import socket


site=input('куда направляемся? ')
file=input('что читаем? ')
if not site:
    site='192.168.56.101'
if not file:
    file='index.html'
#input ('присвоил')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#input ('создал сокет')
sock.connect((site, 80))
#input('подключился к сокету')
sock.send(('GET /{} HTTP/1.1\r\n'.format(file) + 'Host: {}\r\n\r\n'.format(site)).encode('utf-8'))
#input('отправил')
print (sock.recv(1024).decode())
#input('принял')
sock.close()
#input('закрыл')
input ('Press enter to exit')