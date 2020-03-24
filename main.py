import attacks.monitor as monitor

import argumentparser

args = argumentparser.parse()

if args.attack == "monitor":
    monitor.start()