import random


class Person:
    def __init__(self, name='noname', age=None, money=0, home=[]):
        self.name = name
        self.age = age
        self.money = money
        self.home = home

    def provide(self):
        print(f'My name is {self.name}, I am {self.age} years old')
        print(f'Availability of money: {self.money}')
        if self.home:
            print(f'My property: {self.home}')
        else:
            print('I haven\'t propety')

    def earn(self, amount):
        self.money += amount
        print(f'\nI earned {amount}$')
        print(f'Availability of money: {self.money}$\n')

    def buy(self, home):
        if self.money >= home.cost:
            self.home.append(home)
            self.money -= home.cost
            print(f'I bought: {home}')
            print(f'Availability of money: {self.money}$')


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def discount(self, percent):
        self.cost -= self.cost * percent / 100
        print(f'Now this house costs {self.cost}')

    def __repr__(self):
        return f'This house costs {self.cost}$ and his area is {self.area}'


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=SingletonMeta):
    def __init__(self, name, houses, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def provide(self):
        if self.houses:
            print(f'I am {self.name}')
            for count, house in enumerate(self.houses):
                print(f'{count+1}) This house costs {house.cost}$ and his area is {house.area}')

    def give_discount(self, house):
        print(f'\nThis house costs {house.cost} and I\'ll give you discount {self.discount}%')
        house.discount(self.discount)

    @staticmethod
    def steal(somebody):
        n = random.randint(0, 100)
        if n <= 10:
            somebody.money = 0
            print('\nRealtor steal you money')
        else:
            print('\nRealtor coudn\'t steal you money')


if __name__ == "__main__":
    small_house = House(40, 35000)
    small_house_1 = House(40, 40000)
    houses = [small_house, small_house_1]
    house1 = [small_house_1, small_house_1]

# *Realtor:

# There is only one realtor who handles small houses you wanna buy. (Singleton) Realtor is only one in your city and can:

    # проверим, что риэлтор это Singleton
    # создаем два экземпляра класса с разными данными и видим, что в двух экземплярах данные первого экземпляра
    realtor = Realtor('Realtor_John', houses, 15)
    realtor_1 = Realtor('Realtor_Mary', house1, 20)
    # if id(realtor) == id(realtor_1):
    #     print("Singleton works, both variables contain the same instance.")
    # else:
    #     print("Singleton failed, variables contain different instances.")
# Provide information about all the Houses
    realtor.provide()
    realtor_1.provide()

# Give a discount
    realtor.give_discount(small_house)


# There is a Person whose characteristics are:
# Name
# Age
# Availability of money
# Having your own home
    person = Person('Alex', 37, 200000)
# Human can:
# Provide information about yourself
    print()
    person.provide()
# Make money
    person.earn(30000)
# Buy a house
    person.buy(small_house)


# Realter can steal your money with 10% chance
    realtor.steal(person)
