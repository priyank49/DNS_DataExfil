# DNS_DataExfil
Simple way to exfiltrate the data from the target machine.
_*For Educational purposes only, and any misuse of the techniques is strongly dicouraged._


**Step 1:** Setup EC2 instance on AWS or any cloud where you have control to Linux OS. This machine will be used for listening the DNS query so minimum hardware config will suffice. Following is the command for your quick reference to open port 53.
> sudo ufw allow 53/tcp
> 
> sudo systemctl restart ufw

**Step 2:** Start listening and save the PCAP file.
> sudo tcpdump -w dns.pcap -i eth0 port 53 -v[^1]


![Listener](https://github.com/user-attachments/assets/fc101f1a-d0ad-4665-8516-ce9977720015)

**Step 3:** Transfer file to windows machine to extract details from PCAP file.
> sudo python3 -m http.server 443

**Step 4:** Once the PCAP file is transferred use the python decoder to extract data.
> python decoder.py

![Decoder](https://github.com/user-attachments/assets/f1e6d57e-0ff0-4e1f-bd1e-b5a55a067e55)
