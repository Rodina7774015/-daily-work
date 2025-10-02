# Напишите программу, в которой создается текстовый файл. Имя фай-
# ла вводится пользователем. Текст для файла вводится пользователем.
# При записи текста в файл все маленькие буквы заменяются на большие
import os
import time


def boot():

    for i in range(100):
        sym = "█"  * i
        time.sleep(0.02)  
        print(f"\r{sym}", end="", flush=True)
    print()  

def delete(name):
    try:
        os.remove(name)
        print("Файл удален")
    except PermissionError:
        print("У вас нет прав на удаления этого файла ")
    except FileNotFoundError:
        print("Файл не найден ")
    except Exception as e:
        print(f"Ошибка при удалении {e} ")

def file_w(name, file):
    """Функция записывает в фаил"""
    
    with open(name, "w") as fw:
        fw.write(file)  


def upper_lower(txt):
    """Функция инвертирует верхний и нижний регистр"""
    
    res = []
    for i in txt:
        if i == i.upper():
            res.append(i.lower())
        elif i == i.lower():
            res.append(i.upper())
    return "".join(res)


def main():
    try:
        us_name_file = input("Введите имя файла:\n")
        us_data_text = upper_lower(input("Введите содержимое файла:\n"))

        try:
            file_w(us_name_file, us_data_text)
            print("Фаил успешно создан.")
        except Exception:
            print("Фаил не получилось создать")

        us_ask=input("Вы хотите удалить файл:\n")

        match(us_ask):
            case "yes" | "y":
                boot()
                return delete(us_name_file)
            case "no" | "n":
                print("Файл остался в дериктории")
            case _:
                print("Вы ввели не корректное значение")
    

            
    except KeyboardInterrupt:
        print("\nСессия закончена")


if __name__ == "__main__":
    main()