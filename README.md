# Forensic Geo IP Traffic Analyser
Forensic tool to geo locate the traffic from a packet capture (.pcap) file for kali linux or any other linux distro

This tool locates the zone and co-ordinates of the ip traffic flowing through your network.

This is just an initial build, I will try to add vpn capture hopefully in the future.

in kali terminal

git clone https://github.com/faahilBfarouk/Forensic-Geo-IP-Traffic-Analyser-.git

cd Forensic-Geo-IP-Traffic-Analyser-

chmod +x install.sh 

./install.sh

done!!

# Demo

I have put up a demo traffic capture file called demo.pcap

you can run it by using forensicGeoIP -F demo.pcap -l

you can save the output using -o option

forensicGeoIP -F demo.pcap -l -o outpu.txt
