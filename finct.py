# def user_hello(user_name,):
#     """ПРОСТО СПРАШИВАЕТ У ПОЛЬЗОВАТЕЛЯ ИМЯ """
#     print(f"{user_name},привет")

# user_in=input("Введите свое имя :")
# user_hello(user_in)

# --------------------------------------------------------------------------------------------------------------------
# def make_shirt (user_size,user_print):
#     print(f"{user_size} - {user_print}")

# while 1:
#     user_size=input('Введите свой размер ')
#     if not user_size.isdigit():
#         print("Вы ввели не корректно значение ")
#         continue
#     user_print=input("Введите текст ")
#     make_shirt(user_size,user_print)
#     make_shirt(user_size="36",user_print="ебала")
# -----------------------------------------------------------------------------------------------------------------------
# def user_format(user_fist,user_last,age="") :
#     if age:
#         full_name=f"{user_fist} {user_last} {age}"
#     else:
#         full_name=f"{user_fist} {user_last}"
    
#     return full_name.title()

# user_in=input("Введите свое имя :")
# user_last=input("Введите свою фамилию :")
# user_age=input("ХОТИТЕ СКАЗАТЬ СКОЛЬКО ВАМ ЛЕТ ? (yes|no)")
# user_age.lower()
# while 1:
#     if user_age=="yes":
#         user_age=input("Сколько?")
#         musician=user_format(user_in,user_last,user_age)
#         break
#     elif user_age=="no":
#         musician=user_format(user_in,user_last)
#         break
#     else:
#         user_age=input(" либо yes либо no")
# print(musician)
# -------------------------------------------------------------------------------------------------------------------------
# def build_persen(user_name,user_age):
#     person={"name":user_name,"age":user_age}
#     return person

# user_name=input("Введите свою имя :")
# user_age=input("Введите свой возраст :")

# person_data=build_persen(user_name,user_age)

# for key,valeo in person_data.items():
#     print(f"{key}-{valeo}")
#--------------------------------------------------------------------------------------------------------------------------
# def greet_user(names):
#     """Приветствует пользователя."""
#     for name in names:
#         msg=f"hello {name}"
#         print(msg)


# user_name=['ilya','lilo','kata']
# greet_user(user_name)
# ------------------------------------------------------------------------------------------------------------------------
# import tqdm 
# import time

# def print_model (unprint_model,complited_model):
#     while unprint_model:
#         current_desig=unprint_model.pop()
#         print(f"Печать моделей {current_desig}")
#         complited_model.append(current_desig)
        
# def show_complited_model(complited_model):
#     print("Вывод всего что напечатано ")
#     for complited in complited_model:
#         print(complited)
        
        
# unprint_model=['ilya','lilo',"locke"]
# complited_model=[]

# print_model (unprint_model[:],complited_model)

# for _ in tqdm.tqdm(range(50)):
#     time.sleep(0.25)  

# show_complited_model(complited_model)
# ------------------------------------------------------------------------------------------------------------------------------------
# def new_func():
#     def make_pizza(*topping):
#         for i in topping:
#             if i=='ilya':
#                 print("жопа")

#     make_pizza('ilya','lilo')

# new_func()
# -----------------------------------------------------------------------------------------------------------------------------------
# import tqdm
# user_file=input("Введите имя файла ")

# file_path = user_file
# if os.path.exists(file_path):
#     print(f"Файл {file_path} существует")
# else:
#     print(f"Файл {file_path} не существует")
# class Dog():
#     """ self-ссылка на экземляр 
#     класс-это своего рода инструкция по созданию экземпляра """
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def sit(self):
#         print(f"{self.name} hello,sit")

#     def roll_over(self):
#         print(f"{self.name},roll over")
# my_dog=Dog('lilo',6)
# ----------------------------------------------------------------------------------------------------------------------
# print(f"{my_dog.name}\nhe {my_dog.age} age")
# my_dog.sit()
# my_dog.roll_over()
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type

#     def describe_restaurant(self):
#         print(f"\nНазвание ресторана:{self.restaurant_name}\nВид кухни:{self.cuisine_type}")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name}-открыт")

# my_rest=Restaurant("Tokio-citi","Японская")
# my_rest1=Restaurant("Евразия","Европейская")
# my_rest2=Restaurant("Бургер-Кинг","Говно")

# # print(f"{my_rest1.restaurant_name}")

# my_rest.describe_restaurant()

# my_rest1.describe_restaurant()

# my_rest2.describe_restaurant()
# ----------------------------------------------------------------------------------------------------------------
# class User():
#     def __init__(self,first_name,last_name,age,local):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#         self.local=local

#     def describe_user(self):
#         user_data=f"ФИО:{self.first_name} {self.last_name} \nВозраст:{self.age}\nМесто проживания:{self.local}"
#         print(user_data.title())

#     def greet_user(self):
#         print(f"Привет,{self.first_name}.")

# user_ilya=User('ilya','sennikov',"25",'Архангельск')

# user_ilya.describe_user()
# user_ilya.greet_user() 
#--------------------------------------------------------------------------------------------------------------
class Car():
    """Простая модель автомобиля  """
    def __init__(self,make,model,age):
        self.make = make.title()
        self.model = model.title()
        self.age = age
        self.odometer_reading=10


    def info(self):
        return(f"Полная информация об авто:\nМарка:{self.make}\nМодель:{self.model}\nВозраст:{self.age} age")
    
    def read_odometer(self):
        print(f"Пробег у авто:{self.odometer_reading} Км")
    
    def update_odometer(self,km):
        if km>= self.odometer_reading:
            self.odometer_reading=km
        else:
            print("Вы ПЫТАЕТЬСЯ СКРУТИТЬ ПРОБЕГ")
    def increment_odometer(self,kms):
        """Увеличения пробега"""
        self.odometer_reading+=kms
    def fille_gas_tank(self):
        print("ПОЛНЫЙ БАК")
    def obnul_odomentr(self):
        self.odometer_reading=0
        

my_car=Car("bmw","m2","23")
# user_odometr=int(input("Введите пробег авто:(когда вы его купили)"))
# if user_odometr<my_car.odometer_reading:
#     print("вы ввели не корректное значение ")
# else:
#     my_car.update_odometer(user_odometr)
#     user_prob=int(input("Введите сколько вы проехали км :"))
#     my_car.increment_odometer(user_prob)
#     # my_car.obnul_odomentr()
#     my_car.read_odometer()

class ElectroCar(Car):
    def __init__(self, make, model, age):
        """Инициализирует атрибуты класса-родителя"""
        super().__init__(make, model, age)
        self.el_battery=75
    def size_battery(self):
        """Размер батареи"""
        return(f"Размер батареи : {self.el_battery} А/Ч " )
    def fille_gas_tank(self):
        print("В электромобиле нет бензобака ")
my_tesla=ElectroCar("Tesla","m-s","2019")
BAT=my_tesla.size_battery()
print(f"{my_tesla.info()} {my_car.info()} {BAT}")
my_tesla.fille_gas_tank()
my_car.fille_gas_tank()



