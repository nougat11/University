import sqlite3

db = r"sql1.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return conn
def base_request(request, data):
    conn = create_connection(db)
    c = conn.cursor()
    c.execute(request,data)
    conn.commit()
    q = c.fetchall()
    c.close()
    conn.close()
    return q
sql_select_user = '''select password from user where login = ?;'''
sql_insert_user = '''INSERT INTO USER(login, password) VALUES (?, ?);'''
sql_select_group = '''select ip from groups;'''
sql_select_group_name = '''select name from groups;'''

sql_insert_group = '''insert into groups(ip, name, host) values(?, ?, ?);'''
sql_insert_group_access = '''insert into group_access(user_name, group_name) values(?, ?);'''
sql_select_group_access = '''select group_name from group_access where user_name = ?;'''
sql_select_group_ip = '''select ip from groups where name = ?;'''
sql_select_group_host = '''select host from groups where name = ?;'''