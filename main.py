import time
import os
from Player import Player
from map import *
from Items import Item
from Riddles import Riddle
import threading
from inputimeout import inputimeout 


def clear_screan():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_player_position(player, map):
    map[player.get_entity_position().get_position_x()][player.get_entity_position().get_position_y()] = 2
    print_map(map)

def can_move(map: list,position: Position):
    if check_bounds(len(map[0]),position) and map[position.get_position_x()][position.get_position_y()] == 1:
        return True
    return False

def next_posible_pisitions(map: list,current_position: Position):
    posible_position = []
    # print(current_position.get_next_possiotn_x())
    if can_move(map,current_position.get_next_possiotn_x()):
        posible_position.append("Stright")
    if can_move(map,current_position.get_next_possiotn_y()):
        posible_position.append("Right")
    if can_move(map,current_position.get_previos_possiotn_y()):
        posible_position.append("Left")
    return posible_position

def move_player(game_map: list,player: Player, next_position: str):
    game_map[player.get_entity_position().get_position_x()][player.get_entity_position().get_position_y()] = 0
    if next_position == "Right":
        player.move_player(player.get_entity_position().get_next_possiotn_y())
    elif next_position == "Left":
        player.move_player(player.get_entity_position().get_previos_possiotn_y())
    elif next_position == "Stright":
        player.move_player(player.get_entity_position().get_next_possiotn_x())
    return game_map

def search_for_open_position(game_map) -> Position:
    for i in range(len(game_map[0])):
        for y in range(len(game_map[0])):
            if game_map[i][y] == 1:
                player_next_position = Position(i,y)
                return player_next_position
    return False

def turn_item(player: Player):
    
    first_item = Item()
    second_item = Item()
    third_item = Item()
    items = [first_item, second_item, third_item]
    print("You have found this 3 items you may take only 1:")
    print(f"1. {first_item.get_item_name()}")
    print(f"2. {second_item.get_item_name()}")
    print(f"3. {third_item.get_item_name()}")
    print("To display more info about the items input E/e to select the item input the item number")
    
    user_input = input()
    if user_input.isnumeric():
        player.add_item(items[int(user_input) - 1])
    elif user_input == "E" or user_input == "e":
        clear_screan()

        for item in items:
            item.display_info()
            print()
        user_input = input()
        player.add_item(items[int(user_input) - 1])

def turn_riddle():
    clear_screan()
    riddle = Riddle()
    try: 
        riddle.display_riddle()
        user_answer = inputimeout(prompt=">>", timeout=riddle.get_time_to_solve()) 
        if int(user_answer) == riddle.get_answer():
            print("Correct!")
            return True
        else:
            print("Incorrect! The correct answer.")
    except Exception: 
        user_answer = 'Your time is over!'
        print(user_answer) 

def turn(player: Player):
    turn_options = ["Items", "Riddle"]
    current_turn = random.choice(turn_options)
    match current_turn:
        case "Items":
            turn_item(player)
        case "Riddle":
            turn_riddle()

if __name__ == "__main__":
    player = Player()
    game_map = create_map()
    while search_for_open_position(game_map) and next_posible_pisitions(game_map,player.get_entity_position()) != []:
        print(next_posible_pisitions(game_map,player.get_entity_position()))
        next_position = input("go to: ")
        game_map = move_player(game_map,player,next_position)
        print_player_position(player,game_map)
        if next_posible_pisitions(game_map,player.get_entity_position()) == []:
            player.move_player(search_for_open_position(game_map))
        turn(player)
        print(player.get_all_items_names())





