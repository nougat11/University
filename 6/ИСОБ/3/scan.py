import socket
import threading
import time

is_finish = [False]


def thread_scanner(ip_t: str, port_s: int, port_e: int):
    for port in range(port_s, port_e):
        print('сканирую порт :', port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not sock.connect_ex((ip_t, port)):
            print('Открытый порт  :', port)
        sock.close()

        if is_finish[0]:
            return


def thread_exit():
    while not is_finish[0]:
        data = input()
        if data == 'exit':
            is_finish[0] = True


if __name__ == '__main__':
    ip_target = input('\nIP цели        : ')
    port_start = int(input('Стартовый порт : '))
    port_end = int(input('Конечный порт  : '))

    print('\nПоиск пошёл...\nДля остановки введите `exit`')
    t_scan = threading.Thread(target=thread_scanner, args=(ip_target, port_start, port_end + 1))
    t_exit = threading.Thread(target=thread_exit, daemon=True)

    start_time = time.time()

    t_scan.start()
    t_exit.start()
    t_scan.join()

    print('\nВремя работы   :', str(time.time() - start_time)[:-13], 'секунд\n')
