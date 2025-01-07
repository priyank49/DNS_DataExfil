# DNS_DataExfil
This is sample project to extract the data using DNS.

Step 1: Setup EC2 instance on AWS or any cloud where you have control to Linux OS. This machine will be used for listening the DNS query so minimum hardware config will suffice.

#Enable SSH
sudo ufw allow 53/tcp
sudo systemctl restart ufw

#start listening and save the PCAP file.
sudo tcpdump -w dns.pcap -i eth0 port 53 -v

#Transfer file to windows machine to extract details from PCAP file.
sudo python3 -m http.server 443

#once the PCAP file is transferred use the python decoder to extract data.
python decoder.py
