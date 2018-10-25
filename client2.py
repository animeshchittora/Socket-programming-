import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()

port = 9999


s.connect((host, port))

print ("Enter Message to send")

s.send(msg)

s.close()