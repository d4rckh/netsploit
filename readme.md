**__NOTE: This project is still in development, but it should work fine, if you find any bugs please create an issue!__**

# wids
Wifi Intrusion Detection Sytem (*kinda*) and Attacker (*soon*)

## Installing
Before installing make sure you have python3 and python3-pip added to your path
```sh
$ sudo su
# cd wids/
# git clone https://github.com/d4rckh/wids
# chmod +x setup.sh
# ./setup.sh
```

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
    - **--iface {interface}** `Selects the interface to be used`
    - Other optional params:
        - **--hideBeacons** `Do not show beacon packets`
        - **--hideDeauths** `Do not show deauth packets`
        - **--dontHop** `Disables channel hoppinh`
        - **--verbose** `Show more info (probably useless for now)`
            - Right now this is activated for deauth packets and can't be turned off
### Deauth
- Sends deauths from a client to an access point and to an access point to a client
- Disconnects every device from a wifi network no matter about the encryption used
- Does not require for the attacker to know the passport of the access point
- Requires:
    - An interface with the mode set on monitor using the channel your access point target uses(use your fav method of setting up the mode to monitor, here's how with the `aircrack-ng` suite):
        > sudo airmon-ng start \<wlan0mon\> \<channel\>
    - Root access
- Syntax (example):
    > sudo python main.py --attack deauth --bssid 10:FE:AC:AA:CC:AS --client 76:A6:F9:FF:A8:5E --iface wlan0mon --number 1
    - **--attack deauth** `Selects the deauth function`
    - **--iface {interface}** `Selects the interface to be used`
    - **--bssid {access point bssid}** `Defines the access point`
    - **--client {client bssid}** `Defines client/target bssid`
    - **--number {count}** `How many packets do you want to send?`
### Scan
- Scans for access points
    - An interface with the mode set on monitor (use your fav method of setting up the mode to monitor, here's how with the `aircrack-ng` suite):
        > sudo airmon-ng start \<wlan0mon\>
    - Root access
- Syntax (example):
    > sudo python main.py --attack scan --iface wlan0mon
    - **--attack scan** `Selects the scan function`
    - **--iface {interface}** `Selects the interface to be used`