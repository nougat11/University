import sqlite3
import socket
import sys
import threading
import json

conn_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 8888)
is_finished = [False]
ban_list = list()


def thread_tcp():
    conn_tcp.bind(server_addr)
    conn_tcp.listen()

    while not is_finished[0]:
        try:
            conn, addr = conn_tcp.accept()
            if addr in ban_list:
                print('Ban connection', addr)
                conn.close()
            else:
                print('Get connection', addr)
                t = threading.Thread(target=thread_connection, args=(conn, addr))
                t.start()
        except:
            ban_list.append(addr)
            print('Connection lost', addr)
            conn.close()


def thread_connection(client_socket, client_addr):
    try:
        while True:
            data = client_socket.recv(2048).decode()
            print(sys.getsizeof(data))

            if sys.getsizeof(data) > 2048:
                print('Catch buffer overflow from', client_addr)
                client_socket.close()
                return

            if not data:
                break

            print('GET FROM', client_addr, data, sys.getsizeof(data), 'bytes')
            data = data_menu(data, client_addr)
            print('SEND TO', client_addr, data)
            client_socket.sendall(data.encode())
    except:
        print('Connection lost', client_addr)
        ban_list.append(client_addr)
    finally:
        client_socket.close()


def data_menu(data: str, addr) -> str:
    conn_sql = sqlite3.connect('database.db')
    cursor = conn_sql.cursor()

    try:
        data = json.loads(data)
    except:
        data = ['bad request']

    if data[0] == 'in':
        res = cursor.execute(' SELECT name, password, role FROM users WHERE name = ? and password = ?', (data[1], data[2],)).fetchone()
        if res is not None:
            data = [[res[0], res[1], res[2]], get_posts(cursor, conn_sql)]
            if res[2] == 2:
                data.append(get_users(cursor))
        else:
            data = ['wrong input']

    elif data[0] == 'up':
        if cursor.execute(' SELECT COUNT(*) FROM users WHERE name = ? ', (data[1],)).fetchone()[0] == 0:
            cursor.execute(' INSERT INTO users(name, password, role) VALUES (?, ?, 1)', (data[1], data[2],))
            data = [[data[1], data[2], 1], get_posts(cursor, conn_sql)]
        else:
            data = ['already exist']

    elif data[0] == 'books':
        data = get_posts(cursor, conn_sql)

    elif data[0] == 'users':
        res = cursor.execute(' SELECT role FROM users WHERE name = ? and password = ? ', (data[1], data[2],)).fetchone()
        if res is not None and res[0] == 2:
            data = get_users(cursor)
        else:
            data = ['permission denied']

    elif data[0] == 'create book':
        res = cursor.execute(' SELECT id FROM users WHERE name = ? and password = ? ', (data[1], data[2],)).fetchone()
        if res is not None:
            cursor.execute(' INSERT INTO posts(id_users, name, category, author, price, telephone) VALUES(?, ?, ?, ?, ?, ?) ', (res[0], data[3], data[4], data[5], data[6], data[7],))
            data = ['create book', data[3]]
        else:
            data = ['no create book']

    elif data[0] == 'delete book':
        if cursor.execute(' SELECT role FROM users WHERE name = ? and password = ? ', (data[1], data[2],)).fetchone()[0] == 2:
            cursor.execute(' DELETE FROM posts WHERE id = ? ', (data[3], ))
            data = ['delete book', data[3]]
        else:
            res = cursor.execute(' SELECT id_users FROM posts WHERE id = ? ', (data[3],)).fetchone()[0]
            if cursor.execute(' SELECT COUNT(*) FROM users WHERE name = ? and password = ? and id = ? ', (data[1], data[2], res,)).fetchone()[0] == 1:
                cursor.execute(' DELETE FROM posts WHERE id = ? ', (data[3],))
                data = ['delete book', data[3]]
            else:
                data = ['no delete book', data[3]]

    elif data[0] == 'update role':
        res = cursor.execute(' SELECT id, role FROM users WHERE name = ? and password = ? ', (data[1], data[2],)).fetchone()
        if res is not None:
            if str(res[0]) != str(data[3]) and res[1] == 2:
                role = cursor.execute(' SELECT role FROM users WHERE id = ? ', (data[3],)).fetchone()[0]
                role = 1 if role == 2 else 2
                cursor.execute(' UPDATE users SET role = ? WHERE id = ? ', (role, data[3],))
                data = ['update role']
            else:
                data = ['no update role', data[3]]
        else:
            data = ['no update role', data[3]]

    cursor.close()
    conn_sql.commit()
    conn_sql.close()
    return json.dumps(data)


def get_posts(cur, conn) -> list:
    posts = list()
    for row in cur.execute(" SELECT id, name, category, author, price, telephone, id_users FROM posts "):
        row = list(row)

        cursor_user = conn.cursor()
        user_name = cursor_user.execute(" SELECT name FROM users WHERE id = " + str(row[-1]) + "").fetchone()[0]
        cursor_user.close()

        row[-1] = user_name
        posts.append(row)
    return posts


def get_users(cur) -> list:
    users = list()
    for row in cur.execute(" SELECT id, name, role FROM users "):
        users.append(list(row))
    return users


if __name__ == '__main__':
    t_server = threading.Thread(target=thread_tcp)

    t_server.start()
    t_server.join()
