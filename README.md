# DNS_DataExfil
Simple way to exfiltrate the data from the target machine.


**Step 1:** Setup EC2 instance on AWS or any cloud where you have control to Linux OS. This machine will be used for listening the DNS query so minimum hardware config will suffice. Following is the command for your quick reference to open port 53.
> sudo ufw allow 53/tcp
> 
> sudo systemctl restart ufw

**Step 2:** Add A record to your domain name to redirect the traffic to your EC2 instance.

**Step 3:** Start listening and save the PCAP file.
> sudo tcpdump -w dns.pcap -i eth0 port 53 -v


![Listener](https://github.com/user-attachments/assets/fc101f1a-d0ad-4665-8516-ce9977720015)

**Step 4:** Transfer file to windows machine to extract details from PCAP file.
> sudo python3 -m http.server 443

**Step 5:** Once the PCAP file is transferred use the python decoder to extract data.
> python decoder.py

![Decoder](https://github.com/user-attachments/assets/f1e6d57e-0ff0-4e1f-bd1e-b5a55a067e55)


**Note:**_*For Educational purposes only, and any misuse of the techniques is strongly dicouraged._
