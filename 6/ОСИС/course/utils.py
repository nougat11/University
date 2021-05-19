import random

from base import *
def generate_ip():
    groups = load_groups_ip()
    ip = '224.5.2.1'
    while ip in groups:
        ip = [random.randint(224, 231), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        ip = list(map(str, ip))
        ip = ".".join(ip)
    return ip
def load_groups_ip():
    groups = base_request(sql_select_group, [])
    groups = [i[0] for i in groups]
    return groups
def load_groups_names():
    conn = create_connection(db)
    c = conn.cursor()
    group_query = c.execute(sql_select_group_name)
    groups = base_request(sql_select_group, [])
    groups = [i[0] for i in groups]
    return groups
