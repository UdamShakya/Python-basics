# inheritance_polymorphism_abcs.py
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def move(self) -> str:
        pass

class DriveMixin:
    def drive(self) -> str:
        return f"{self.name} is driving on the road."

class FlyMixin:
    def fly(self) -> str:
        return f"{self.name} is flying in the sky."

class Car(Vehicle, DriveMixin):
    def move(self) -> str:
        return self.drive()

class Plane(Vehicle, FlyMixin):
    def move(self) -> str:
        return self.fly()

# Demonstrates polymorphism: treat different Vehicle subclasses the same
def operate(vehicle: Vehicle) -> None:
    print(vehicle.move())

if __name__ == "__main__":
    c = Car("Sedan")
    p = Plane("Boeing")
    for v in (c, p):
        operate(v)

    # MRO example: show method resolution order
    print("Car MRO:", [c.__name__ for c in Car.__mro__])
