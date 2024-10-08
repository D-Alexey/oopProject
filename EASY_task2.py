class Car:
    def __init__(self, speed=0, color='', is_police=False):
        self.speed = speed
        self.color = color
        self.name = 'Машина'
        self.is_police = is_police

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

    def crash(self, target):
        print(f'{self.name} столкнулась с {target.name}')

class TownCar(Car):
    def __init__(self, speed = 200, color = 'белый'):
        super().__init__(speed, color, 'Городская машина')

class SportCar(Car):
    def __init__(self, speed = 300, color = 'красный'):
        super().__init__(speed, color, 'Спортивная машина')

class WorkCar(Car):
    def __init__(self, speed = 200, color = 'черный'):
        super().__init__(speed, color, 'Рабочая машина')

class PoliceCar(Car):
    def __init__(self, speed = 200, color = 'синий'):
        super().__init__(speed, color, 'Полицейская машина', True)

car1 = SportCar()
car2 = WorkCar()
car1.crash(car2)