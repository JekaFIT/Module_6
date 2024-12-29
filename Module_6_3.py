from random import random, randint


class Animal:
    _DEGREE_OF_DANGER = 0
    live = True
    sound = None

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
       new_x = self._cords[0] + dx * self.speed
       new_y = self._cords[1] + dy * self.speed
       new_z = self._cords[2] + dz * self.speed
       if new_z < 0:
           print("It's too deep, i can't dive :(")
       else:
           self._cords = [new_x, new_y, new_z]

    def get_cords(self):
        x, y, z = self._cords
        return f"X: {x}, Y: {y}, Z: {z}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        if self.sound:
            print(f"Животное говорит: {self.sound}")
        else:
            print("Животное молчит.")

class Bird(Animal):
    beak = True

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        eggs = randint(1, 4)
        print(f"Here are {eggs} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        dz = abs(dz)
        new_z = self._cords[2] - dz * (self.speed / 2)
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = new_z
            print(f"Животное нырнуло. Новые координаты: {self._cords}")

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed):
        super().__init__(speed)

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        Bird.__init__(self, speed)
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()

db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()

db.lay_eggs()








