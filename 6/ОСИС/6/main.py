import socket
import struct
import json
import random


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


def send_message(name, chat, group):
    message = input("Type a message: ")
    message = name + ': ' + message
    chat.sendto(str.encode(message), group)


def get_messages(chat):
    messages = []
    while True:
        message = get_message(chat)
        if message == 0:
            break
        else:
            message = message.decode("utf-8")
            messages.append(message)
    if len(messages) == 0:
        print("You don't have new messages")
    else:
        print(f"You have {len(messages)} new messages")
        print(*messages, sep='\n')


def get_message(chat):
    try:
        data, addr = chat.recvfrom(1024)
    except socket.timeout:
        return 0
    else:
        return data


def load_groups():
    groups = 0
    ips = []
    with open('groups.json', 'r') as f:
        groups = json.load(f)
    for group in groups:
        ips.append(group['ip'])
    return ips


def generate_ip():
    groups = load_groups()
    ip = '224.5.2.1'
    while ip in groups:
        ip = [random.randint(224, 231), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        ip = list(map(str, ip))
        ip = ".".join(ip)
    return ip


def create_group(login):
    ip = generate_ip()
    names = []
    with open('groups.json', 'r') as f:
        groups = json.load(f)
    for group in groups:
        names.append(group['name'])
    while True:
        name = input("Type a name of group: ")
        if name in names:
            print("Sorry. Such a group already exists. Try again")
        else:
            break
    users = [login]
    group = {'ip': ip, 'name': name, "host": login, "users": users}
    with open('groups.json', 'r') as f:
        groups = json.load(f)
    groups.append(group)
    with open('groups.json', 'w') as outfile:
        json.dump(groups, outfile)


def choose_group(login, group_chosen):
    with open('groups.json', 'r') as f:
        groups = json.load(f)
    visible_groups = []
    for group in groups:
        if login in group['users']:
            visible_groups.append(group['name'])
    if len(visible_groups) == 0:
        print("Sorry. You don't have any groups. Create new group or create request")
        return
    print(*visible_groups, sep='\n')
    while True:
        print("Type a name group for connecting")
        name = input()
        if group_chosen:
            if name == group_chosen['name']:
                print("You already connected to this group. Choose another.")
                continue
        if name in visible_groups:
            for group in groups:
                if name == group['name']:
                    return group
        else:
            print("Invalid name. Try again")


def connect_to_group(chat, ip):
    print(ip)
    gr = socket.inet_aton(ip)
    mr = struct.pack('4sL', gr, socket.INADDR_ANY)
    chat.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mr)


def create_request(login, requester):
    with open('groups.json', 'r') as f:
        groups = json.load(f)
    non_groups = []
    for group in groups:
        if login not in group['users']:
            non_groups.append(group['name'])
    if len(non_groups) == 0:
        print("You in all groups.")
        return
    print(*non_groups, sep='\n')
    while True:
        print("Type a name group for connecting")
        name = input()
        if name in non_groups:
            print(groups)
            for group in groups:
                if name == group['name']:
                    request = login + " " + group['host'] + " " + group['name']
                    requester.sendto(str.encode(request), ('<broadcast>', 25565))
                    return
        else:
            print("Invalid name. Try again")


def accept_request(login, requester):
    with open('groups.json', 'r') as f:
        groups = json.load(f)
    while True:
        try:
            request, addr = requester.recvfrom(1024)
        except socket.timeout:
            break
        else:
            request = request.decode("utf-8")
            print(request)
            requestor, admin, name_group = request.split(' ', 2)
            if admin == login:
                print(f"{requestor} wants to join un your group{name_group}")
                print("Yes - for accept, another symbols - for decline")
                action = input()
                if action == "Yes":
                    for group in groups:
                        if group['name'] == name_group:
                            group['users'].append(requestor)
                            break
    with open('groups.json', 'w') as outfile:
        json.dump(groups, outfile)


def group_hub(chat, login, requester):
    group = None
    while True:
        print('1. Create a group')
        print('2. Choose a group')
        print('3. Request.')
        print('4. Accept request')
        print('0. Exit')
        action = input('Action: ')
        if action == "1":
            create_group(login)
        elif action == "2":
            group = choose_group(login, group)
            if group:
                print(f"Congratulations. You connected in a group {group['name']}")
                connect_to_group(chat, group['ip'])
        elif action == "3":
            create_request(login, requester)
        elif action == "4":
            accept_request(login, requester)
        elif action == "0":
            if group:
                return group
            return
        else:
            print("Sorry. I don't understand this action.")


def main(chat, requester):
    name = input("What's your name?: ")
    group = None
    print(f"Hello {name}!")
    while True:
        print(f"What do you want to do?")
        print("1. Write a message.")
        print("2. Get messages.")
        print("3. GroupHub")
        print("0. Return")
        action = input("Action: ")
        if action == "1":
            if group:
                send_message(name, chat, group)
            else:
                print("You don't choose group. Please choose in GroupHub")
        elif action == "2":
            if group:
                get_messages(chat)
            else:
                print("You don't choose group. Please choose in GroupHub")
        elif action == "3":
            group = group_hub(chat, name, requester)
            if group:
                group = (group['ip'], 27015)
        elif action == "0":
            return
        else:
            print("Sorry. I don't know this action.")



if __name__ == '__main__':
    requester = run_requster()
    chat = run()
    main(chat, requester)


