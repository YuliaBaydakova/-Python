#задача №1
user_list = ['Шоколад', 195, 562.5, None, False]
for el in user_list:
    print(type(el),sep=',  ')

#задача №2
user_list1 = []
el = int(input('Введите количество элементов списка '))
i = 0
while True:
    if i <= el-1:
        unit = input('Введите элемент списка ')
        user_list1.append(unit)
    else:
        break
    i = i + 1
print(user_list1)
j = 0
for i in range(int(el/2)):
     user_list1[j], user_list1[j + 1] =  user_list1[j+1], user_list1[j]
     j = j + 2
print(user_list1)

#задача №3
number_month = int(input('введите № месяца в году '))
list_months = ['зима','весна','лето','осень']
if number_month >=3 and number_month <=5:
    print(list_months[1])
elif number_month >=6 and number_month <=8:
    print(list_months[2])
elif number_month >=9 and number_month <=11:
    print(list_months[3])
else:
    print(list_months[0])
dict_months = {1:'зима', 2:'зима', 3:'весна', 4:'весна', 5:'весна', 6:'лето', 7:'лето', 8:'лето', 9:'осень',10:'осень',11:'осень',12:'зима'}
print (dict_months.get(number_month))

#задача №4
user = []
user = input('введите данные через пробелы ')
i = 1
for el in user.split(sep=' '):
    print(f'{i} {el}') if len(el)<10 else print(f'{i} {el[0:10]}')
    i +=1

#задача №5
my_list = [7, 5, 3, 3, 2]
user_number = float (input('Введите число '))
a = my_list.count(user_number)
min_number = min(my_list)
max_number = max(my_list)
if a==0 and min_number >user_number:
    my_list.append(user_number)
elif a==0 and max_number<user_number:
    my_list.insert(0, user_number)
else:
    i = 0
    for el in my_list:
        if  user_number<=el:
            i+=1
    my_list.insert(i,user_number)
print (my_list)

#задача №6
products = []
features = {'наименование': '','цена': '','количество': '','ед. измерения': ''}
analytics = {'наименование': [],'цена':[],'количество': [],'ед. измерения': []}
i = 0
while True:
    if input('Для выхода из приложения нажмите "Q", для продолжения нажмите "Enter":').upper()=='Q':
        break
    i +=1
    for f in features.keys():
        products_key = input(f'Введите значение свойства {f} ')
        features[f] = int(products_key) if (f=='цена' or f=='количество') else products_key
        analytics[f].append(features[f])
    products.append((i,features.copy()))
    print(f'Cтруктура товаров: {products}')
    print(f'Аналитика: ')
    for key, value in analytics.items():
        print(f'{key[:25]:>25}:{value}')
