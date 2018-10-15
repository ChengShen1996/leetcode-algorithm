#! /usr/bin/python
from socket import socket, AF_INET, SOCK_STREAM

import select
import thread
import sys

# receSocket is the side connect with client and connectionSocket is the built connection
# sendSocket is the side connect with server
running = False

def messFullReceive(conn):
	wholeMessage 	= ''
	currMessage 	= ''
	while True:
		currMessage = conn.recv(1024)
		if(len(currMessage)==0):
			return None
		print(currMessage)
		wholeMessage +=currMessage
		if(currMessage[-1] == '\n'):
			return wholeMessage


def communicateThread(connC):
	global running
	while running:
		pass
	running = True
	sendSocket = socket(AF_INET, SOCK_STREAM)
	sendSocket.bind((fake_ip,0))
	sendSocket.connect((server_ip,8080))

	while True:
		messFromClient = messFullReceive(connC)
		if not messFromClient:
			break
		sendSocket.send(messFromClient)
		messFromServer = messFullReceive(sendSocket)
		if not messFromServer:
			break
		connC.send(messFromServer)
	connC.close()
	sendSocket.close()
	running = False



listen_port = int(sys.argv[1])
fake_ip = sys.argv[2]
server_ip = sys.argv[3]

recvSocket = socket(AF_INET, SOCK_STREAM)
recvSocket.bind(('127.0.0.1',listen_port))
recvSocket.listen(5)
i=0



while True:
	connectionSocket,addr = recvSocket.accept()

	thread.start_new_thread(communicateThread,(connectionSocket,))
	









# sendSocket = socket(AF_INET, SOCK_STREAM)
# sendSocket.bind((fake_ip,0))


# connectionSocket,addr = recvSocket.accept()
# sendSocket.connect((server_ip,8080))

# while True:
# 	messFromClient = messFullReceive(connectionSocket)
# 	if not messFromClient:
# 		break
# 	sendSocket.send(messFromClient)
# 	messFromServer = messFullReceive(sendSocket)
# 	if not messFromServer:
# 		break
# 	connectionSocket.send(messFromServer)

# sendSocket.close()
# connectionSocket.close()
