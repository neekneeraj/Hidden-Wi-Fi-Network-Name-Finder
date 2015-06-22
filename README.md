# Cracking and Hardening of Hidden-SSID feature of Wireless Access Point
APs announces its presence by broadcasting the SSID, which is human-readable and often contain name of organisation, companies or government departments. Hidden networks restrict APs point from broadcasting the SSID, gives organisation some privacy. The clients need to send directed active probe to every AP they encountered. This creates the tradeoff between the privacy for the network and for the client. Many organisation gives importance to their infrastructure security rather than that of the client. They see hiding the network as defense in depth when used in combination with other mechanisms such as link-layer encryption and MAC-address filtering.

This project comprises of: 

1. A tool which crack and hardens the Hidden-SSID feature

    o The cracking part attacks actively or passively to find the hidden network name. 
    
    o The hardening part spoofs the automated cracking tools and also make it harder and time consuming for the manually crackers to crack it by injecting frames with fake SSID into the Wi-Fi network.

2. Used Kali Linux as platform and Python 2.7.3 for coding the tool

3. Scapy 2.2.3 is used as the library for IEEE 802.11 frame handling

4. Cracking part is useful for penetration testing and hardening part make Hidden-SSID more reliable and secure
