"""
1. Сreate a class hierarchy of animals with at least 5 animals that have additional methods each, create an instance for
 each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class
class Animals:
Parent class, should have eat, sleep

class Animal1(Animal):
Some of the animal with 1-2 extra methods related to this animal
"""


class Animals:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')


class Dog(Animals):
    def bark(self):
        print(f'Dog {self.name} is barking')


class Cat(Animals):
    def mew(self):
        print(f'Cat {self.name} is meowing now')


class Fish(Animals):
    def swim(self):
        print(f'Fish {self.name} is swimming now')


class Cow(Animals):
    def moo(self):
        print(f'Cow {self.name} is mooing now')


class Pig(Animals):
    def grunt(self):
        print(f'Pig {self.name} is grunting now')


dog = Dog('Rex')
dog.bark()
cat = Cat('Vasiliy')
cat.mew()
fish = Fish('Bubble')
fish.swim()
cow = Cow('Marysa')
cow.moo()
pig = Pig('Hrusha')
pig.grunt()