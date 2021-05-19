#задача №1
get_name = input('Ваше имя - ')
s_name = input('Ваша фамилия - ')
age = input('Год рождения - ')
age = 2021 - int(age)
print('Вас зовут ', get_name,' ', s_name,'. Вам ', age, ' лет.',sep='')

#задача №2
user_time =int(input('Введите время в секундах '))
min = user_time//60
hh = min//60
ss = user_time%60
print ("%02i:%02i:%02i" % (hh,min,ss))

#задача №3
user_number = input('Введите число ')
x = user_number
y = x+x
z = x+x+x
result = int(user_number)+int(y)+int(z)
print (result)

#задача №4
user_number = int(input('Введите число '))
n = user_number
k = n % 10
n = n//10
while  n > 0:
    if n % 10 > k:
        k = n % 10
    n = n//10
print(k)

#задача №5
revenue = float(input('введите выручку '))
costs = float(input('введите издержки '))
if revenue>costs:
    print('Компания работает с прибылью!')
    profitability = (revenue-costs)/costs
    personal = int(input('введите численность сотрудников -'))
    p_revenue = (revenue-costs)/ personal
    print('Прибыль на одного сотрудника',p_revenue)
else:
    print('Компания работает с убытком!')

#задача 6
a = float(input('длительность пробежки в первый день, км '))
b = float(input('длительность пробежки в день n '))
c = 1
d = a
while c < b:
    c = c + 1
    d = d + d * 0.1
print('В выбранный Вами день пробежка составила', d)