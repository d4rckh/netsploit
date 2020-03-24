import attacks.monitor as monitor
import attacks.deauth as deauth

import argumentparser

args = argumentparser.parse()

if args.attack == "monitor":
    monitor.start()
if args.attack == "deauth":
    deauth.start()