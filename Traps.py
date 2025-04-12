import random

class Traps:
    def __init__(self):
        trap_kinds = ["Drop down", "Fall into", "Shooting", "Close from the sides"]
        trap_kind = random.choice(trap_kinds)
        match trap_kind:
            case "Drop down":
                self.damage = random.randint(100,200) 
                self.trap_name = random.choice(["Siling", "Tree", "Spikes"])
                self.length = random.randint(70,150) 
                self.width = random.randint(70,150)
                self.durability =  random.randint(150,300)
                self.force = random.randint(100,200)
            case "Fall into":
                self.damage = random.randint(100,200) 
                self.trap_name = random.choice(["hole", "pit"])
                self.length = random.randint(70,150) 
                self.width = random.randint(70,150)
                self.durability =  random.randint(150,300)
                self.force = random.randint(100,200)
            case "Shooting":
                self.damage = random.randint(100,200) 
                self.trap_name = random.choice(["arrows", "Spikes"])
                self.length = random.randint(70,150) 
                self.width = random.randint(70,150)
                self.durability =  random.randint(150,300)
                self.force = random.randint(100,200)
            case "Close from the sides":
                self.damage = random.randint(100,200) 
                self.trap_name = random.choice(["spike walls", "walls"])
                self.length = random.randint(70,150) 
                self.width = random.randint(70,150)
                self.durability =  random.randint(150,300)
                self.force = random.randint(100,200)
            case _:
                self.durability = 0
                self.length = 0
                self.damage = 0
                self.width = 0
        self.trap_kind = trap_kind

    def display_info(self):
        print(f"trap_kind: {self.trap_kind}")
        print(f"trap_name: {self.trap_name}")
        print(f"length: {self.length}")
        print(f"width: {self.width}")
        print(f"damage: {self.damage}")
        print(f"durability: {self.durability}")
        print(f"force: {self.force}")
        print()
    
    def get_trap_kind(self):
        return self.trap_kind
    
        