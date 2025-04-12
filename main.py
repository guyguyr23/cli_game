import time
import os
from entity_modules.Player import Player
from map.map import *
from Riddles import Riddle
from inputimeout import inputimeout 
from turn.item import *
from map.player_map import *
from turn.enemy import turn_enemy
def clear_screan():
    os.system('cls' if os.name == 'nt' else 'clear')

def turn_riddle():
    clear_screan()
    riddle = Riddle()
    try: 
        riddle.display_riddle()
        user_answer = inputimeout(prompt=">> ", timeout=riddle.get_time_to_solve()) 
        if int(user_answer) == riddle.get_answer():
            print("Correct!")
            time.sleep(2)
            return True
        else:
            print("Incorrect!")
            time.sleep(2)
    except Exception: 
        if riddle.get_answer() == 0:
            print("Correct!, sometime there is no right answer")
            time.sleep(2)
        else:
            user_answer = 'Your time is over!'
            print(user_answer) 
            time.sleep(2)

def turn(player: Player):
    turn_options = ["Items", "Enemy", "Riddle", "Skip"]
    current_turn = random.choices(turn_options, weights=[21, 17, 17, 40], k=1)[0]
    match current_turn:
        case "Items":
            turn_item(player)
        case "Riddle":
            turn_riddle()
        case "Enemy":
            turn_enemy(player)
        case "Skip":
            return 0

def open_manu():
    manu_player_select = input("""
          select on of the following option
          1. return to game
          2. show stats
          3. display inventory
          4. use item
          """)
    while manu_player_select not in ["1","2","3","4"]:
        manu_player_select = input("""
            select on of the following option
            1. return to game
            2. show stats
            3. display inventory
            4. use item
            """)
    match int(manu_player_select):
        case 1:
            print()
        case 2:
            player.display_stats()
        case 3:
            player.display_all_items()
        case 4:
            if len(player.get_all_items("Consumeble")) > 0:
                try:
                    player.display_all_items("Consumeble")
                    consume_item = int(input("choose item to use:")) -1
                    player.use_consumable(consume_item)
                    player.display_stats()
                except:
                    None
            else:
                print("You dont have items that you can use right now")
        case _:
            print("Not a supported option")

if __name__ == "__main__":
    player = Player()
    game_map = create_map()
    while not player.check_death() and search_for_open_position(game_map) and next_posible_pisitions(game_map,player.get_entity_position()) != []:
        # clear_screan()
        print(next_posible_pisitions(game_map,player.get_entity_position()))
        next_position = input("go to: ")
        if next_position == "manu":
            open_manu()
        else:
            game_map = move_player(game_map,player,next_position)
            if next_posible_pisitions(game_map,player.get_entity_position()) == []:
                player.move_player(search_for_open_position(game_map))
            turn(player)
            # print(player.get_all_items_names())
        # print_player_position(player,game_map)





