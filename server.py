import socket
import sys
from _thread impoort *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket object
host = socket.gethostname()
port = 9999

try:
	s.bind((host,port)) # bind hostname and port
except socket.error:
	print ("Bind Failed")
	sys.exit()
	
s.listen(10) # can listen maximum 10 clients

def client(conn):
	wel = "Welcome to server"
	conn.send(wel.encode()) 
	while True:
		data = conn.recv(1024)
		reply = data.decode()
		if not data:
			break
		print (reply)
		conn.sendall(data)
		conn.close()

while 1:
	conn,addr = s.accept()
	start_new_thread(client,(conn,))


conn.close()
s.close()