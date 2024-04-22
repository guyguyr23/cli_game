from Entity import Entity
import random
from Attack import Attack
class Animal(Entity):

    def __init__(self):
        super().__init__()
        animal_names = ["Mouse","Wolf","Lion","Fox"]
        animal_name = random.choice(animal_names)
        match animal_name:
            case "Mouse":
                self.damage = random.randint(100,200) 
                self.hight = random.randint(3,6)
                self.width = random.randint(4,7)
                self.health = random.randint(300,400)
                self.attacks = [Attack("bite",self.damage)]
            case "Lion":
                self.damage = random.randint(70,120) 
                self.hight = random.randint(90,140)
                self.width = random.randint(50,70)
                self.health = random.randint(150,300)
                self.attacks = [Attack("bite",self.damage), Attack("Scratch", self.damage - 10), Attack("Roar",self.damage - 20 )]
            case "Wolf":
                self.damage = random.randint(70,110) 
                self.hight = random.randint(70,120)
                self.width = random.randint(30,60)
                self.health = random.randint(130,270)
                self.attacks = [Attack("bite",self.damage), Attack("Dash", self.damage + 10)]
            case "Fox":
                self.damage = random.randint(50,80) 
                self.hight = random.randint(60,80)
                self.width = random.randint(20,50)
                self.health = random.randint(80,150)
                self.attacks = [Attack("bite",self.damage), Attack("Jump attack", self.damage + 10)]
            case _:
                self.durability = 0
        self.animal_name = animal_name

    def display_info(self):
        print(f"animal name: {self.animal_name}")
        print(f"hight: {self.hight}")
        print(f"width: {self.width}")
        print(f"health: {self.health}")
    
    def get_damage(self):
        return self.damage

    def get_attacks(self):
        return self.attackes