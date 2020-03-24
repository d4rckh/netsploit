import threading, os, time, random
from scapy.all import *
from termcolor import colored as termcolor
import sys
sys.path.append('..')
import argumentparser
from time import sleep
from mac_vendor_lookup import MacLookup

args = argumentparser.parse()
stop_hopper = args.dontHop

ch = 1

aps = []

def threadf(iface):
    n = 1
    while True:
        print("CHANNEL: " + str(n))
        print("NAME\t\t\tMAC ADDRESS")#\t\t\tCHANNEL")
        print("=============================================")
        for ap in aps:
            print(ap) 
        time.sleep(0.50)
        os.system('iwconfig %s channel %d' % (iface, n))
        dig = int(random.random() * 14)
        if dig != 0 and dig != n:
            n = dig
        os.system("clear")



F_bssids = []    # Found BSSIDs
def findSSID(pkt):
    if pkt.haslayer(Dot11Beacon):
        layer = pkt.getlayer(Dot11).addr2
        layerElt = pkt.getlayer(Dot11Elt)
        if layer not in F_bssids:
            ssid = layerElt.info
            ssid = ssid.decode("utf-8")
            mac = pkt.addr2
            channel = "PLACEHOLDER"#str(1)
            #mac = ssid.devoce("utf-8")
            aps.append(ssid + "\t\t" + mac)#) + "\t\t" + channel)
            if ssid == '' or layerElt.ID != 0:
               print("Hidden Network Beacon.")
            F_bssids.append(layer)

def show():
    pass

def start():
    thread = threading.Thread(target=threadf, args=(args.iface,), name="threadf")
    thread.daemon = True
    thread.start()
    thread = threading.Thread(target=show, args=(), name="show")
    thread.daemon = True
    thread.start()
    sniff(iface=args.iface, prn=findSSID)