import socket
import uuid
from des import des_encode, des_decode, get_hex_key
from datetime import datetime

client_addr = ('127.0.0.1', 20000)
kdc_addr = ('127.0.0.1', 20001)
ss_addr = ('127.0.0.1', 20002)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(client_addr)

if __name__ == "__main__":
    print('\n-= 1 =-')
    login = str('1|' + input('Введите ваш логин: '))
    print('C -> AS:', login)
    sock.sendto(login.encode(), kdc_addr)

    print('\n-= 2 =-')
    res_encode = sock.recvfrom(1024)[0].decode()
    print('AS -> C:', res_encode)

    print('\n-= 3 =-')
    password = input('Введите ваш пароль: ')
    res = des_decode(res_encode, password, False)
    TGT_encode, K_c_tgs = res.split('|')
    AUT1 = login + '|' + str(datetime.now())
    AUT1_encode = des_encode(AUT1, K_c_tgs, True)
    res = '3|' + TGT_encode + '|' + AUT1_encode
    print('C -> TGS:', res)
    sock.sendto(res.encode(), kdc_addr)

    print('\n-= 4 =-')
    res_encode = sock.recvfrom(1024)[0].decode()
    print('TGS -> C:', res_encode)

    print('\n-= 5 =-')
    res = des_decode(res_encode, K_c_tgs, True)
    TGS_encode, K_c_ss = res.split('|')
    AUT2 = login + '|' + str(datetime.now())
    AUT2_encode = des_encode(AUT2, K_c_ss, True)
    res = '5|' + TGS_encode + '|' + AUT2_encode
    print('C -> SS:', res)
    sock.sendto(res.encode(), ss_addr)

    print('\n-= 6 =-')
    res_encode = sock.recvfrom(1024)[0].decode()
    print('SS -> C:', res_encode)
    res = des_decode(res_encode, K_c_ss, True)
    if AUT2.split('|')[2] == res[:-1]:
        print('*Подлинность SS подтверждена!*')
        print('Ключ для защиты сеанса связи Kc_ss:', K_c_ss)
    else:
        print('*Истекло время ключа или неправильный идентификатор*')
    print()

    sock.close()
