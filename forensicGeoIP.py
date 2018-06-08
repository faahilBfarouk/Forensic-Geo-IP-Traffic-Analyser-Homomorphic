#!/usr/bin/env python
#Author: Faahil B Farouk
import dpkt
import socket
import sys, os
from geoip import geolite2
import optparse
def geoLoc(ip):
        loc=geolite2.lookup(ip)
        try:
                reg=loc.timezone
                Lat,Long=loc.location
                if reg=='None':
                        return [Lat,Long,'N/A']
                else:
                        return [Lat,Long,reg]
        except:
                return 'N/A'
def printPcap(pcap,flag,out):
	if (out!=None):
		out=open(out,'wr')	
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			srcLoc=geoLoc(src)
			dst = socket.inet_ntoa(ip.dst)
			dstLoc=geoLoc(dst)
			if (out!=None):
				out.write('\n')
				out.write('\n[+] Src: ' + src +'('+srcLoc[2]+')'+ ' --> Dst: ' + dst+'('+dstLoc[2]+')')
			
				if (flag):
                                	out.write('\n[*] Src-> Lat:'+str(srcLoc[0])+' Long:'+str(srcLoc[1]))
                                	out.write('\n[*] Dst-> Lat:'+str(dstLoc[0])+' Long: '+str(dstLoc[1]))
			else:
				print('\n')
				print ('[+] Src: ' + src +'('+srcLoc[2]+')'+ ' --> Dst: ' + dst+'('+dstLoc[2]+')')
			
				if (flag):
                                	print('[*] Src-> Lat:'+str(srcLoc[0])+' Long:'+str(srcLoc[1]))
                                	print('[*] Dst-> Lat:'+str(dstLoc[0])+' Long: '+str(dstLoc[1]))
                        	
		except:
			pass


def main():
        parser=optparse.OptionParser(usage="usage: geoLoc [options] -F <file_name.pcap> [-o <output file>]")
        parser.add_option('-F', dest='fileName',type='string',help = 'the .pcap file to use')
        parser.add_option('-l',dest='lat',action='store_true',help='choose to view latitude and longitude')
        parser.add_option('-o',dest='out',help='the output file')
        (options, arg)=parser.parse_args()
        if (options.fileName==None):
            print (parser.usage)
            sys.exit()
        else:
            f=str(options.fileName)
            f=open(f)
            pcap = dpkt.pcap.Reader(f)
            printPcap(pcap,options.lat,options.out)

if __name__ == '__main__':
	main()
