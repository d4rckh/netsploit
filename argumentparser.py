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
parser.add_argument('--verbose', help='Show more info about the packets',
    action='store_true')

def parse():
    return (parser.parse_args())