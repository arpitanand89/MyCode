import socket
s1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''req = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() '''
req = 'GET http://www.textfiles.com/100/914bbs.txt HTTP/1.0\n\n'.encode()
s1.connect(('GET http://www.textfiles.com/', 80))
s1.send(req)


while True:
	data = s1.recv(512)
	if len(data)<1:
		break
		print(data)
socket.close()
