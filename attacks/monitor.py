import threading, os, time, random
from scapy.all import *
from termcolor import colored as termcolor
import sys
sys.path.append('..')
import argumentparser

args = argumentparser.parse()
stop_hopper = args.dontHop

def hopper(iface):
    n = 1
    while not stop_hopper:
        time.sleep(0.50)
        os.system('iwconfig %s channel %d' % (iface, n))
        dig = int(random.random() * 14)
        if dig != 0 and dig != n:
            n = dig

F_bssids = []    # Found BSSIDs
def findSSID(pkt):
    if pkt.haslayer(Dot11Beacon):
        layer = pkt.getlayer(Dot11).addr2
        layerElt = pkt.getlayer(Dot11Elt)
        if True:#layer not in F_bssids:
            ssid = layerElt.info
            if layer not in F_bssids:
                print('New network: %s' % ssid)
                F_bssids.append(layer)
            if ssid == '' or layerElt.ID != 0:
               print("Hidden Network Beacon.")
            if not args.hideBeacons:
                print("Beacon: " + str(ssid))#+ " (ch " + str(n) + ")")
                if args.verbose:
                    print(pkt.summary())
    if pkt.haslayer(Dot11Deauth) and not args.hideDeauths:
        print(termcolor("Deauth packet: " + pkt.summary(), "red"))
   

def start():
    thread = threading.Thread(target=hopper, args=(args.iface,), name="hopper")
    thread.daemon = True
    thread.start()
    sniff(iface=args.iface, prn=findSSID)