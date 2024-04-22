from Position import Position
from Entity import Entity
from Items import Item
class Player(Entity):

    def __init__(self, items = []):
        super().__init__()
        self.items = items

    def move_player(self, new_position):
        self.position.move_to_postion(new_position.get_position_x(),new_position.get_position_y())
    
    def add_item(self,new_item: Item):
        self.items.append(new_item)

    def get_all_items(self):
        return self.items
    
    def get_all_items_names(self):
        items_names = []
        for item in self.items:
            items_names.append(item.get_item_name())
        return items_names

    def get_an_item(self, item_index):
        return self.items[item_index]
