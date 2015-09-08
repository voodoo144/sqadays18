import socket

serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(('', 0))
port=serversocket.getsockname()[1]
print "Fake server running on port %s"%port
serversocket.listen(5)
while 1:
    (clientsocket, address) = serversocket.accept()
    