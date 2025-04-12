from entity_modules.Entity import Entity
import random
from Attack import Attack

class Animal(Entity):
    def __init__(self):
        super().__init__()

        # Level 1 animals
        animal_names_level_1 = ["Mouse", "Wolf", "Lion", "Fox", "Snake", "Tiger", "Eagle", "Pig", "Bat", "Deer"]
        # Level 2 animals
        animal_names_level_2 = ["Bear", "Panther", "Crocodile", "Rhino", "Leopard"]
        # Level 3 animals
        animal_names_level_3 = ["Dragon", "Griffin", "Phoenix", "Hydra"]

        if self.level == 1:
            animal_name = random.choice(animal_names_level_1)
        elif self.level == 2:
            animal_name = random.choice(animal_names_level_2 + animal_names_level_1)
        elif self.level == 3:
            animal_name = random.choice(animal_names_level_3 + animal_names_level_2)
        
        # Match for Level 1 animals
        match animal_name:
            case "Mouse":
                self.damage = random.randint(100, 200)
                self.height = random.randint(3, 6)
                self.width = random.randint(4, 7)
                self.health = random.randint(300, 400)
                self.attacks = [Attack("bite", self.damage)]
            case "Lion":
                self.damage = random.randint(70, 120)
                self.height = random.randint(90, 140)
                self.width = random.randint(50, 70)
                self.health = random.randint(150, 300)
                self.attacks = [Attack("bite", self.damage), Attack("scratch", self.damage - 10), Attack("roar", self.damage - 20)]
            case "Wolf":
                self.damage = random.randint(70, 110)
                self.height = random.randint(70, 120)
                self.width = random.randint(30, 60)
                self.health = random.randint(130, 270)
                self.attacks = [Attack("bite", self.damage), Attack("dash", self.damage + 10)]
            case "Fox":
                self.damage = random.randint(50, 80)
                self.height = random.randint(60, 80)
                self.width = random.randint(20, 50)
                self.health = random.randint(80, 150)
                self.attacks = [Attack("bite", self.damage), Attack("jump attack", self.damage + 10)]
            case "Snake":
                self.damage = random.randint(60, 100)
                self.height = random.randint(5, 15)
                self.width = random.randint(5, 20)
                self.health = random.randint(100, 200)
                self.attacks = [Attack("bite", self.damage), Attack("constrict", self.damage + 15)]
            case "Tiger":
                self.damage = random.randint(80, 130)
                self.height = random.randint(90, 120)
                self.width = random.randint(50, 80)
                self.health = random.randint(180, 320)
                self.attacks = [Attack("bite", self.damage), Attack("claw", self.damage + 20), Attack("pounce", self.damage + 15)]
            case "Eagle":
                self.damage = random.randint(40, 70)
                self.height = random.randint(30, 50)
                self.width = random.randint(10, 30)
                self.health = random.randint(60, 120)
                self.attacks = [Attack("talon slash", self.damage), Attack("dive", self.damage + 20)]
            case "Pig":
                self.damage = random.randint(30, 60)
                self.height = random.randint(50, 70)
                self.width = random.randint(30, 50)
                self.health = random.randint(100, 180)
                self.attacks = [Attack("charge", self.damage), Attack("tusk strike", self.damage + 10)]
            case "Bat":
                self.damage = random.randint(30, 50)
                self.height = random.randint(5, 10)
                self.width = random.randint(15, 30)
                self.health = random.randint(50, 100)
                self.attacks = [Attack("bite", self.damage), Attack("sonic screech", self.damage + 10)]
            case "Deer":
                self.damage = random.randint(40, 70)
                self.height = random.randint(100, 120)
                self.width = random.randint(40, 60)
                self.health = random.randint(100, 200)
                self.attacks = [Attack("antler strike", self.damage), Attack("kick", self.damage + 15)]
            
        # Match for Level 2 animals
        match animal_name:
            case "Bear":
                self.damage = random.randint(100, 150)
                self.height = random.randint(150, 180)
                self.width = random.randint(80, 100)
                self.health = random.randint(400, 500)
                self.attacks = [Attack("claw swipe", self.damage), Attack("bite", self.damage + 20), Attack("roar", self.damage - 30)]
            case "Panther":
                self.damage = random.randint(90, 140)
                self.height = random.randint(70, 100)
                self.width = random.randint(40, 70)
                self.health = random.randint(200, 400)
                self.attacks = [Attack("bite", self.damage), Attack("claw", self.damage + 15), Attack("pounce", self.damage + 10)]
            case "Crocodile":
                self.damage = random.randint(110, 160)
                self.height = random.randint(50, 80)
                self.width = random.randint(40, 90)
                self.health = random.randint(300, 450)
                self.attacks = [Attack("bite", self.damage), Attack("tail swipe", self.damage + 20), Attack("death roll", self.damage + 30)]
            case "Rhino":
                self.damage = random.randint(130, 180)
                self.height = random.randint(160, 200)
                self.width = random.randint(80, 120)
                self.health = random.randint(500, 600)
                self.attacks = [Attack("charge", self.damage), Attack("gore", self.damage + 25)]
            case "Leopard":
                self.damage = random.randint(80, 130)
                self.height = random.randint(60, 80)
                self.width = random.randint(40, 60)
                self.health = random.randint(180, 300)
                self.attacks = [Attack("bite", self.damage), Attack("claw", self.damage + 15), Attack("leap attack", self.damage + 10)]

        # Match for Level 3 animals
        match animal_name:
            case "Dragon":
                self.damage = random.randint(200, 300)
                self.height = random.randint(200, 300)
                self.width = random.randint(150, 200)
                self.health = random.randint(1000, 1500)
                self.attacks = [Attack("fire breath", self.damage + 50), Attack("bite", self.damage), Attack("tail swipe", self.damage + 30)]
            case "Griffin":
                self.damage = random.randint(180, 250)
                self.height = random.randint(180, 220)
                self.width = random.randint(100, 140)
                self.health = random.randint(800, 1200)
                self.attacks = [Attack("bite", self.damage), Attack("claw", self.damage + 20), Attack("wing buffet", self.damage + 25)]
            case "Phoenix":
                self.damage = random.randint(150, 220)
                self.height = random.randint(160, 200)
                self.width = random.randint(80, 100)
                self.health = random.randint(700, 1000)
                self.attacks = [Attack("flame burst", self.damage + 40), Attack("talon strike", self.damage), Attack("rebirth", self.damage - 50)]
            case "Hydra":
                self.damage = random.randint(190, 280)
                self.height = random.randint(100, 180)
                self.width = random.randint(100, 180)
                self.health = random.randint(1200, 1600)
                self.attacks = [Attack("bite", self.damage), Attack("multiple heads strike", self.damage + 60), Attack("regenerate", self.damage - 50)]

        self.animal_name = animal_name
        self.max_health = self.health
        self.xp = self.health / 10 + self.damage / 5

    def display_info(self):
        print(f"Animal name: {self.animal_name}")
        print(f"Height: {self.height}")
        print(f"Width: {self.width}")
        print(f"Health: {self.health}")

    def get_max_health(self) -> int:
        return self.max_health

    def get_damage(self) -> int:
        return self.damage

    def get_name(self) -> str:
        return self.animal_name

    def get_an_attack(self) -> Attack:
        return random.choice(self.attacks)

    # def get_attacks(self) -> list[Attack]:
    #     return self.attacks
