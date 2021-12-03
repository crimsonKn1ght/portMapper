#!/usr/share/env python3

import socket
import threading
import sys
from queue import Queue
import argparse


class argcheck:
	def __init__(self):
		self.example=\
		f'example: python {sys.argv[0]} -i 192.168.0.1 -p 200-300\n	 python {sys.argv[0]} -i 192.168.0.1 -p 100-400,443'

	def Argcheck(self):
		parser = argparse.ArgumentParser(description="Tool for web page & directory discovery and also good \nfor fuzzing or sub-domain enumeration", usage=f"python {sys.argv[0]} -i <ip> -p <ports range>", epilog=self.example, formatter_class=argparse.RawTextHelpFormatter)
		parser.add_argument('-i', '--ip', metavar='', dest='ip', help='Enter ip')
		parser.add_argument('-p', '--ports', metavar='', dest='ports', help='Enter port range')
		parser.add_argument('-v', '--version', action='version', version='Version: 1.0', help=f'Show version of {sys.argv[0]}')
		args = parser.parse_args()

		if len(sys.argv) < 1:
			parser.print_help()
			sys.exit()

		return args

class portDiscovery:
	def __init__(self,ip,ports):
		self.ip = ip
		self.ports = ports
		self.q = Queue()		

	def banner(self):
		border = '='*100+'\n'
		creator = 'DirEnum created by Gourab Roy(@confusedHatHacker)\nVersion: 1.0\nMeant for legal use only!\n'
		settings = f'Details:\n==> ip/domain: {self.ip}\n==> port range: {self.ports}\n'
		prologue = '\nStarting port Scanning:\n'
		print('\n'+border+creator+border+settings+border+prologue)

	def portScan(self):
		while not self.q.empty():
			port = self.q.get()
			try:
				scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				scan.settimeout(1.5)
				scan.connect((self.ip, port))
				open_ports.append(port)
				print('[+] Open port: {}'.format(port))
				scan.close()
			except:
				pass

	def run_scan(self,threads):
		for ports in self.ports:
			if '-' in ports:
				for port in range(int(ports.split('-')[0].strip()),int(ports.split('-')[1].strip())+1):
					self.q.put(port)
			else:
				self.q.put(int(ports.strip()))

		thread_list = []
		
		for _ in range(int(threads)):
			thread = threading.Thread(target=self.portScan)
			thread.start()
			thread_list.append(thread)

		for thread in thread_list:
			thread.join()

class portService:
	def __init__(self, ip):
		self.ip = ip
		pass

	def portService(self):
		for port in open_ports:
			try:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.settimeout(20)
				sock.connect((self.ip, port))
				service = socket.getservbyport(port)
				print("Port {}: {}".format(port, service))
				sock.close()
			except:
				print("Port {}: Couldn\'t retrieve service".format(port))



if __name__=='__main__':

	open_ports = []

	arguments = argcheck()
	args = arguments.Argcheck()
	
	ports = ['1-1000']
	ports = args.ports.split(',')

	portDisc = portDiscovery(args.ip, ports)
	portDisc.banner()
	portDisc.run_scan(400)

	services = portService(args.ip)
	services.portService()
