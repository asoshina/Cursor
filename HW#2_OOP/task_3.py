"""
3.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
and create an HPLaptop class by using your interface.

"""
from abc import abstractmethod, ABC


class Laptop:
    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def keyboard(self):
        pass

    @abstractmethod
    def touchpad(self):
        pass

    @abstractmethod
    def webcam(self):
        pass

    @abstractmethod
    def ports(self):
        pass

    @abstractmethod
    def dynamics(self):
        pass


class HPLaptop(Laptop):
    def screen(self):
        print('HPLaptop has a screen')

    def keyboard(self):
        print('HPLaptop has a keyboard')

    def touchpad(self):
        print('HPLaptop has a touchpad')

    def webcam(self):
        print('HPLaptop has a webcam')

    def ports(self):
        print('HPLaptop has many ports')

    def dynamics(self):
        print('HPLaptop has two dynamics')


user_comp = HPLaptop()
user_comp.screen()
user_comp.keyboard()
user_comp.touchpad()
user_comp.webcam()
user_comp.ports()
user_comp.dynamics()
