import threading
import socket

udpSocket =None
destIP="127.0.0.1"
destPort=2000


def recvData():
	flag=True
	while flag:
		recvInfo= udpSocket.recvfrom(1024)
		if recvInfo[0]=="stop":
			flag=False
		print("\r\n>>%s"%(recvInfo[0]))
		pass

def sendData():
	flag=True
	while flag:
		sendInfo=raw_input("<<")
		if sendInfo=="stop":
			flag=False
		udpSocket.sendto(sendInfo,(destIP,destPort))
		pass

def main():
	global udpSocket, re,rh
	global destPort

	udpSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	destPort=int(input("input destPort: "))
	localPort=input("input localPort: ")
	udpSocket.bind(("",localPort))
	re=threading.Thread(target=recvData)
	rh=threading.Thread(target=sendData)

	re.start()
	rh.start()

if __name__ == '__main__':
	main()