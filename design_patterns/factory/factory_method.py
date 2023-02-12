from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def beep(self) -> str:
        pass

    @abstractmethod
    def info(self):
        pass


class AutoCompanyFactory(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> None:
        car = self.factory_method()
        print(car.beep())
        print(car.info())


class Mercedes(AutoCompanyFactory):
    def factory_method(self) -> Car:
        return SClass()


class Toyota(AutoCompanyFactory):
    def factory_method(self) -> Car:
        return Camry()


class Camry(Car):
    mark = 'Toyota'
    model = 'Camry'

    def beep(self) -> str:
        return "Beep in Japanese"

    def info(self):
        return {
            'mark': self.mark,
            'model': self.model,
        }


class SClass(Car):
    mark = 'Mercedes'
    model = 'S'

    def beep(self) -> str:
        return "Beep in German"

    def info(self):
        return {
            'mark': self.mark,
            'model': self.model,
        }


if __name__ == "__main__":
    Mercedes().some_operation()
    Toyota().some_operation()
