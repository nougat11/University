from authorize import *
from bridge import *


if __name__ == '__main__':
    while True:
        print("Здравствуйте. Вы не авторизированы.")
        print("1. Регистрация")
        print("2. Авторизация")
        print("0. Выход")
        key = input('Введите действие: ')
        if key == "1":
            login = register()
            bridge(login)
        elif key == "2":
            login = login()
            bridge(login)
        elif key == "0":
            break
        else:
            print("Действие не опознано")





