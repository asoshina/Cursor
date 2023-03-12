"""
1.a. Create a new class Human and use multiple inheritance to create Centaur class, create an instance of Centaur class
and call the common method of these classes and unique.

 class Human:
Human class, should have eat, sleep, study, work

 class Centaur(.. , ..):
Centaur class should be inherited from Human and Animal and has unique method related to it.
"""


class Human:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'Human {self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleping')

    def study(self):
        print(f'{self.name} is studying')

    def work(self):
        print(f'{self.name} is work')


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'Animal {self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')


class Centaur(Human, Animal):
    def speek(self):
        print(f'Centaur {self.name} is speeking')


centaur = Centaur('Ben')
centaur.speek()
centaur.eat()
