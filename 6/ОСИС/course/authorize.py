from base import *
from cryptography.fernet import Fernet
def input_reg():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    confirm_password = input("Подтвердите пароль: ")
    return login, password, confirm_password
def register():
    while True:
        login, password, confirm_password = input_reg()
        if confirm_password != password:
            print("Введенные пароли не совпадают")
            continue
        user = base_request(sql_select_user, (login,))
        if len(user) > 0:
            print("Пользователь с таким именем уже существует")
            continue
        if len(password) < 8:
            print("Пароль должен содержать хотя бы 8 символов")
            continue
        key = b'sZfIfHACBmosHsfB4858H_hIvh8tkJktvKE1Q4HgADs='
        f = Fernet(key)
        password = f.encrypt(password.encode())
        print(password)
        base_request(sql_insert_user, (login, password,))
        return login

def login():
    while True:
        login = input("Введите логин: ")
        passwor = input("Введите пароль: ")
        password = base_request(sql_select_user, (login,))
        if len(password) == 0:
            print("Неверный логин")
            continue
        password = password[0][0]
        key = b'sZfIfHACBmosHsfB4858H_hIvh8tkJktvKE1Q4HgADs='
        f = Fernet(key)
        password = f.decrypt(password)
        password = password.decode()
        if password != passwor:
            print("Неверный пароль")
        return login





