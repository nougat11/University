import socket
import uuid
import datetime
from des import des_encode, des_decode, get_hex_key, time_compare

client_addr = ('127.0.0.1', 20000)
kdc_addr = ('127.0.0.1', 20001)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(kdc_addr)

# AS data
tgs = uuid.uuid4()
K_as_tgs = uuid.uuid4()
p1 = 10
# c: [K_c, K_c_tgs]
db = {'vlad': ['70617373776f7264', get_hex_key(str(uuid.uuid4()))]}

# TGS data
ss = '2323d4e8-4b32-44b2-b035-d0a6bf24daef'
K_tgs_ss = '3030353861396231'
p2 = 10
# c: Kc_ss
db_ss = {'vlad': '6231353064313266'}

if __name__ == "__main__":
    while True:
        try:
            data = sock.recvfrom(1024)[0].decode()
            if data[:2] == '1|':
                print('\n-= 2 =-')
                login = data[2:]

                TGT = login + '|' + str(tgs) + '|' + str(datetime.datetime.now()) + '|' + str(p1) + '|' + db[login][1]
                print(' TGT(d):', TGT)
                TGT_encode = des_encode(TGT, str(K_as_tgs), False)
                print(' TGT(e):', TGT_encode, '\n')

                res = TGT_encode + '|' + db[login][1]
                print(' res(d):', res)
                res_encode = des_encode(res, db[login][0], True)
                print(' res(e):', res_encode, '\n')

                sock.sendto(res_encode.encode(), client_addr)

            if data[:2] == '3|':
                print('-= 3 =-')
                data = data.split('|')


                TGT_encode = data[1]
                print(' TGT(e):', TGT_encode)
                TGT = des_decode(TGT_encode, str(K_as_tgs), False)
                print(' TGT(d):', TGT, '\n')
                TGT = TGT.split('|')

                AUT = des_decode(data[2], TGT[4], True)
                print(' AUT(d):', AUT, '\n')
                AUT = AUT.split('|')[1:]

                if TGT[0] == AUT[0] and time_compare(TGT[2], AUT[1], TGT[3]):
                    print('-= 4 =-')

                    TGS = TGT[0] + '|' + ss + '|' + str(datetime.datetime.now()) + '|' + str(p2) + '|' + db_ss[TGT[0]]
                    print(' TGS(d):', TGS)
                    TGS_encode = des_encode(TGS, K_tgs_ss, True)
                    print(' TGS(e):', TGS_encode, '\n')

                    res = TGS_encode + '|' + db_ss[TGT[0]]
                    print(' res(d):', res)
                    res_encode = des_encode(res, db[TGT[0]][1], True)
                    print(' res(e):', res_encode, '\n')

                    sock.sendto(res_encode.encode(), client_addr)

                else:
                    print('*Истекло время ключа или неправильный идентификатор*')
        except socket.error:
            pass

    sock.close()
