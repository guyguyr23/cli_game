import random
from Attack import Attack
class Item:
    def __init__(self):
        items = ["Sword", "Rope", "Shield", "Knife", "Broken door", "Axe", "Stick", "Bow", "Potion", "Helmet", "Armor", "Staff", "Dagger", "Hammer",
                 "Torch", "Grapple Hook", "Smoke Bomb"]
        item_name = random.choice(items)
        match item_name:
            case "Stick":
                self.durability = random.randint(30, 100)
                self.length = random.randint(30, 140)
                self.damage = random.randint(20, 100)
                self.width = random.randint(5, 15)
                self.attackes = [Attack("Hit", self.damage), Attack("Quick Attack", self.damage - 20)]
            case "Axe":
                self.durability = random.randint(65, 130)
                self.length = random.randint(40, 80)
                self.damage = random.randint(90, 180)
                self.width = random.randint(10, 20)
                self.attackes = [Attack("Chop", self.damage), Attack("Cleave", self.damage + 10)]
            case "Sword":
                self.durability = random.randint(50, 100)
                self.length = random.randint(40, 150)
                self.damage = random.randint(100, 200)
                self.width = random.randint(10, 20)
                self.attackes = [Attack("Slash", self.damage), Attack("Thrust", self.damage + 20)]
            case "Knife":
                self.durability = random.randint(30, 70)
                self.length = random.randint(15, 30)
                self.damage = random.randint(70, 150)
                self.width = random.randint(7, 15)
                self.attackes = [Attack("Stab", self.damage), Attack("Slice", self.damage - 10)]
            case "Rope":
                self.durability = random.randint(20, 80)
                self.length = random.randint(50, 300)
                self.damage = random.randint(10, 30)
                self.width = random.randint(5, 20)
                self.attackes = [Attack("Strangle", self.damage),Attack("Whip", self.damage + 10 )]
            case "Shield":
                self.durability = random.randint(100, 300)
                self.length = random.randint(40, 120)
                self.damage = random.randint(30, 60)
                self.width = random.randint(40, 120)
                self.attackes = [Attack("Bash", self.damage)]
            case "Broken door":
                self.durability = random.randint(80, 120)
                self.length = random.randint(200, 220)
                self.damage = random.randint(30, 70)
                self.width = random.randint(80, 110)
                self.attackes = [Attack("Smash", self.damage)]
            case "Bow":
                self.durability = random.randint(40, 80)
                self.length = random.randint(100, 180)
                self.damage = random.randint(70, 120)
                self.width = random.randint(10, 20)
                self.attackes = [Attack("Shoot", self.damage), Attack("Quick Shot", self.damage + 10)]
            case "Potion":
                self.durability = 1  # For potions, durability can be set to 1 as they are consumable
                self.length = 4
                self.damage = 2
                self.width = 5
                self.attackes = [Attack("Throw",self.damage)]
            case "Helmet":
                self.durability = random.randint(80, 150)
                self.length = random.randint(20, 30)
                self.damage = 0  # Helmets don't deal damage
                self.width = random.randint(20, 30)
                self.attackes = [Attack("Throw",self.damage)]
            case "Armor":
                self.durability = random.randint(150, 300)
                self.length = random.randint(50, 80)
                self.damage = 0  # Armor doesn't deal damage
                self.width = random.randint(40, 80)
                self.attackes = [Attack("Throw",self.damage)]
            case "Staff":
                self.durability = random.randint(50, 100)
                self.length = random.randint(100, 180)
                self.damage = random.randint(60, 120)
                self.width = random.randint(5, 15)
                self.attackes = [Attack("Smash", self.damage), Attack("Fire ball", self.damage + 10)]
            case "Dagger":
                self.durability = random.randint(20, 60)
                self.length = random.randint(10, 25)
                self.damage = random.randint(40, 80)
                self.width = random.randint(3, 8)
                self.attackes = [Attack("Stab", self.damage), Attack("Lunge", self.damage + 10)]
            case "Hammer":
                self.durability = random.randint(70, 120)
                self.length = random.randint(30, 50)
                self.damage = random.randint(80, 140)
                self.width = random.randint(10, 20)
                self.attackes = [Attack("Smash", self.damage), Attack("Crush", self.damage + 20)]
            case "Torch":
                self.durability = random.randint(20, 50)
                self.length = random.randint(10, 20)
                self.damage = random.randint(30, 50)
                self.width = random.randint(3, 6)
                self.attackes = [Attack("Burn", self.damage)]
            case "Grapple Hook":
                self.durability = random.randint(30, 60)
                self.length = random.randint(10, 20)
                self.damage = 30  # Grapple hooks don't deal damage
                self.width = random.randint(5, 10)
                self.attackes = [Attack("Hook", self.damage)]
            case "Smoke Bomb":
                self.durability = random.randint(5, 15)
                self.length = 0
                self.damage = random.randint(10, 30)
                self.width = random.randint(5, 10)
                self.attackes = [Attack("Disorient", self.damage)]
            case _:
                self.durability = 0
                self.length = 0
                self.damage = 0
                self.width = 0
                self.attackes = []
        self.item_name = item_name

    def display_info(self):
        print(f"item_name: {self.item_name}")
        print(f"durability: {self.durability}")
        print(f"length: {self.length}")
        print(f"width: {self.width}")
        print(f"damage: {self.damage}")
    
    def get_attacks(self):
        return self.attackes

    def get_item_name(self):
        return self.item_name
    
    def get_length(self):
        return self.length
    
    def get_durability(self):
        return self.durability

    def get_width(self):
        return self.width

    def get_damage(self):
        return self.damage
    
    def take_damage(self, damage_taken):
        self.durability -= damage_taken
        return self.durability
        