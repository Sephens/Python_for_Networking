import socket
from binascii import hexlify
def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.171.10']:
        packed_ip = socket.inet_aton(ip_addr)
        unpacked_ip = socket.inet_ntoa(packed_ip)
        print("Ip Address: %s => Packed: %s, Unpacked: %s" %(ip_addr, hexlify(packed_ip), unpacked_ip))
if __name__ == '__main__':
    convert_ip4_address()
        