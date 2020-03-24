import threading, os, time, random
import argparse
from scapy.all import *
from termcolor import colored as termcolor

parser = argparse.ArgumentParser(description='WiFi attaccer')
parser.add_argument('--attack',
                   help="type of attack (monitor, deauth)")
parser.add_argument('--iface',
                    help="interface to run on")
parser.add_argument('--hideBeacons', help='Do not show beacons',
    action='store_true')
parser.add_argument('--hideDeauths', help='Do not show deauth packets',
    action='store_true')
parser.add_argument('--dontHop', help='Turn off channel hopping',
    action='store_true')
parser.add_argument('--verbose', help='Show more info about the packets',
    action='store_true')
parser.add_argument("-b", "--bssid", help="The BSSID of the Wireless Access Point you want to target")
parser.add_argument("-c", "--client",
                    help="The MAC address of the Client you want to kick off the Access Point, use FF:FF:FF:FF:FF:FF if you want a broadcasted deauth to all stations on the targeted Access Point")
parser.add_argument("-n", "--number", help="The number of packets you want to send")


def parse():
    return (parser.parse_args())