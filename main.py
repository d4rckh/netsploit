import attacks.monitor as monitor
import attacks.deauth as deauth
import attacks.scan as scan

import argumentparser

args = argumentparser.parse()

if args.attack == "monitor":
    monitor.start()
if args.attack == "deauth":
    deauth.start()
if args.attack == "scan":
    scan.start()