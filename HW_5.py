#задача №1
with open("my_data.txt", "w") as f:
    my_data = []
    while True:
        my_data = input('Введите ваши данные: ')
        f.writelines(my_data+'\n')
        if my_data == '':
            break

#задача №2
lines = 0
words = 0
i = 0
with open("my_data.txt", "r") as f:
    for line in f:
        lines +=1
        words = len(line.split())
        print (f'Слов в строкe {i} - {words}')
        i = i + 1
print ('Всего строк в файле: ', lines)

#задача №3
from statistics import mean
my_word = []
pays = []
surmame = []
i = 0
with open("my_data1.txt", "r", encoding = 'utf-8' ) as f:
    for line in f:
        my_word = line.split()
        lines +=1
        pay = float(my_word[2])
        pays.append(pay)
        if pay < 20000:
            surmame.append(my_word[0])   
av_pay = round(mean(pays),2)
print(f'Сотрудники с зарплатой ниже 20000 рублей - {surmame}.')
print(f'Средняя величина дохода {av_pay} рублей.')

#задача №4
num_rus = ['Один', 'Два', 'Три', 'Четыре']
words = []
with open("secret.txt", "r", encoding='utf-8') as f, open("secret1.txt", "w", encoding='utf-8') as f1:
    i = 0
    for line in f:
        words = line.split()
        words[0] = num_rus[i]
        print(f'{words[0]} - {i+1}', file=f1)
        i +=1

#задача №5
sum_my_data_num = float()
with open("my_file_data.txt", "w", encoding='utf-8') as f:
    num = input('Введите числа через пробелы:  ')
    f.write(num)
with open("my_file_data.txt", "r", encoding='utf-8') as f:
    my_data_num = f.read()
    kol = my_data_num.split()
    for el in kol:
        el = float(el)
        sum_my_data_num +=el
    print(sum_my_data_num)

#задача №6
my_lessons = {}
my_lessons_sum ={}
with open("my_lessons.txt", "r", encoding='utf-8') as f:
    for line in f:
        key, value = line.split(':')
        my_lessons[key] = value
        key_i = key
        dt = my_lessons.get(key_i)
        number = "".join(el if el.isdigit() else " " for el in dt).split()
        sum_l = 0
        for num in number:
            sum_l += float(num)
        value = sum_l
        my_lessons_sum[key_i] = value
print(my_lessons_sum)

#задача №7
import json
data = []
profit = []
all_profit = []
all_profit_sum = 0
all_profit_mean = 0
num_company = 0
company = {}
company_profit = {}
with open("cash.txt", "r", encoding='utf-8') as f:
    dt = f.readlines()
    for line in dt:
        data = line.split()
        profit = float(data[2])-float(data[3])
        all_profit.append(profit)
        key, value = data[0], profit
        company[key] = value
    num_company = len(all_profit)
    for el in all_profit:
        if el > 0:
            all_profit_sum +=el
    all_profit_mean = all_profit_sum/num_company
    key, value = 'Средняя прибыль компаний составила', all_profit_mean
    company_profit[key] = value
    result = [company, company_profit]
    print(result)
with open("company.json", "w") as write_f:
    json.dump(result, write_f)


