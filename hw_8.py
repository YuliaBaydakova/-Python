#задача 1
class Data:

    @classmethod
    def num_of_date (cls, user_date):
        result =''.join(user_date)
        day = int(result.split('-')[0])
        month = int(result.split('-')[1])
        year = int(result.split('-')[2])
        print (f'Число месяца {day}, месяц {month}, год {year}')

    @staticmethod
    def check_month(user_date):
        result = ''.join(user_date)
        month = int(result.split('-')[1])
        if month >=13 or month <1:
            print(f'Дата введена не корректно!')

user_date = list(input('Ввведите дату в формате ''день-месяц-год'' '))
Data.num_of_date(user_date)
Data.check_month(user_date)

#задача 2
class MyError(Exception):
    def __init__(self,txt):
        self.txt = txt

inp_data_1 = int(input("Введите делимое число: "))
inp_data_2 = int(input("Введите делитель числа: "))

try:
    if inp_data_2 == 0:
        raise MyError("Вы ввели ноль!На ноль делить запрещено!")
    result = inp_data_1/inp_data_2
except ValueError:
    print("Вы ввели не число!")
except MyError as e:
    print(e)
else:
    print(f'Все хорошо! Результат операции {result}')

#задача 3
class Check(Exception):
    def __init__(self, txt):
        self.txt = txt

data_list = []
while True:
    inp_data = input("Введите число: ")
    if inp_data=='':
        break
    try:
        if inp_data.isdigit() == False:
            raise Check('Введенные Вами данные не являются числом!')
        if inp_data.isdigit() == True:
            data_list.append(inp_data)
    except Check as e:
        print(e)
print(data_list)

#задачи 4-6

class Sklad:
    def __init__(self):
        self._dict = {}

    def move_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def move_from(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop()

class Equipment:
    def __init__(self, name, model, num):
        self.name = name
        self.model = model
        self.num = num
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.model} {self.num}'

class Printer(Equipment):
    def func(self):
        print(f'печать документов')

class Scanner(Equipment):
    def func(self):
        print(f'сканирование документов')

class Сopier(Equipment):
    def func(self):
        print(f'копирование документов')

class Check(Exception):
    def __init__(self, txt):
        self.txt = txt

sklad = Sklad()
scanner = Scanner('HP', 321, 1)
sklad.move_to(scanner)
printer = Printer ('Самсунг', 2052, 1)
sklad.move_to(printer)
xerox = Сopier('Canon', 856, 1)
sklad.move_to(xerox)

#механизм валидации вводимых пользователем данных
model = input('Введите цифровой код модели ')
try:
    if model.isdigit() == False:
        raise Check('Введенные Вами данные не являются цифрами!')
except Check as e:
    print(e)
    model = input('Введите корректные данные ')

xerox = Сopier('HP', model, 1)
sklad.move_to(xerox)
print(f'На склад поступило {sklad._dict}')
sklad.move_from('Сopier')
print(f'На складе остались {sklad._dict}')

#задача 7
class СomplNumber():
    def __init__(self, x, y):
        self.x = complex(x).real
        self.y = complex(y).imag
    def __add__(self, other):
         sum_r = self.x+other.x
         sum_i = self.y+other.y
         return complex(sum_r,sum_i)
    def __mul__(self, other):
            return complex(self.x, self.y)*complex(other.x, other.y)

num_a = СomplNumber(5, 3j)
num_b = СomplNumber(5, 2j)
print(num_a+num_b)
print(num_a*num_b)

