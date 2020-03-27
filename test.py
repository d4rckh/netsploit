import argparse
from attacks.arpscan import start as arpscan

parser = argparse.ArgumentParser()
parser.add_argument('--attack', required=True)
parser.add_argument('--range', required=False)
args = parser.parse_args()

attack = args.attack

range = args.range

if attack == "arpscan":
    if range == None:
        print("Range not specified: --range")
        quit()
    arpscan(range)