from entity_modules.Player import Player
from usable.Items import Item
from usable.Consumable import Consumable
import random

def add_item_to_user(player :Player, items: list[str], player_choise: int):
    if len(player.get_all_items_names()) == 3:
        print("You have the max number of items will you need to deop 1, or not take new item")
        print("1. drop item")
        print("2. keep items")
        user_keep_item_input = input()
        if int(user_keep_item_input) == 1:
            for_count = 1
            for item in player.get_all_items_names():
                print(f"{for_count}. {item}")
                for_count+=1
            user_drop_item_input = input()
            print(f"You have droped the item and got {items[int(player_choise)].get_useable_name()}")
            player.remove_item(int(user_drop_item_input) -1 )
            player.add_item(items[int(player_choise)])

    else:
        player.add_item(items[int(player_choise)])

def create_item_for_player():
    options = ["Items", "Items", "Consumable"]
    player_item = random.choice(options)
    if player_item == "Items":
        return Item()
    else:
        return Consumable()
    
def turn_item(player: Player):
    first_item = create_item_for_player()
    second_item = create_item_for_player()
    third_item = create_item_for_player()
    
    items = [first_item, second_item, third_item]
    print("You have found this 3 items you may take only 1:")
    print(f"1. {first_item.get_useable_name()}")
    print(f"2. {second_item.get_useable_name()}")
    print(f"3. {third_item.get_useable_name()}")
    print("To display more info about the items input E/e to select the item input the item number")
    
    user_item_input = input()
    if user_item_input.isnumeric():
        user_item_input = int(user_item_input)
        if items[user_item_input - 1].get_type() == "Item":
            add_item_to_user(player,items,int(user_item_input) - 1)
        else:
            player.add_item(items[user_item_input - 1],"consumeble")
        # player.add_item(items[int(user_item_input) - 1])

    elif user_item_input == "E" or user_item_input == "e":
        for item in items:
            item.display_info()
            print()
        user_item_input = int(input())
        # user_item_input = int(user_item_input)
        if items[user_item_input - 1].get_type() == "Item":
            add_item_to_user(player,items,int(user_item_input) - 1)
        else:        
            player.add_item(items[user_item_input - 1],"consumeble")
