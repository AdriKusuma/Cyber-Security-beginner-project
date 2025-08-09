import socket
import argparse
import sys
from scapy.all import ARP, Ether, srp

port = [1, 7, 9, 11, 13, 15, 17, 18, 19, 20, 21, 22, 23, 25, 37, 42, 43, 49, 50, 53, 57, 65, 67, 68, 70, 77, 79, 80, 87, 88, 95, 98, 101, 102, 104, 105, 106, 107,
    109, 110, 111, 113, 115, 117, 119, 123, 129, 135, 137, 138, 139, 143, 161, 162, 163, 164, 174, 177, 178, 179, 191, 194, 199, 201, 202, 204, 206, 209,
    210, 213, 220, 345, 346, 347, 369, 370, 371, 372, 389, 406, 427, 443, 444, 445, 464, 465, 487, 500, 512, 513, 514, 515, 526, 530, 531, 532, 538, 540,
    543, 544, 546, 547, 548, 549, 554, 556, 563, 587, 607, 610, 611, 612, 628, 631, 636, 655, 706, 749, 750, 751, 754, 760, 765, 775, 777, 783, 808, 871,
    873, 901, 989, 990, 992, 993, 994, 995, 1001, 1080, 1093, 1094, 1099, 1109, 1127, 1178, 1194, 1214, 1236, 1241, 1300, 1313, 1314, 1352, 1433, 1434, 1524,
    1525, 1529, 1645, 1646, 1649, 1677, 1701, 1812, 1813, 1863, 1957, 1958, 1959, 2000, 2003, 2010, 2049, 2053, 2086, 2101, 2105, 2111, 2119, 2121, 2135, 2150,
    2401, 2430, 2431, 2432, 2433, 2583, 2600, 2601, 2602, 2603, 2604, 2605, 2606, 2607, 2608, 2628, 2792, 2811, 2947, 2988, 2989, 3050, 3130, 3260, 3306, 3493,
    3632, 3689, 3690, 4031, 4094, 4190, 4224, 4353, 4369, 4373, 4557, 4559, 4569, 4600, 4691, 4899, 4949, 5002, 5050, 5051, 5052, 5060, 5061, 5151, 5190, 5222,
    5269, 5308, 5353, 5354, 5355, 5432, 5556, 5666, 5667, 5671, 5672, 5674, 5675, 5680, 5688, 6000, 6001, 6002, 6003, 6004, 6005, 6006, 6007, 6346, 6347, 6444,
    6445, 6446, 6514, 6566, 6667, 7000, 7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008, 7009, 7100, 8021, 8080, 8081, 8088, 8990, 9098, 9101, 9102, 9103, 9418,
    9667, 9673, 10000, 10050, 10051, 10080, 10081, 10082, 10083, 10809, 11112, 11201, 11371, 13720, 13721, 13722, 13724, 13782, 13783, 15345, 17004, 17500,
    20011, 20012, 22125, 22128, 22273, 24554, 27374, 30865]

count = 0
parser = argparse.ArgumentParser(description="Simple Host Scanner")
group = parser.add_mutually_exclusive_group(required=True)

parser.add_argument("-p", "--port", type=int, nargs='+', dest='port', help="Input ports for scanning") 
parser.add_argument("-P", "--PORT", action='store_true', dest='ports', help="Scan common ports")
parser.add_argument("-v", "--verbose", action='store_true', dest='verbose', help="Show all port scan results")

group.add_argument("-H", "--Host", dest='hostname', help="Input hostname for scanning")
group.add_argument("-I", "--IP", dest='protocol', help="Input IP for scanning")
group.add_argument("-a", "--arp", action='store_true', dest='arp', help="Find active IP and MAC addresses on local subnet")

args = parser.parse_args()

try:
    if args.hostname:
        ip = socket.gethostbyname(args.hostname)
    elif args.protocol:
        ip = args.protocol

    if not args.arp:
        print(f"[+] Hostnama  : {args.hostname}")
        print(f"[+] IP Address: {ip}")

    if args.ports or args.port:
        targets = args.port if args.port else port
        print("\n[+] Scanning for open ports...")
        for i in targets:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip, i))
            if result == 0:
                print(f"[OPEN] Port {i}")
                count += 1
            elif args.verbose:
                print(f"[CLOSE] Port {i}")
            s.close()
        if count == 0:
            print("[!] All scanned ports are closed.")

except socket.gaierror:
    print("[-] Invalid hostname or IP. Please check your input.")
    sys.exit()


if args.arp:
    target_ip = "192.168.1.0/24"  
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=2, verbose=0)[0]

    print("\n[+] ARP Scan Result:\n")
    for sent, received in result:
        print(f"[up] {received.psrc}  ")
        print(f"MAC: {received.hwsrc}\n")