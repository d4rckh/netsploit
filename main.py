import threading, os, time, random
import argparse
from scapy.all import *
from termcolor import colored as termcolor

parser = argparse.ArgumentParser(description='WiFi attaccer')
parser.add_argument('--attack',
                   help="type of attack (monitor)")
parser.add_argument('--iface',
                    help="interface to run on")
parser.add_argument('--hideBeacons', help='Do not show beacons',
    action='store_true')
parser.add_argument('--hideDeauths', help='Do not show deauth packets',
    action='store_true')
parser.add_argument('--dontHop', help='Turn off channel hopping',
    action='store_true')

args = parser.parse_args()

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
            
    if pkt.haslayer(Dot11Deauth) and not args.hideDeauths:
        print(termcolor("Deauth packet: " + pkt.summary(), "red"))
   

def monitor():
    thread = threading.Thread(target=hopper, args=(args.iface,), name="hopper")
    thread.daemon = True
    thread.start()
    sniff(iface=args.iface, prn=findSSID)


if args.attack == "monitor":
    monitor()