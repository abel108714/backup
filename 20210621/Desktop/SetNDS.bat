@echo off

netsh interface ip add dnsservers "Wired Ethernet Connection" s
atic 10.10.20.4 primary

netsh interface ip add dnsservers "Wired Ethernet Connection" 8.
8.8.8 index=2