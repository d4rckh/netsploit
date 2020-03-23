# wids
Wifi Intrusion Detection Sytem (*kinda*) and Attacker (*soon*)

## Functions
### Monitoring
- The actual Intrusion "Detection System"
- Shows beacons and deauths
- Shows unique networks
- Detects hidden networks
- Requires:
    - An interface with the mode set on monitor (use your fav method of setting up the mode to monitor, here's how with the `aircrack-ng` suite):
        > sudo airmon-ng start \<wlan0mon\>
    - Root access 
- Syntax (example):
    > python main.py --attack monitor --iface wlan0mon
    - **--attack monitor** `Selects the monitor function`
    - **--iface <interface>** `Selects the interface to be used`
        - Other optional params:
            - **--hideBeacons** `Do not show beacon packets`
            - **--hideDeauths** `Do not show deauth packets`
            - **--dontHop** `Disables channel hoppinh`
 
