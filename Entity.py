from Position import Position

class Entity:
    def __init__(self, health=100,attack_power=30, position=Position()):
        self.health = health
        self.attack_power = attack_power
        self.position = position

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
    