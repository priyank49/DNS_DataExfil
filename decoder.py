from scapy.all import *
import base64

def extract_subdomains_from_queries(pcap_file):
    # Open the pcap file using Scapy
    packets = rdpcap(pcap_file)

    # Set to store unique subdomains
    seen_subdomains = set()

    # List to store the final subdomains to concatenate
    subdomains = []

    for packet in packets:
        # Check if the packet has a DNS layer
        if packet.haslayer(DNS):
            dns_layer = packet[DNS]
            
            # Check if this is a DNS query (qr == 0 means query) and the query type is A (type 1)
            if dns_layer.qr == 0 and dns_layer.qd.qtype == 1:  # qtype 1 corresponds to A record (IPv4)
                # Extract the queried domain name
                query_name = dns_layer.qd.qname.decode().strip('.')  # Remove trailing dot

                # Split the domain name by period ('.')
                parts = query_name.split('.')

                # If there are more than two parts, we have subdomains
                if len(parts) > 2:
                    subdomain = '.'.join(parts[:-2])  # Join everything except the last two parts (domain + TLD)
                    
                    # Check if this subdomain is not already seen
                    if subdomain not in seen_subdomains:
                        seen_subdomains.add(subdomain)  # Mark as seen
                        subdomains.append(subdomain)  # Add it to the list

    # Concatenate all the subdomains into a single string
    concatenated_subdomains = ''.join(subdomains)

    # Base64 decode the concatenated subdomains string
    decoded_subdomains = base64.b64decode(concatenated_subdomains).decode('utf-8', errors='ignore')

    # Print the exfiltrated info
    print("Data Exfiltrated: ", decoded_subdomains)

# Example usage
if __name__ == "__main__":
    pcap_file = "dns.pcap"  # Replace with your PCAP file path
    extract_subdomains_from_queries(pcap_file)
