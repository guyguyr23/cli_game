from map.Position import Position
from Attack import Attack

class Entity:
    def __init__(self, health=200,attack_power=30, position=Position(), level: int = 1):
        self.health = health
        self.attack_power = attack_power
        self.position = position
        self.damage = 1
        self.xp = 0
        self.level = level
        self.attacks = []
    def get_damage(self):
        return self.damage

    def add_health(self,health_to_add: int):
        self.health += health_to_add

    def set_health(self, health):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage

    def check_death(self):
        if self.health <= 0:
            return True
        return False

    def get_health(self):
        return self.health
    
    def get_entity_position(self):
        return self.position
    
    def get_xp(self):
        return self.xp

    def add_xp(self,xp):
        self.xp += int(xp)

    def get_attacks(self) -> list[Attack]:
        return self.attacks