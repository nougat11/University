import sys
import socket
import json
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

conn_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 8888)
info = list()


class AuthWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(70, 70))
        self.setWindowTitle("Авторизация")

        layout = QVBoxLayout()
        self.setLayout(layout)

        tabs = QTabWidget()
        tabs.addTab(self.sign_in_ui(), "Войти")
        tabs.addTab(self.sign_up_ui(), "Регистрация")
        layout.addWidget(tabs)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        w.show()

    # GUI для TAB входа
    def sign_in_ui(self) -> QWidget:
        sign_in_tab = QWidget()
        layout = QFormLayout()

        self.e_name_in = QLineEdit()
        self.e_pass_in = QLineEdit()
        b_si_in = QPushButton('Войти', self)
        b_si_in.clicked.connect(self.on_click_sign_in)

        layout.addRow('Логин', self.e_name_in)
        layout.addRow('Пароль', self.e_pass_in)
        layout.addRow(b_si_in)

        sign_in_tab.setLayout(layout)
        return sign_in_tab

    def sign_in_ui(self):
        def get_reg_info():
            info[1] = QFormLayout()
            return QVBoxLayout()

        info = [QWidget(), QFormLayout(), QWidget(), QFormLayout()]
        self.e_name_in = QLineEdit()
        self.e_pass_in = QLineEdit()
        self.e_name_reg = QLineEdit()
        self.e_pass_reg = QLineEdit()

        b_si_in = QPushButton('Войти', self)
        b_si_in.clicked.connect(self.on_click_sign_in)

        info[1].addRow('Логин', self.e_name_in)
        info[3].addRow('Войти без регистрации', self.e_pass_reg)
        info[1].addRow('Пароль', self.e_pass_in)
        info[1].addRow(b_si_in)
        info[0].setLayout(info[1])

        if info[0] is not info[2]:
            info[2] = get_reg_info()
        return info[0]

    # GUI для TAB регистрации
    def sign_up_ui(self) -> QWidget:
        sign_up_tab = QWidget()
        layout = QFormLayout()

        self.e_name_up = QLineEdit()
        self.e_pass_up = QLineEdit()
        self.e_pass_up_check = QLineEdit()
        b_si_up = QPushButton('Регистрация', self)
        b_si_up.clicked.connect(self.on_click_sign_up)

        layout.addRow('Логин', self.e_name_up)
        layout.addRow('Пароль', self.e_pass_up)
        layout.addRow('Повт. пароль', self.e_pass_up_check)
        layout.addRow(b_si_up)

        sign_up_tab.setLayout(layout)
        return sign_up_tab

    # GUI Показать окно с ошибкой
    def show_error_msg(self, title: str, msg: str):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(msg)
        msg_box.setWindowTitle(title)
        msg_box.exec_()

    # Вход через существующего пользователя
    @pyqtSlot()
    def on_click_sign_in(self):
        data = json.dumps(['in', self.e_name_in.text(), self.e_pass_in.text()]).encode()
        print('Send', data)
        try:
            data = json.loads(tcp_data(data))
            print('Get', data)
            if data[0] == "wrong input":
                self.show_error_msg('Ошибка', 'Неправильный логин или пароль')
            else:
                global info
                info = data
                self.close()
                self.window = WorkWindow()
                self.window.show()
        except:
            self.show_error_msg('Ошибка', 'Непредвиденный ответ с сервера!')

    # Вход через регистрацию
    @pyqtSlot()
    def on_click_sign_up(self):
        data = json.dumps(['up', self.e_name_up.text(), self.e_pass_up.text()]).encode()
        print('Send', data)
        try:
            data = json.loads(tcp_data(data))
            print('Get', data)
            if data[0] == "already exist":
                self.show_error_msg('Ошибка', 'Данный пользователь уже зарегистрирован')
            else:
                global info
                info = data
                self.close()
                self.window = WorkWindow()
                self.window.show()
        except:
            self.show_error_msg('Ошибка', 'Непредвиденный ответ с сервера!')


class WorkWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        print(info)
        self.setMinimumSize(QSize(70, 70))
        self.setWindowTitle("Из рук в руки")

        layout = QVBoxLayout()
        self.setLayout(layout)

        tabs = QTabWidget()
        tabs.addTab(self.show_book_ui(), "Просмотр книг")
        tabs.addTab(self.create_book_ui(), "Разместить объявление")
        if info[0][2] == 2:
            tabs.addTab(self.manage_role_ui(), "Управление ролями")
        layout.addWidget(tabs)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    def show_book_ui(self) -> QWidget:
        show_book_tab = QWidget()
        layout = QFormLayout()

        self.t_book = QTableWidget()
        self.t_book.setColumnCount(6)
        self.t_book.setHorizontalHeaderLabels(["Название", "Жанр", "Автор", "Цена", "Телефон", "Разместил"])
        self.update_books_ui()
        self.t_book.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.t_book.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.t_book.itemDoubleClicked.connect(self.delete_book)
        self.t_book.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        header = self.t_book.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        for i in range(1, 6):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
        self.t_book.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.t_book)

        b_update = QPushButton('Обновить', self)
        b_update.clicked.connect(self.update_books)
        layout.addRow(b_update)

        show_book_tab.setLayout(layout)
        return show_book_tab

    def create_book_ui(self) -> QWidget:
        create_book_tab = QWidget()
        layout = QFormLayout()

        self.e_name = QLineEdit()
        self.e_name.setPlaceholderText("Последнее желание")
        layout.addRow('Название произведения', self.e_name)

        self.c_catg = QComboBox()
        self.c_catg.addItem("Фэнтези")
        self.c_catg.addItem("Детективы")
        self.c_catg.addItem("Ужасы")
        self.c_catg.addItem("Поэзия")
        self.c_catg.addItem("Фантастика")
        self.c_catg.addItem("Любовные романы")
        self.c_catg.addItem("Триллеры")
        self.c_catg.addItem("Комиксы и манга")
        self.c_catg.addItem("Проза")
        layout.addRow("Жанр произведения", self.c_catg)

        self.e_auth = QLineEdit()
        self.e_auth.setPlaceholderText("Анджей Сапковский")
        layout.addRow('Автор произведения', self.e_auth)

        self.e_pric = QLineEdit()
        self.e_pric.setPlaceholderText("20 руб.")
        layout.addRow('Цена за товар', self.e_pric)

        self.e_phone = QLineEdit()
        self.e_phone.setPlaceholderText("+375(29) 333-33-33")
        layout.addRow('Телефон для связи', self.e_phone)

        b_create = QPushButton('Разместить', self)
        b_create.clicked.connect(self.create_book)
        layout.addRow(b_create)

        create_book_tab.setLayout(layout)
        return create_book_tab

    def manage_role_ui(self) -> QWidget:
        manage_role_tab = QWidget()
        layout = QFormLayout()

        self.t_user = QTableWidget()
        self.t_user.setColumnCount(2)
        self.t_user.setHorizontalHeaderLabels(["Пользователь", "Роль"])
        self.update_users_ui()
        self.t_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.t_user.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.t_user.itemDoubleClicked.connect(self.change_role)
        self.t_user.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        header = self.t_user.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        for i in range(1, 2):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
        self.t_user.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.t_user)

        b_update = QPushButton('Обновить', self)
        b_update.clicked.connect(self.update_users)
        layout.addRow(b_update)

        manage_role_tab.setLayout(layout)
        return manage_role_tab

    # GUI Показать окно с ошибкой
    def show_error_msg(self, title: str, msg: str):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(msg)
        msg_box.setWindowTitle(title)
        msg_box.exec_()

    @pyqtSlot()
    def update_books_ui(self):
        books = info[1]
        self.t_book.setRowCount(len(books))
        for i in range(len(books)):
            self.t_book.setItem(i, 0, QTableWidgetItem(books[i][1]))
            self.t_book.setItem(i, 1, QTableWidgetItem(books[i][2]))
            self.t_book.setItem(i, 2, QTableWidgetItem(books[i][3]))
            self.t_book.setItem(i, 3, QTableWidgetItem(books[i][4]))
            self.t_book.setItem(i, 4, QTableWidgetItem(books[i][5]))
            self.t_book.setItem(i, 5, QTableWidgetItem(books[i][6]))

    @pyqtSlot()
    def update_books(self):
        try:
            data = json.dumps(['books', info[0][0], info[0][1]]).encode()
            print('Send', data)
            data = json.loads(tcp_data(data))
            print('Get', data)

            info[1] = data
            self.update_books_ui()
        except:
            self.show_error_msg('Ошибка', 'Ошибка при обновлении книг со стороны сервера')

    @pyqtSlot()
    def update_users_ui(self):
        users = info[2]
        self.t_user.setRowCount(len(users))
        for i in range(len(users)):
            role_name = 'Модератор' if users[i][2] == 2 else 'Пользователь'
            self.t_user.setItem(i, 0, QTableWidgetItem(users[i][1]))
            self.t_user.setItem(i, 1, QTableWidgetItem(role_name))

    @pyqtSlot()
    def update_users(self):
        try:
            data = json.dumps(['users', info[0][0], info[0][1]]).encode()
            print('Send', data)
            data = json.loads(tcp_data(data))
            print('Get', data)

            if data[0] == 'permission denied':
                self.show_error_msg('Ошибка', 'Доступ запрещён')
            else:
                info[2] = data
                self.update_users_ui()
        except:
            self.show_error_msg('Ошибка', 'Ошибка при обновлении пользователей со стороны сервера')

    @pyqtSlot()
    def delete_book(self):
        if self.t_book.item(self.t_book.currentRow(), 5).text() == info[0][0] or info[0][2] == 2:
            try:
                data = json.dumps(['delete book', info[0][0], info[0][1], info[1][self.t_book.currentRow()][0]]).encode()
                print('Send', data)
                data = json.loads(tcp_data(data))
                print('Get', data)
                if data[0] == 'no delete book':
                    self.show_error_msg('Ошибка', 'Удалить не получилось!')
                self.update_books()
            except:
                self.show_error_msg('Ошибка', 'Ошибка при удалении со стороны сервера')

    @pyqtSlot()
    def create_book(self):
        try:
            data = json.dumps(['create book', info[0][0], info[0][1], self.e_name.text(), self.c_catg.currentText(), self.e_auth.text(), self.e_pric.text(), self.e_phone.text()]).encode()
            print('Send', data)
            data = json.loads(tcp_data(data))
            print('Get', data)
            if data[0] == 'no create book':
                self.show_error_msg('Ошибка', 'Разместить объявление не получилось!')
            self.update_books()
        except:
            self.show_error_msg('Ошибка', 'Ошибка при размещении со стороны сервера')

    @pyqtSlot()
    def change_role(self):
        if info[0][2] == 2:
            try:
                data = json.dumps(['update role', info[0][0], info[0][1], info[2][self.t_user.currentRow()][0]]).encode()
                print('Send', data)
                data = json.loads(tcp_data(data))
                print('Get', data)
                if data[0] == 'no update role':
                    self.show_error_msg('Ошибка', 'Изменить роль не вышло!')
                self.update_users()
            except:
                self.show_error_msg('Ошибка', 'Ошибка при обновлении роли со стороны сервера')


def tcp_init():
    try:
        conn_tcp.connect(server_addr)
    except socket.error:
        print('Server not responding')


def tcp_data(data: str) -> str:
    try:
        conn_tcp.send(data)
        return conn_tcp.recv(2048).decode()

    except socket.error:
        return 'bad request'


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()

    tcp_init()

    app.exec_()
