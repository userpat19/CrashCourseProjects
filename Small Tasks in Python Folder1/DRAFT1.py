# BASIC IMPLEMENTATION OF CLASS INHERITANCE IN PYTHON
# THIS PROGRAM IS A ONLINE SHOPPING KIND OF PLATFORM

class Character():
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def take_damage(self, amount):
        self.health -= amount
    
    def display_damage(self):
        return f"Damage capability: {self.damage}/s"

class Warrior(Character):
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed)
        self.counter_damage = 0.80
        self.damage_multiplier = 1.45

    def take_damage(self, amount):
        modified_damage = amount * self.counter_damage
        super().take_damage(modified_damage)

    def spartan_rage(self):
        self.damage *= self.damage_multiplier

class Ninja(Character):
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed)
        self.counter_damage = 0.90
        self.damage_multiplier = 2.45

    def take_damage(self, amount):
        modified_damage = amount * self.counter_damage
        super().take_damage(modified_damage)

    def killintent(self):
        self.damage *= self.damage_multiplier

warrior = Warrior(100, 3, 45)
print(f"Initial Health: {warrior.health}")
warrior.take_damage(45)
print(f"Your health is at {warrior.health}")
print(f"{warrior.display_damage()}")
warrior.spartan_rage()
print(f"Spartan Rage Damage: {warrior.display_damage()}/s")

print("---------------------------------------")

ninja = Ninja(100, 5, 78)
print(f"Initial Health: {ninja.health}")
ninja.take_damage(45)
print(f"Your health is at {ninja.health}")
print(f"{ninja.display_damage()}")
ninja.killintent()
print(ninja.display_damage())