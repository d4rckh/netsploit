import argparse
from attacks.arpscan import start as arpscan

parser = argparse.ArgumentParser()
parser.add_argument('--attack', required=True)
parser.add_argument('--range', required=False)
parser.add_argument('--wait', required=False, type=int)
args = parser.parse_args()

attack = args.attack

wait = args.wait
range = args.range

if attack == "arpscan":
    if range == None:
        print("Range not specified: --range (it's probably 192.168.0.1/24)")
        quit()
    if wait == None:
        wait = 2
    arpscan(range,wait)