import random
from entity_modules.Player import Player
from usable.Useable import *

class Consumable(Useable):
    def __init__(self):
        super().__init__("Consumable")
        match self.name:
            case "Health posion":
                self.affect = "Heal"
                self.resture_health_by = random.randint(200, 400)
                # self.width = random.randint(5, 15)
                # self.attackes = [Attack("Hit", self.damage), Attack("Quick Attack", self.damage - 20)]
            case "Barry":
                self.affect = "Heal"
                self.resture_health_by = random.randint(100, 200)
            case _:
                self.affect = ""
                self.resture_health_by = 0
        self.consumable_name = self.name

    def display_info(self):
        print(f"consumable_name: {self.consumable_name}")
        print(f"affect: {self.affect}")
        if self.affect == "Heal":
            print(f"health by: {self.resture_health_by}")
    
    def get_affect(self) -> str:
        return self.affect

    def get_resture_health_by(self) -> int:
        return self.resture_health_by
    
    def constume(self,player: Player):
        match self.affect:
            case "Heal":
                player.add_health(self.resture_health_by)
            case _:
                print("")
        