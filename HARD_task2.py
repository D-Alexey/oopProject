class Toy:
    def __init__(self, name, color, typie):
        self.name = name
        self.color = color
        self.typie = typie

    def get_info(self):
        print(f'\nИмя: {self.name} \nЦвет: {self.color} \nТип: {self.typie}')

class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, 'Животное')

class MultikToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, 'Мультфильм')

class ToyFactory:
    def __purchase(self):
        print('Сырьё закуплено')

    def __sewing(self):
        print('Пошив закончен')

    def __painting(self):
        print('Покраска закончена')

    def make_Toy(self, name, color, typie):
        self.__purchase()
        self.__sewing()
        self.__painting()
        match typie:
            case 'животное':
                return AnimalToy(name, color)
            case 'мультфильм':
                return MultikToy(name, color)
            case _:
                print(f'Игрушки типа "{typie}" не производятся.')
                exit()

toyFactory = ToyFactory()

animalToy = toyFactory.make_Toy('Игрушка', 'Чёрный', 'мультфильм')
animalToy.get_info()
