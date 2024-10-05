class Toy:
    def __init__(self, name, color, typie):
        self.name = name
        self.color = color
        self.typie = typie

    def get_info(self):
        print(f'\nИмя: {self.name} \nЦвет: {self.color} \nТип: {self.typie}')

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
        return Toy(name, color, typie)

toyFactory = ToyFactory()

toy1 = toyFactory.make_Toy('toy1', 'black', 'mult')
toy1.get_info()
