from random import randint

class Person:
    def __init__(self, health, damage, armor, name='none'):
        self.health = health
        self.damage = damage
        self.armor = armor
        self.name = name

    def __damage_calc(self, target):
        damage = self.damage + randint(-5, 5) - target.armor
        print(f'Урон: {damage}')
        return damage

    def attack(self, target):
        damage = self.__damage_calc(target)
        print(f'\nУ {target.name}а {target.health} здоровья!')
        target.health -= damage
        print(f'{self.name} нанёс {damage} урона!')
        print(f'Теперь у {target.name}а {target.health} здоровья!')

    def get_info(self):
        print(f'\n{self.name}: {self.health}hp, {self.damage}dmg, {self.armor}arm')

class Player(Person):
    def __init__(self, health=100, damage=30, armor=20):
        super().__init__(health, damage, armor, 'Игрок')

class Enemy(Person):
    def __init__(self, health=70, damage=35, armor=20):
        super().__init__(health, damage, armor, 'Враг')

class Fight:
    def __init__(self, fighter_1, fighter_2):
        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2

    def start_fight(self):
        while True:
            self.fighter_1.attack(self.fighter_2)
            if self.fighter_2.health < 1:
                print(f'\n{self.fighter_1.name} победил!')
                break
            self.fighter_2.attack(self.fighter_1)
            if self.fighter_1.health < 1:
                print(f'\n{self.fighter_2.name} победил!')
                break

player = Player()
enemy = Enemy()
fight = Fight(player, enemy)
fight.start_fight()
