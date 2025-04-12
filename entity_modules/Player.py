from map.Position import Position
from entity_modules.Entity import Entity
from usable.Items import Item
from Attack import Attack

class Player(Entity):

    def __init__(self, items = [], consumables = [], tames = []):
        super().__init__()
        self.items = items
        self.consumables = consumables
        self.damage = 1
        self.health = 1000
        self.attacks = [Attack("kick",self.damage * 60 ),Attack("Panch",self.damage * 60 - 10)]
        self.max_health = 1000
        self.xp_to_next_level = 100
        self.tames = tames

    def tame(self,tame: Entity):
        if len(self.get_tames()) >= 2:
            print("You can only tame 2 cretures you have the following options:")
            print("1. Dont tame")
            print("2. Kill one of you tames")
            print("3. release one of you tames")
            player_tame_choice = int(input())
            match player_tame_choice:
                case 1:
                    return 0
                case 2 | 3: #TODO need to change some of the setting so there will be a diffrence between release and kill
                    print("Who do you want to kill:")
                    for i in len(self.get_tames()):
                        print(f"{i + 1}. {self.get_tames()[i].get_name()}")
                    player_tame_choice = int(input())
                    self.tames.remove(self.get_tames()[i].get_name())

        self.tames.append(tame)
        self.damage += int(tame.get_damage() * 0.05) * 0.1
        self.max_health += int(int(tame.get_health() * 0.01) * 0.1)

    def move_player(self, new_position):
        self.position.move_to_postion(new_position.get_position_x(),new_position.get_position_y())

    def leavel_up(self):
        print("You have been leavel UP, you new stats are:")
        self.damage = int(self.damage * 1.25)
        print(f"Damage: {self.damage}")

        self.max_health = int(self.max_health * 1.2)
        self.health = self.max_health
        print(f"Health: {self.health}")

        self.xp_to_next_level = int(self.xp_to_next_level * 1.4)

    def check_for_level_up(self) -> bool:
        if self.xp > self.xp_to_next_level:
            return True
        return False

    def get_attack_damage(self, attack):
        return self.attacks[int(attack) - 1].get_attack_damage()

    def display_attacks(self):
        for i in range(len(self.attacks)):
            print(str(i + 1) + f". {self.attacks[i].get_attack_name()}, Damage: {self.attacks[i].get_attack_damage()}")
        if self.items:
            print("3. use item")
    
    def display_all_items(self, item_or_consumeble: str = "Item"):
        if item_or_consumeble == "Item":
            for item in self.items:
                print(item.display_info())
        else:
            for consume in self.consumables:
                print(consume.display_info())

    def add_item(self,new_item: Item, item_or_consumeble: str = "Item"):
        if item_or_consumeble == "Item":
            self.items.append(new_item)
        else:
            self.consumables.append(new_item)

    def remove_item(self, item_idex, item_or_consumeble: str = "Item"):
        if item_or_consumeble == "Item":
            self.items.pop(item_idex)
        else:
            self.consumables.pop(item_idex)

    def get_all_items(self, item_or_consumeble: str = "Item") -> list[Item]:
        if item_or_consumeble == "Item":
            return self.items
        else:
            return self.consumables
    
    def get_all_items_names(self, item_or_consumeble: str = "Item") -> list[str]:
        items_names = []
        if item_or_consumeble == "Item":
            for item in self.items:
                items_names.append(item.get_useable_name())
        else:
            for consumeble in self.consumables:
                items_names.append(consumeble.get_useable_name())      

        return items_names

    def get_an_item(self, item_index, item_or_consumeble: str = "Item") -> Item:
        if item_or_consumeble == "Item":
            return self.items[item_index]
        else:
            return self.consumables[item_index]

    def get_tames(self) -> list[Entity]:
        return self.tames

    def use_consumable(self,index):
        consume = self.consumables[index]
        if consume.get_affect() == "Heal":
            self.health += consume.get_resture_health_by()
            if self.health > self.max_health:
                self.health == self.max_health
            self.consumables.pop(index)
        print(consume.get_affect())

    def display_stats(self):
        print(f"""
            health: {self.health}
            damage: {self.damage}
            xp    : {self.xp}
            xp to next level: {self.xp_to_next_level}
            tame: {self.tames}
            """)