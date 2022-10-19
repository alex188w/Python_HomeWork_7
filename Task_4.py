"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышает разрешенную скорость для данного автомобиля'
        else:
            return f'Скорость {self.name} в пределах допустимой для данного автомобиля'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышает разрешенную скорость для данного автомобиля'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} принадлежит полиции'
        else:
            return f'{self.name} не принадлежит полиции'


ferrari = SportCar(150, 'красная', 'Ferrari', False)
oka = TownCar(35, 'белая', 'Oka', False)
lada = WorkCar(80, 'синяя', 'Lada', True)
BMW = PoliceCar(120, 'зеленая',  'BMV', True)
print(lada.turn_left())
print(f'Сейчас {oka.turn_right()}, а {ferrari.stop()}')
print(f'{lada.go()}. {lada.show_speed()}')
print(f'{lada.name} - {lada.color}')
print(f'{ferrari.name} полицейская машина? {ferrari.is_police}')
print(f'{lada.name}  полицейская машина? {lada.is_police}')
print(ferrari.show_speed())
print(oka.show_speed())
print(BMW.police())
print(BMW.show_speed())
