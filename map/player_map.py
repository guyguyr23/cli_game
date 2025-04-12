from map.Position import Position
from map.map import *
from entity_modules.Player import Player

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
