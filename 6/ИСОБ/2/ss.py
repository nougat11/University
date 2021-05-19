import socket
import uuid
from des import des_encode, des_decode, get_hex_key, time_compare

client_addr = ('127.0.0.1', 20000)
ss_addr     = ('127.0.0.1', 20002)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ss_addr)

ss = '2323d4e8-4b32-44b2-b035-d0a6bf24daef'
K_tgs_ss = '3030353861396231'

if __name__ == "__main__":
    while True:
        try:
            data = sock.recvfrom(1024)[0].decode()
            if data[:2] == '5|':
                print('\n-= 5 =-')
                TGS_encode, AUT_encode = data[2:].split('|')

                print(' TGS(e):', TGS_encode)
                TGS = des_decode(TGS_encode, K_tgs_ss, True)
                print(' TGS(d):', TGS, '\n')
                TGS = TGS.split('|')

                print(' AUT(e):', AUT_encode)
                AUT = des_decode(AUT_encode, TGS[4], True)
                print(' AUT(d):', AUT, '\n')
                AUT = AUT.split('|')[1:]

                if TGS[0] == AUT[0] and time_compare(TGS[2], AUT[1], TGS[3]):
                    print('*Подлинность CLIENT подтверждена!*')
                    print('Ключ для защиты сеанса связи Kc_ss:', TGS[4])

                    print('\n-= 6 =-')
                    res = AUT[1] + '1'
                    print(' res(d):', res)
                    res_encode = des_encode(res, TGS[4], True)
                    print(' res(e):', res_encode)

                    sock.sendto(res_encode.encode(), client_addr)
                else:
                    print('*Истекло время ключа или неправильный идентификатор*')
                print('\n')
            pass
        except socket.error:
            pass
