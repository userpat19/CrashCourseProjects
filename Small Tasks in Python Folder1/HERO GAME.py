class Character():
    def __init__(self, name, health, mana, attack_power, defense):
        self.name = name
        self.health = health
        self.mana = mana
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, opponent):
        if opponent.defense > 0:
            opponent.defense -= self.attack_power
        else:
            opponent.health -= self.attack_power
    def take_damage(self , opponent, amount):
        if self.defense > 0:
            self.defense -= opponent.attack_power
        else:
            self.health -= opponent.attack_power
    def health_boost(self):
        self.health += 10
    def display_stats(self):
        print(f"Player Name: {self.name}")
        print(f"Current Health: {self.health}")
        print(f"Current Mana: {self.mana}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Defense: {self.defense}")

class Warrior(Character):
    def __init__(self, name, health, mana, attack_power, defense):
        super().__init__(name, health, mana, attack_power, defense)

        self.toughness_perk = 0.80

    def shield_block(self , opponent, shield_health):
        if shield_health > 0:
            modified_amount = opponent.attack_power * self.toughness_perk
            super().take_damage(opponent , modified_amount)
            print("The Warrior used the ShieldBlock ability: reduces the damage by 20%")
            shield_health -= 1
        else:
            print("The Warrior has no shield block left")
        

class Mage(Character):
    def __init__(self, name, health, mana, attack_power, defense):
        super().__init__(name, health, mana, attack_power, defense)

        self.attack_mult = 1.20

    def cast_spell(self, opponent):

        if self.mana > 0:
            modified_amount = self.attack_power * self.attack_mult
            super().attack(opponent, modified_amount)
        else:
            print("Not enough mana to generate a spell")

class Archer(Character):
     def __init__(self, name, health, mana, attack_power, defense):
        super().__init__(name, health, mana, attack_power, defense)

        self.arrows_damage = 1.25

     def shoot_arrows(self, opponent):
         modified_amount = self.attack_power * self.arrows_damage
         super().attack(opponent , modified_amount)

         #MAIN FUNCTIONALITY IS GOOD NA, BUT STILL LACK IN TERMS OF HERO'S CAPABILITY TO USE UNIQUE SKILL

username = input("Username:")

warrior = Warrior(username, 100 , 0 , 9 , 50)
mage = Mage(username, 100 , 25 , 7 , 25)
archer = Archer(username, 100 , 0 , 8 , 35)
shield = 5

def main():

    while True:
        print("---------------------------------")
        print("            HERO TYPE            ")
        print("---------------------------------")
        print("1.Warrior")
        print("2.Mage")
        print("3.Archer")
        Role = input("Role:")

        while True:

            if Role == "1":
                print("1.Pick a opponent")
                print("2.Use Base Attack")
                choice = input("Enter:")

                match choice:
                    case "1":
                        print("Availabe Opponents: Archer and Mage")
                        Opponent = input("Opponent:") 

                    case "2":
                        if Opponent == "Archer":
                            print("---------------------------------------")
                            print(f"Archer Prev health: {archer.health}")
                            print(f"Archer Prev defense health: {archer.defense}")
                            print("---------------------------------------")
                            warrior.attack(archer)
                            print("'The Warrior ⚔️ strikes the Archer using his base attack'")
                            print("---------------------------------------")
                            print(f"Archer After Damage health: {archer.health}")
                            print(f"Archer After Damage defense health: {archer.defense}")
                            print("---------------------------------------")
                        if Opponent == "Mage":
                            print("---------------------------------------")
                            print(f"Mage Prev health: {mage.health}")
                            print(f"Mage Prev defense health: {mage.defense}")
                            print("---------------------------------------") 
                            warrior.attack(mage)
                            print("'The Warrior ⚔️ strikes the Mage using his base attack'")
                            print("---------------------------------------") 
                            print(f"Mage After Damage health: {mage.health}")
                            print(f"Mage After Damage defense health: {mage.defense}")
                            print("---------------------------------------") 
                        

            elif Role == "2":
                 print("1.Pick a opponent")
                 print("2.Use Base Attack")
                 choice = input("Enter:")

                 match choice:
                    case "1":
                        print("Availabe Opponents: Archer and Warrior")
                        Opponent = input("Opponent:") 

                    case "2":
                        if Opponent == "Archer":
                            print("---------------------------------------") 
                            print(f"Archer Prev health: {archer.health}")
                            print(f"Archer Prev defense health: {archer.defense}")
                            print("---------------------------------------") 
                            mage.attack(archer)
                            print("The mage 🧙 casted a damage spell against the Archer")
                            print("---------------------------------------") 
                            print(f"Archer After Damage health: {archer.health}")
                            print(f"Archer After Damage defense health: {archer.defense}")
                            print("---------------------------------------") 
                        if Opponent == "Warrior":
                            print("---------------------------------------") 
                            print(f"Warrior Prev health: {warrior.health}")
                            print(f"Warrior Prev defense health: {warrior.defense}")
                            print("---------------------------------------") 
                            mage.attack(warrior)
                            print("The mage 🧙 casted a damage spell against the Warrior")
                            print("---------------------------------------") 
                            print(f"Warrior After Damage health: {warrior.health}")
                            print(f"Warrior After Damage defense health: {warrior.defense}")
                            print("---------------------------------------") 
            elif Role == "3":
                 print("1.Pick a opponent")
                 print("2.Use Base Attack")
                 choice = input("Enter:")

                 match choice:
                    case "1":
                        print("Availabe Opponents: Warrior and Mage")
                        Opponent = input("Opponent:") 

                    case "2":
                        if Opponent == "Warrior":
                            print("---------------------------------------") 
                            print(f"Warrior Prev health: {warrior.health}")
                            print(f"Warrior Prev defense health: {warrior.defense}")
                            print("---------------------------------------") 
                            print("The archer 🏹 shot at the warrior")
                            if shield > 0:
                               warrior.shield_block(archer , shield)
                               print("Block By warrior")
                            else:
                                print("Shieldd lives expires")
                                archer.attack(warrior)
                            print("---------------------------------------") 
                            print(f"Warrior After Damage health: {warrior.health}")
                            print(f"Warrior After Damage defense health: {warrior.defense}")
                            print("---------------------------------------") 
                        if Opponent == "Mage":
                            print("---------------------------------------") 
                            print(f"Mage Prev health: {mage.health}")
                            print(f"Mage Prev defense health: {mage.defense}")
                            print("---------------------------------------") 
                            archer.attack(mage)
                            print("The archer 🏹 shot at the mage")
                            print("---------------------------------------") 
                            print(f"Mage After Damage health: {mage.health}")
                            print(f"Mage After Damage defense health: {mage.defense}")
                            print("---------------------------------------") 
            else:
                print("Please pick among the three roles")




if __name__ == "__main__":
    main()
