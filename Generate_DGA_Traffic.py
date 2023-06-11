from scapy.all import *
import random
import string
import datetime


def generate_dga_domains(seed, count):
    random.seed(seed)
    tld = ['.com', '.net', '.org', '.info']
    domains = []
    for _ in range(count):
        domain_length = random.randint(8, 15)
        domain = ''.join(random.choice(string.ascii_lowercase)
                         for _ in range(domain_length))
        domain += random.choice(tld)
        domains.append(domain)
    return domains


def generate_seed():
    now = datetime.datetime.now()
    seed = now.strftime("%Y%m%d%H")
    return seed


def generate_dga_packet(seed, count):
    domains = generate_dga_domains(seed, count)
    packet = IP(src="192.168.138.158", dst="192.168.138.2") / UDP(sport=random.randint(
        1024, 65535), dport=53) / DNS(rd=1, qd=[DNSQR(qname=domain) for domain in domains])
    return packet


# Example usage
pcap_file = 'DGA_traffic.pcap'
packet_count = 10
domain_count = 5

packets = []
for _ in range(packet_count):
    seed = generate_seed()
    packet = generate_dga_packet(seed, domain_count)
    packets.append(packet)

wrpcap(pcap_file, packets)
