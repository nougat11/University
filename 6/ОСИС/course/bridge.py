import socket
import struct
import sys
import threading


from base import *
from utils import *
def run_requster():
    requester = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    requester.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    requester.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    requester.settimeout(1.0)
    requester.bind(('', 25565))
    return requester

def run():
    chat = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    chat.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    chat.settimeout(1.0)
    chat.bind(('', 27015))
    return chat



def bridge(login):
    requester = run_requster()
    chat = run()

    group = None
    while True:
        print(f"Здравствуйте, {login}")
        print("Что желаете сделать?")
        print("1. Создать группу")
        print("2. Подключиться к группе")
        print("3. Отправить запросы")
        print("4. Принять запросы")
        print("5. Подключиться к чату")
        print("0. Выйти")
        action = input('Что желаете сделать?: ')
        if action == "1":
            create_group(login)
        elif action == "2":
            ip = choose_group(login)
            if ip:
                print(f"Вы успешно подключились к группе.")
                connect_to_group(chat, ip)
                group = (ip, 27015)
        elif action == "3":
            create_request(login, requester)
        elif action == "4":
            accept_request(login, requester)
        elif action == "5":
            if not group:
                print("Вы не подключились к группе.")
                continue
            cht(chat,group,login)
        elif action == "0":
            return
        else:
            print("Неизвестное действие")
def get_message(chat,login):
    k = 0
    while True:
        try:
            data, addr = chat.recvfrom(1024)
        except socket.timeout:
            k += 1
        else:
            if data.decode() == login +": /exit":
                sys.exit()
            if data.decode()[-5:] != "/exit":
                print(data.decode())
def cht(chat,group, login):
    th = threading.Thread(target = get_message, args=(chat,login,))
    th.start()
    print("Введите /exit для завершения.")
    while True:
        message = input()

        chat.sendto(str.encode(f"{login}: {message}"), group)
        if message == "/exit":
            break


def accept_request(login, requester):


    while True:
        try:
            request, addr = requester.recvfrom(1024)
        except socket.timeout:
            break
        else:
            request = request.decode("utf-8")
            requestor, admin, group_name=request.split(' ', 2)
            if admin == login:
                print(f"{requestor} желает присоединиться к вашей группе {group_name}")
                print("Да - принять, другие слова - отказать")
                action = input()
                
                if action == "Да":
                    base_request(sql_insert_group_access, (requestor, group_name,))


def create_request(login, requester):
    groups = base_request(sql_select_group_name,[])
    for i in range(len(groups)):
        groups[i] = groups[i][0]

    groups_req = base_request(sql_select_group_access,(login,))

    for i in range(len(groups_req)):
        groups_req[i] = groups_req[i][0]

    groups = list(set(groups) - set(groups_req))

    if len(groups) == 0:
        print("Вы состоите во всех группах")

        return
    print(*groups, sep='\n')
    while True:
        name = input("Введите название группы для соединения: ")
        if name in groups:
            host = base_request(sql_select_group_host, (name, ))[0][0]
            request = login + " " + host + " " + name
            requester.sendto(str.encode(request), ('<broadcast>', 25565))

            return
        else:
            print("Неверное имя. Попробуйте ещё раз.")



def connect_to_group(chat, ip):
    print(ip)
    gr = socket.inet_aton(ip)
    mr = struct.pack('4sL', gr, socket.INADDR_ANY)
    chat.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mr)
def choose_group(login):
    groups = base_request(sql_select_group_access, (login,))
    for i in range(len(groups)):
        groups[i] = groups[i][0]
    if len(groups) == 0:
        print("У вас нет групп для подключения.")
    print(*groups)
    while True:
        group_name = input("Введите название группы")
        if group_name not in groups:
            print("Неверное название")
            continue
        ip = base_request(sql_select_group_ip, (group_name,))[0][0]
        return ip

def create_group(login):
    ip = generate_ip()
    names = load_groups_names()
    while True:
        name = input("Введите название группы: ")
        if name in names:
            print("Извините. Группа с таким именем уже существует. Попробуйте ещё раз")
        else:
            break
    base_request(sql_insert_group, (ip, name, login, ))
    base_request(sql_insert_group_access,(login, name,))
