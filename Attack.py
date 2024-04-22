
class Attack:
    def __init__(self, attack_name, attack_damage):
        self.attack_name = attack_name
        self.attack_damage = attack_damage

    def get_attack_name(self):
        return self.attack_name

    def get_attack_damage(self):
        return self.attack_damage
    
    def incress_damage(self,amount):
        self.attack_damage += amount
    