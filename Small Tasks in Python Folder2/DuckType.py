class Animal():
    alive = True



class Dog(Animal):
 

    def speak(self):
        print("Woooof")


class Cat(Animal):
    

    def speak(self):
        print("Meooow")


class Car():
    
    alive = False

    def speak(self):
        print("Honkkkkk!!!")        



animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

    