#задача №1
from time import sleep
class TrafficLight():
    __color = ['red', 'yellow', 'green']
    def running (self):
        while True:
            print ('red')
            sleep(7)
            print ('yellow')
            sleep(2)
            print ('green')
            sleep(10)
            print ('yellow')
            sleep(2)
            break


Trafficlight_1 = TrafficLight()
Trafficlight_1.running()

#задача №2
class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.depth = 5
        self.massa_width = 25
    def massa(self):
        work_massa = self._length *self._width*self.depth*self.massa_width/1000
        print (f'Необходимая масса асфальта {work_massa} тонн')
    
    
road_1 = Road(5000, 20)
road_1.massa()

#задача №3
class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    
    def get_full_name (self):
        print (f'{self.name} {self.surname} - {self.position}')
    
    def get_total_income (self):
        print (f'Уровень дохода - {sum(self._income.values())}.')

director = Position('Иван', 'Иванов', 'Генеральный директор', 150, 50)
director.get_full_name()
director.get_total_income()

#задача №4
class Car():
    def __init__(self,  speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

        
    def go (self):
        print (f'{self.name}: машина поехала!')
    
    def stop(self):
        print (f'{self.name}: машина остановилась.')
        
    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} повернула {"направо" if {self.direction} == 0 else "налево"}.')
        
    def show_speed(self):
        print(f'{self.name}: cкорость движения автомобиля - {self.speed} км/ч.')
    
class TownCar(Car):
    
    def show_speed (self):
         print(f'{self.name}: превышение скорости! Скорость движения - {self.speed} км/ч') if self.speed > 60  else print(f'{self.name}: скорость движения - {self.speed} км/ч')
    
class WorkCar(Car):
    
    def show_speed (self):
        print(f'{self.name}: превышение скорости! Скорость движения - {self.speed} км/ч') if self.speed > 40  else print(f'{self.name}: скорость движения - {self.speed} км/ч')
       
class PoliceCar (Car):
    def __init__(self, speed, color, name, is_police=True):
            super().__init__(self, speed, color, name, is_police=True)

class SportCar(Car):
    pass

police = Car(140, 'белый', 'Lada', True)     
police.go()
police.show_speed()

tractor = WorkCar(60, 'оражевый', 'Bobcat', False)
tractor.show_speed()
tractor.turn(0)
tractor.stop()

skoda = TownCar(80, 'оражевый', 'Skoda', False)
skoda.show_speed()
skoda.stop()

#задача 5
class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки!')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки - {self.title}!')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки - {self.title}!')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки - {self.title}!')

red_pencil = Pencil('красный карандаш')
red_pencil.draw()

green_handle = Handle('зеленый маркер')
green_handle.draw()

blue_pen = Pen('голубая ручка')
blue_pen.draw()