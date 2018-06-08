#!/usr/bin/env bash

clear
echo "******* ForensicGeoIP Locator installer ********"
echo ""
echo "=====> Installing libraries Please Give 'Y' if prompted "
sudo apt-get install python
sudo apt-get install python-pip
sudo pip install dpkt
sudo pip install python-geoip
sudo pip install python-geoip-geolite2sudo chmod +x forensicGeoIP.py
sudo cp forensicGeoIP.py /usr/bin/forensicGeoIP
echo "=====> Done "
echo "This is a tool to geo locate all the packet traffic in your network from apacket capture file (typically captured using wireshark in .pcap format)"
echo "=====> Open terminal and type 'forensicGeoIP' for usage "
