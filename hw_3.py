#задача 1
num1 = float(input('введите число 1 '))
num2 = float(input('введите число 2 '))
def funct_div (num1, num2):
    try:
        result = num1 / num2
        print(result)
    except ZeroDivisionError:
        print('Деление на ноль запрещено!')
funct_div (num1, num2)

#задача 2
name = input('Введите имя: ')
surname = input('Введите вашу фамилию: ')
age = input('Введите год рождения: ')
city = input('Город проживания: ')
mail = input('Ваш адрес электроной почты: ')
tel = input('Ваш номер телефона: ')
def funct_personal (name, surname, age, city,mail,tel):
    print(f'{name} {surname}, {age} года рождения, проживает в городе {city}, адрес электронной почты {mail}, номер телефона {tel}')
funct_personal (name, surname, age, city,mail,tel)

#задача 3
arg1 = 5
arg2 = 9
arg3 = 8
def my_funct (arg1, arg2, arg3):
    print(arg1 + arg2 + arg3 - min(arg1, arg2, arg3))
my_funct(arg1, arg2, arg3)

#задача 4
x = 5
y = -3
def my_funct_pow (x, y):
    print(x**y)
my_funct_pow(x, y)

def my_funct_pow_c (x, y):
    result = 1
    i = 1
    while i <= abs(y):
        result *= 1 / x
        i = i + 1
    print(result)
my_funct_pow_c (x, y)

#задача 5
user_list = []
def my_sum():
    sum_user = 0
    while True:
        user_list = input('Введите числа разделенные пробелами ').split()
        for num in user_list:
            if num == 'q':
                return sum_user
            else:
                sum_user += float(num)
        print(sum_user)
print(my_sum())

#задача 6
word = input('Введите слово латинскими буквами ')
def word_up (word):
    set_alf = 'qwertyuiopasdfghjklzxcvbnm'
    print(word.title() if not set(word).isdisjoint(set_alf) else "ошибка!слово должно содержать только латинские буквы")
word_up (word)

word_list = input('Введите слова латинскими буквами ').split()
for el in word_list:
    result = word_up(el)
    if result:
        print (result)