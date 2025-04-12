import random

class Useable:
    def __init__(self, type):
        if type == "Item":
            self.type = "Item"
            items = ["Sword", "Rope", "Shield", "Knife", "Broken door", "Axe", "Stick", "Bow", "Potion", "Helmet", "Armor", "Staff", "Dagger", "Hammer",
                    "Torch", "Grapple Hook", "Smoke Bomb"]
            self.name = random.choice(items)
        else:
            self.type = "consumable"
            consumables = ["Health posion", "Barry"]
            self.name = random.choice(consumables)

    def get_useable_name(self) -> str:
        return self.name
    
    def get_type(self) -> str:
        return self.type
        