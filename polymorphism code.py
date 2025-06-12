class Cat:
    def sound(self):
        print("Meow")
class Dog:
    def sound(self):
        print("woof")
def make_sound(animal):
    animal.sound()
d=Dog()
c=Cat()
make_sound(d)
make_sound(c)