class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"{self.__model}:<название модели транспорта>"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def set_color(self, color):
        if color in self.__COLOR_VARIANTS:
            self.__color = color
        else:
            print(f"Цвет {color} не доступен. Выберите один из вариантов: {', '.join(self.__COLOR_VARIANTS)}.")

    def print_info(self):
        print(self.get_model())
        print(f"Владелец: {self.owner}")
        print(self.get_horsepower())
        print(self.get_color())


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()

# Меняем свойства
vehicle1.set_color('Pink')  # Это не допустимо, так как цвет не существует
vehicle1.set_color('black')  # Это допустимо, так как цвет существует

vehicle1.owner = 'Vasyok'

# Проверяем, что поменялось
vehicle1.print_info()
