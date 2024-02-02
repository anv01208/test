class Car:
    def __init__(self, make, model, year, color, sound):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.sound = sound

    def __str__(self):
        res = f"Автомобиль {self.year} года производства, модель: {self.model}, цвет: {self.color}, страна: {self.make}"
        return res

    def engine_on(self):
        print(self.sound)


toyota = Car('Japan', 'Camry 3.5', '2022', 'Black', 'V6 sound!')
ferrari = Car('Italy', 'F140', '2002', 'Red', 'V12 sound!!!')

print(toyota)
toyota.engine_on()
print('---------------------------------------')
print(ferrari)
ferrari.engine_on()
print('---------------------------------------')


class Moto(Car):
    def __init__(self, make, model, year, color, sound):
        super().__init__(make, model, year, color, sound)

    def __str__(self):
        res = f"Мотоцикл {self.year} года производства, модель: {self.model}, цвет: {self.color}, страна: {self.make}"
        return res


honda_cbr = Moto('Japan', 'CBR 600 RR', '2007', 'Blue', 'Woom-Woom')

print(honda_cbr)
honda_cbr.engine_on()
