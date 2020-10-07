from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def run(self):
        pass


class Car(Vehicle):
    def run(self):
        print("Car is running")


# obj = Vehicle() ==> Can not create instance for a abstract class
obj = Car() # Must define and override the abstract method in this class
# obj.run() ==> Not recommended
Car.run(obj)





