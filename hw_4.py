#задача 1
from sys import argv

script_name, hours, pay, prize = argv

#print("Имя скрипта: ", script_name)
print("Выработка в часах: ", hours)
print("Ставка: ", pay)
print("Премия: ", prize)
result = int(hours)*int(pay)+int(prize)
print('Зарплата сотрудника', result)

#задача 2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
i = 1
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(new_list)

#задача 3
print([(20 + i) for i in range(20, 240) if (20+i)%20 == 0 or (20+i)%21 == 0])

#задача 4
list3 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
i = 4
a = list3.count(list3[i])
my_list3 = [list3[i] for i in range(0, len(list3)) if list3.count(list3[i]) == 1]
print(my_list3)
            
#задача 5
from functools import reduce
my_list4 = []
my_list4 = [i for i in range(100, 1000+2) if i%2 == 0]
def my_funct (prev_el, el):
    return prev_el*el
print (reduce(my_funct, my_list4))

#задача 6
from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)
k = 0
for el in cycle("Python"):
    if k > 20:
        break
    print(el)
    k += 1        

#задача 7
import math
n = 4
def generator (n):
    for el in range(1,n):
        yield math.factorial(el)

g = generator(n)
print(g)

for el in g:
    print(el)

