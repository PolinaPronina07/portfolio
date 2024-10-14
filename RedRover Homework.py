"""1 УРОК ДЗ"""
from asyncio import wait_for

'''  1
 Установить python: https://www.python.org/downloads/
 Установить PyCharm: https://www.jetbrains.com/ru-ru/pycharm/download/'''


'''- Вывести строку "Hello world!" (без кавычек) в консоль.'''

'''print("Hello world!")'''


'''  3
 Посмотрите на следующие переменные:
 1num = 100 - нельзя начинать с цифр имя переменной
 имя = “Алексей” - нельзя кириллицей писать имя переменной
 First_Number = 1 - имя переменной всегда нижним регистром
 “Мой текст” = text - имя переменной нельзя писать кириллицей и в кавычках
 phone_number = “Hi!” - имя переменной не соответствует смыслу значения
 Что с ними не так? Как бы вы их исправили?'''


'''4'''
'''Создать переменную name со значением в виде строки своего имени. 
 Затем вывести строку на экран в виде:
 "Привет, меня зовут <ваше имя>."
 Попробуйте выполнить эту задачу разными способами'''

'''name = 'Polina'
print (f'Привет, меня зовут {name}.')
print ("Привет, меня зовут" + " " + name + ".")'''


'''  5
 Создать переменную name, значение которой определяется через ввод данных с клавиатуры.
 Создать переменную surname, значение которой определяется через ввод данных с клавиатуры.
 Вывести на экран строку "Привет, меня зовут <имя> <фамилия>.". Значение переменных name и surname должно быть отформатировано к корректному виду. Например, если с клавиатуры вводятся строки "еЛеНА" и "поПОВА", то результат должен быть "Привет, меня зовут Елена Попова." '''

'''name = input()
surname = input()
correct_name = name.title()
correct_surname = surname.title()
print (f"Привет, меня зовут {correct_name} {correct_surname}.")'''


'''  6
 Создать переменную a, значение которой определяется через ввод данных с клавиатуры.
 Создать переменную b, значение которой определяется через ввод данных с клавиатуры.
 Вывести на экран сумму двух введенных чисел, если для a было введено 123, а для b 431, то на экран должно быть выведено 554.'''

'''a = input()
b= input()
print (int(a) + int(b))'''



"""2 УРОК ДЗ"""

# 1
'''Создать переменную n, значение которой определяется через ввод данных
с клавиатуры.
Если n является четным числом, то вывести на экран слово “четное”.
Если n является нечетным числом, то вывести на экран слово “нечетное”'''

'''n = int(input())
if n % 2 == 0:
    print("чётное")
if n % 2 != 0:
    print("нечётное")'''

# 2
'''Создать переменную day, значение которой определяется через ввод
данных с клавиатуры.
- Если значение day равно “суббота” или “воскресенье”, то вывести на
экран строку “Сегодня выходной!”.
- Если значение day равно “среда”, то вывести на экран “Мне сегодня к
стоматологу в 15:30”.
- Во всех остальных случая выводить на экран “Сегодня обычный день.”'''

'''day = input()
if day == "суббота" or day == "воскресенье":
    print("Сегодня выходной!")
elif day == "среда":
    print("Мне сегодня к стоматологу в 15:30.")
else:
    print("Сегодня обычный день.")'''


# 3
'''Создать переменную n, значение которой определяется через ввод данных
с клавиатуры (целое число).
- Создать переменную text, значение которой определяется через ввод
данных с клавиатуры (строка).
- Программа должна вывести вашу строку text на экран n-раз. Если вы ввели
3, а затем “Ау”, то результат должен быть:
Ау
Ау
Ау'''

'''n = int(input())
text = str(input())
print((text + "\n") * n)'''


# 4
'''- Создать переменную message, значение которой определяется через ввод
данных с клавиатуры.
- Программа должна вывести на экран количество гласных букв в строке
message. Например, если была введена строка “Мой кот уверен, что
клавиатура – это специально для него купленный массажер”, то
программа должна вывести 26.
 Подразумевается, что подсчитываться должна только кириллица, то есть буквы а, о, у, ы и так далее. '''

'''message = input()
glasnaya = 'аеёиоыуэюяАЕЁИОЫУЭЮЯ' # Определяем набор гласных букв кириллицы
count_glasnaya = sum(1 for char in message if char in glasnaya) # Подсчитываем количество гласных в строке message, 1 обозначает, что считаем каждый символ
print(count_glasnaya) # Выводим результат'''

# 5
'''Программа должна запрашивать у пользователя ввести число с клавиатуры.
После того как пользователь ввел число (пользователь должен вводить только целые числа),
она должна опять попросить его ввести число и так должно продолжаться пока пользователь не введет отрицательное число. 
Как только пользователь ввел отрицательное число, программа должна вывести сумму всех чисел, которые он вводил до этого (не включая отрицательное) и завершиться.'''

'''number = 0
sum = 0

while number >= 0:
    sum += number
    number = int(input("Введите целое число:"))

print(sum)'''


"""3 УРОК ДЗ"""

#1
'''- Сгенерируйте список numbers, состоящий из чисел в диапазоне от 0 до 100
включительно, которые делятся без остатка как на 2, так и на 3.
- Выведите список numbers на экран.

Ответ: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
# Решите эту задачу в 2 способа - с помощью генератора списков и без него.'''


'''numbers = list(range(101)) #без генератора
print([number for number in numbers if number % 2 == 0 and number % 3 == 0])'''

'''numbers = [i for i in range(101) if i % 2 == 0 and i % 3 == 0] # с генератором
print(numbers)'''

#2
'''Имеется список items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
- Составьте новый список numbers, который содержит только целые числа
(int) и вещественные числа (float) из списка items.
- Выведите на экран сумму чисел в numbers.'''

'''items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
numbers = []
for value in items:
    if type(value) == int or type(value) == float:
        numbers.append(value)
print(sum(numbers))'''

#3
'''- Создать список messages, который будет хранить “сообщения”.
- Программа должна в бесконечном цикле запрашивать у пользователя
ввести сообщение (строку) с клавиатуры и сохранять ее в список messages.
Причем программа должна запоминать не более 5 последних сообщений.
То есть, если длина списка messages превысила 5, то первое сообщение в
нем должно быть удалено.
- Если пользователь ввел “Пока”, то программа должна вывести “Ну ладно,
пока!” и список последних сообщения на экран.'''

'''messages = []
flag = 0
while True:
 message = list(input("Введите сообщение ").split('/n'))
 messages.extend(message)
 flag = flag + 1
 if flag <= 5 and "Пока" not in messages:
    print(messages)
 if "Пока" in messages:
     print("Ну ладно, пока!")
     print (messages)
     break
 if flag >= 5:
    messages.pop(0)
    flag = 4'''

#4
'''Без дубликатов.

Имеется список numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
- Создайте новый список, где будут удалены все дубликаты из списка
numbers.
- Отсортируйте итоговый список и выведите на экран.
Ответ: [1, 3, 4, 5, 6, 7, 8, 9, 15, 23, 42]
# Решите задачу с использованием множества и без него.'''

'''numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
new_numbers = list(set(numbers)) #с множеством
print(sorted(new_numbers))'''

'''numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
new_numbers = []
for i in numbers: #без множества
    if i not in new_numbers:
     new_numbers.append(i)
print(sorted(new_numbers))'''


"""4 УРОК ДЗ"""

#1
'''Продвинутый sum.
Встроенная функция sum() в python вызывает ошибку, если один из элементов
последовательности не является числом, например sum([1, 2, ‘A’]).
- Напишите функцию sum_ignore_non_numbers(), которая имеет один
параметр items (список или кортеж).
- Функция должна вернуть сумму всех чисел (int, float) в переданной
последовательности. При этом все нечисловые значения должны
игнорироваться.
- Если чисел нет, то функция должна вернуть 0.
Если вызвать функцию со списком [1, 2, 'Hey', None, 4.3], то она должна вернуть 7.3'''

'''def sum_ignore_non_numbers(items):
 total = 0
 for item in items:
  if isinstance(item, (int, float)):
   total += item
 return total

items = [1, 2, 'Hey', None, 4.3]
print (sum_ignore_non_numbers(items))'''

#2
'''Треугольник возможен, если сумма любых двух его сторон больше длины третьей
стороны.
- Напишите функцию is_triangle(), которая имеет 3 параметра - длины сторон
треугольника.
- Функция должна возвращать True, если треугольник с переданными
сторонами может существовать, и False в противном случае.
Для is_triangle(2, 4, 9) правильный ответ - False, для is_triangle(3, 4, 5) - True.'''

'''def is_triangle(a, b, c):
    add = a + b
    if add > c:
     return True
    else:
     return False

print(is_triangle(1, 2, 4))'''

#3
'''Напишите функцию average(), которая принимает произвольное
количество позиционных аргументов. (Можно передать любое число
аргументов).
- Функция должна посчитать среднее арифметическое всех переданных
чисел. (Представим, что в функцию передаются только числа).
- Если не передать ни одного аргумента, то функция должна вернуть 0.

Такой вызова функции average(1, 2, 3, 4, 5, 6, 7, 8) должен вернуть 4.5'''

'''def average(*args):
 if args:
  aver = sum(args) / len(args)
  return aver
 else:
  return 0
print (average(1, 2, 3, 4, 5, 6, 7, 8))'''

#4
'''Напишите функцию common_strings(), которая имеет 3 параметра: list1,
list2 и ingore_case=True (значение по умолчанию).
- Функция должна вернуть новых список из тех значений, которые
встречаются в обоих списках. При этом, если ignore_case равен True, то
функция должна игнорировать регистр и считать строки “string” и “STRING”
одинаковыми. В противном случае функция должна учитывать регистр
символов и считать такие строки разными.
- Все строки в результирующем списке должны быть в нижнем регистре.
Например, существуют 2 списка:
fruits_1 = [‘banana’, ‘APPLE’, ‘watermelon’, ‘cherry’]
fruits_2 = [‘Mango’, ‘apple’, ‘orange’, ‘cherry’]
То вызов функции common_strings(fruits_1, fruits_2) должен вернуть [‘apple’,
‘cherry’].'''

'''def common_strings(list1, list2, ingore_case=True):
 list_one = [i.lower() for i in list1]
 list_two = [i.lower() for i in list2]
 list3 = list(set(list_one) & set(list_two))
 return list3

fruits_1 = ["banana", "APPLE", "watermelon", "cherry"]
fruits_2 = ["Mango", "apple", "orange", "cherry"]
print (common_strings(fruits_1, fruits_2))'''

#5
'''- Для всех функций из задач 1-4 напишите подробную строку документации.
- Создайте отдельный файл functions и переместите туда все эти
функции.
- Создайте новый файл (или используйте старый рабочий файл) в той же
рабочей директории и импортируйте в него функции из functions.
- Запустите импортированные функции с разными аргументами.'''

#from functions import sum_ignore_non_numbers, is_triangle, average, common_strings


"""5 УРОК ДЗ"""
#1
'''Прямоугольник
- Создайте класс Rectangle, который принимает ширину и высоту
прямоугольника при создании и должен иметь соответствующие атрибуты
width и height (целые числа).
- Создайте метод area(), который возвращает площадь прямоугольника.
- Создайте метод perimeter(), который возвращает периметр
прямоугольника.
Пример:
rect = Rectangle(2, 4)
a = rect.area() # Вернул 8
p = rect.perimeter() # Вернул 12'''

'''class Rectangle:
 def __init__(self, width, height):
    self.width = width
    self.height = height
 def area(self):
    return self.width * self.height
 def perimeter(self):
    return (self.width + self.height) * 2

rect = Rectangle(2, 4)
a = rect.area()
p = rect.perimeter()'''

#2
'''- Создайте класс Car, который принимает марку автомобиля (make) в виде
строки и максимально возможную скорость (max_speed) в виде целого
числа при создании. Также при инициализации (в теле __init__) экземпляра
Car должен быть автоматически создан атрибут speed, равный 0 (текущая
скорость автомобиля).
- Создайте метод display_speed(), который выводит в консоль текущую
скорость автомобиля.
- Создайте метод accelerate(), который увеличивает скорость автомобиля на
10, при этом скорость автомобиля не должна превышать max_speed, если
вызывается accelerate() при максимальной скорости, то скорость не
должна увеличиваться.
- Создайте метод brake(), который уменьшает скорость автомобиля на 10,
при этом скорость автомобиля не может быть меньше 0. Если вызывается
метод brake() при скорости равной 0, то скорость не должна уменьшаться.
Пример:
my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed() # вывел в консоль 30'''

'''class Car:
 def __init__(self, mark, max_speed):
    self.mark = mark
    self.max_speed = max_speed
    self.speed = 0
 def display_speed(self):
    return self.speed
 def accelerate(self):
    if self.speed >= self.max_speed:
        return self.speed
    if self.speed < self.max_speed:
        self.speed = self.speed + 10
        return self.speed

 def brake(self):
    if self.speed <= 0:
        return self.speed
    if self.speed > 0:
        self.speed = self.speed - 10
        return self.speed

my_toyota = Car("Toyota", 180)
print(my_toyota.accelerate())
print(my_toyota.accelerate())
print(my_toyota.brake())
print(my_toyota.display_speed())'''


#3
'''- Создайте класс BankAccount, который принимает имя владельца (name) в
виде строки и текущее состояние счета (balance) в виде целого числа. Оба
этих атрибута должны быть _защищенным.
- Создайте метод deposit(), который принимает 1 аргумент (если не считать
self, конечно) amount (целое число). Метод должен увеличить текущий
баланс аккаунта на amount.
- Создайте метод withdraw(), который принимает 1 аргумент amount (целое
число). Метод должен уменьшить текущий баланс аккаунта на amount. Если
денег на счету недостаточно, то метод выводит на экран “Недостаточно
средств!”.
- Создайте метод get_balance(), который возвращает текущее значение
баланса аккаунта.
Пример:
account = BankAccount("Maria", 1000)
account.deposit(700)
account.withdraw(200)
print(account.get_balance()) # 1500'''

'''class BankAccount:
 def __init__(self, _name, _balance):
    self._name = _name
    self._balance = _balance
 def deposit(self, amount):
    self._balance = self._balance + amount
    return self._balance
 def withdraw(self, amount):
    if self._balance <= 0:
        return "Недостаточно средств!"
    if self._balance > 0:
        self._balance = self._balance - amount
        return self._balance
 def get_balance(self):
        return self._balance'''

'''account = BankAccount("Maria", 1000)
account.deposit(700)
account.withdraw(200)
print(account.get_balance())'''

#4
'''- Создайте класс OverdraftAccount, унаследованный от вашего класса
BankAccount из предыдущей задачи.
- Переопределите существующий метод withdraw(), но теперь, если баланс
аккаунта меньше или равен 0, то это не выводит на экран сообщение
“Недостаточно средств!”, а уменьшает баланс в минус.
Пример:
jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)
jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance()) # -300'''

'''class OverdraftAccount(BankAccount):
 def withdraw(self, amount):
    if self._balance <= 0:
     self._balance = self._balance - amount
     return self._balance
    if self._balance > 0:
     self._balance = self._balance - amount
     return self._balance

jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)
jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance())'''


"""6 УРОК ДЗ"""
#1
'''GET
- Создайте тест для получения списка всех id всех бронирований на сайте.
- Тест считается пройденным, если status code ответа равен 200.
Сайт: https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-GetBookings'''

import requests
'''response = requests.get("https://restful-booker.herokuapp.com/booking")
print(response.status_code)
print(response.json())'''

#2
'''POST
Создайте тест, который включает в себя следующие шаги:
- Шаг 1. Создайте новое бронирование на сайте используя ваши данные.
- Шаг 2. C помощью id вашего созданного бронирования получите
информацию о вашем бронировании (через эндпоинт booking/{id}).
- Тест считается пройденным, если имя и фамилия в вашем созданном
бронировании (Шаг 1) совпадают с теми данными, которые вы получили (Шаг 2).'''
'''
data = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
response = requests.post("https://restful-booker.herokuapp.com/booking", json = data)
print(response.status_code)
print(response.json())'''

'''response = requests.get("https://restful-booker.herokuapp.com/booking/618")
print(response.status_code)
print(response.json())'''

#3
'''Создайте тест, который включает в себя следующие шаги:
- Шаг 1. Создайте новое бронирование на сайте используя ваши данные.
- Шаг 2. Создайте токен авторизации.
- Шаг 3. Измените имя и фамилию в вашей брони через метод PATCH. (не
забудьте передать в заголовке токен авторизации)
- Шаг 4. C помощью id вашего созданного бронирования получите
информацию о вашем бронировании.
- Тест считается пройденным, если имя и фамилия в вашем измененном
бронировании (Шаг 3) совпадают с теми данными, которые вы получили.
(Шаг 4)'''
def auth():
 info = {
    "username" : "admin",
    "password" : "password123"
 }
 response = requests.post("https://restful-booker.herokuapp.com/auth", json = info)
 #tokenchik = str(response.json())
 token = response.json()["token"]
 #print(response.status_code)
 return token

print (auth())

def post():
 data = {
  "firstname" : "Kris",
  "lastname" : "Brown",
  "totalprice" : 100,
  "depositpaid" : True,
  "bookingdates" : {
    "checkin" : "2018-01-01",
    "checkout" : "2019-01-01"
    },
  "additionalneeds" : "Breakfast"
  }
 response = requests.post("https://restful-booker.herokuapp.com/booking", json = data)
 #resp = str(response.json())

 #print (response.status_code)
 return response.json()

print (post())


data = {
  "firstname" : "Коля",
  "lastname" : "Лупкин"
  }
headers = {
 "Cookie": f"token = {auth()}"
 }
id = post()["bookingid"]
response = requests.patch(f"https://restful-booker.herokuapp.com/booking/{id}", data = data, headers = headers)
print(response.status_code)
print(response.json())

response = requests.get(f"https://restful-booker.herokuapp.com/booking/{id}")
print(response.status_code)
print(response.json())

#4
'''Создайте тест, который включает в себя следующие шаги:
- Шаг 1. Создайте новое бронирование на сайте используя ваши данные.
- Шаг 2. Создайте токен авторизации.
- Шаг 3. Удалите ваше бронирование по его id через метод DELETE. (не
забудьте передать в заголовке токен авторизации)
- Тест считается пройденным, если попытка получения информации о вашей
брони по ее id возвращает статус 404 (Not Found).'''

print (auth())

def create():
    data = {
        "firstname": "Pupka",
        "lastname": "Lupa",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response2 = requests.post("https://restful-booker.herokuapp.com/booking", json=data)
    return response2.json()

print (create())

id2 = create()["bookingid"]
headers = {
 "Cookie": f"token = {auth()}"
 }
response = requests.delete(f"https://restful-booker.herokuapp.com/booking/{id2}", headers = headers)
print(response.status_code)

response = requests.get(f"https://restful-booker.herokuapp.com/booking/{id2}")
print(response.status_code)
print(response.json())
























































































