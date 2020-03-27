from scapy.all import ARP, Ether, srp
from time import sleep

def start(range, wait):
    arp = ARP(pdst=range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []

    for sent, received in result:
        res = {'ip': received.psrc, 'mac': received.hwsrc}
        if res not in clients:
            clients.append(res)
    sleep(wait)
    print("Wait time for arp replies: " + str(wait) + "s")
    print("Available devices:")
    print("IP\t\tMAC")
    print("-"*33)
    for client in clients:
        print(client["ip"] + "\t" + client["mac"])

