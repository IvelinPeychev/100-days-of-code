class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")


class Labrador(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        # self.temperament = "friendly"


buddy = Labrador('John', 20)
buddy.bark()
print(buddy.temperament)
print(buddy.name)
print(buddy.age)


class Animal:
    def __init__(self, name):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

    def increase_eyes(self):
        self.num_eyes += 1

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.num = 1

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish('Nemo')
nemo.breathe()
nemo.increase_eyes()
print(nemo.num_eyes)
nemo.increase_eyes()
print(nemo.num_eyes)
nemo.increase_eyes()
print(nemo.num_eyes)
