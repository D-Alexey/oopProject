class TownCar:
    def __init__(self, speed=200, color='белый'):
        self.speed = speed
        self.color = color
        self.name = 'Городская машина'
        self.is_police = False

    def go(self):
        print(self.name + ' поехала')

    def stop(self):
        print(self.name + ' остановилась')

    def turn(self, direction):
        print(self.name + ' повернула ' + direction)

    def get_info(self):
        print(f'Скорость: {self.speed}')
        print(f'Цвет: {self.color}')
        print(f'Имя: {self.name}')
        print(f'Машина полицейская: {self.is_police}')

class SportCar:
    def __init__(self, speed=300, color='красный'):
        self.speed = speed
        self.color = color
        self.name = 'Спортивная машина'
        self.is_police = False

    def go(self):
        print(self.name + ' поехала')

    def stop(self):
        print(self.name + ' остановилась')

    def turn(self, direction):
        print(self.name + ' повернула ' + direction)

    def get_info(self):
        print(f'Скорость: {self.speed}')
        print(f'Цвет: {self.color}')
        print(f'Имя: {self.name}')
        print(f'Машина полицейская: {self.is_police}')

class WorkCar:
    def __init__(self, speed=200, color='черный'):
        self.speed = speed
        self.color = color
        self.name = 'Рабочая машина'
        self.is_police = False

    def go(self):
        print(self.name + ' поехала')

    def stop(self):
        print(self.name + ' остановилась')

    def turn(self, direction):
        print(self.name + ' повернула ' + direction)

    def get_info(self):
        print(f'Скорость: {self.speed}')
        print(f'Цвет: {self.color}')
        print(f'Имя: {self.name}')
        print(f'Машина полицейская: {self.is_police}')

class Car:
    def __init__(self, speed=200, color='синий'):
        self.speed = speed
        self.color = color
        self.name = 'Полицейская машина'
        self.is_police = True

    def go(self):
        print(self.name + ' поехала')

    def stop(self):
        print(self.name + ' остановилась')

    def turn(self, direction):
        print(self.name + ' повернула ' + direction)

    def get_info(self):
        print(f'Скорость: {self.speed}')
        print(f'Цвет: {self.color}')
        print(f'Имя: {self.name}')
        print(f'Машина полицейская: {self.is_police}')
