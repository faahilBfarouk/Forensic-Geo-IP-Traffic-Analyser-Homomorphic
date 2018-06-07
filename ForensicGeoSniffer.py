import dpkt
import socket
from geoip import geolite2
def geoLoc(ip):
        loc=geolite2.lookup(ip)
        try:
                reg=loc.timezone
                if reg=='None':
                        return 'N/A'
                else:
                        return (reg)
        except:
                return 'N/A'
def printPcap(pcap):
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			print '[+] Src: ' + src +'('+geoLoc(src)+')'+ ' --> Dst: ' + dst+'('+geoLoc(dst)+')'
		except:
			pass
def main():
	f = open('geotest.pcap')
	pcap = dpkt.pcap.Reader(f)
	printPcap(pcap)
if __name__ == '__main__':
	main()
