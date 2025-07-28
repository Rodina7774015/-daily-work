import json

class CheckFile():
    def __init__(self, file_user_name='user_name.json'):
        self.file_user_name = file_user_name
        self.user_name = None

    def ask_user_name(self):
        """Запрос у пользователя имени"""
        user_name = input("Введите свое имя: ")
        self.input_check(user_name)
        return user_name

    def check_user_name(self):
        """Читает имя, которое находится в файле"""
        with open(self.file_user_name) as rf:
            user_name = json.load(rf)
        return user_name

    def write_user_name(self, user_name):
        """Запись в файл"""
        with open(self.file_user_name, "w") as wr:
            json.dump(user_name, wr)
        print("Имя занесено в файл")

    def check_for_emptiness(self):
        """Проверка на пустоту файла"""
        with open(self.file_user_name, "r") as rf:
            content = rf.read()
            if not content:
                return False  # если файл пустой
            else:
                return True  # если файл не пуст
        
    def input_check(self, user_name):
        """Проверка, что введено имя"""
        if not user_name.isalpha():
            print("Вы ввели не имя")
        else:
            print(user_name)


my_user = CheckFile()
if not my_user.check_for_emptiness():
    us = my_user.ask_user_name()
    my_user.write_user_name(us)
else:
    u = my_user.check_user_name()
    print(u)