import random
from Position import Position


def path_leangth(current_pisition, path_row, map, map_size,max_path_length):
    length = 1
    new_position = current_pisition.copy()
    if path_row:
        while check_bounds(map_size,new_position.get_previos_possiotn_y()) and map[new_position.get_position_x()][new_position.get_position_y() - 1] == 1:
            length += 1
            new_position.move_y(-1)
    else:
        while check_bounds(map_size,new_position.get_previos_possiotn_x()) and map[new_position.get_position_x() - 1][new_position.get_position_y()] == 1:
            length += 1
            new_position.move_x(-1)
    return length

def create_first_path(minimum_len_of_path, map, position_to_start_the_path_from, path_row,map_size,max_path_length):
    new_position = position_to_start_the_path_from.copy()
    for x in range(minimum_len_of_path ):
        if path_row:
            map[new_position.get_position_x()][new_position.get_position_y()] = 1
            if check_bounds(map_size ,new_position.get_next_possiotn_y()):
                new_position.move_y(1)
            else:
                break
        else:
            map[new_position.get_position_x()][new_position.get_position_y()] = 1
            if check_bounds(map_size ,new_position.get_next_possiotn_x()):
                new_position.move_x(1)
            else:
                break
    if path_row:
        return map,Position(new_position.get_position_x(),new_position.get_position_y() - 1)
    else:
        return map,Position(new_position.get_position_x() - 1,new_position.get_position_y())

def create_path(minimum_len_of_path, map, position_to_start_the_path_from, path_row,map_size,max_path_length):
    chance_to_continue_path = 0.5  #  probability for True
    chance_to_stop_path = 1 - chance_to_continue_path  #  probability for False
    current_position = position_to_start_the_path_from.copy()
    continue_path = random.choices([True, False], weights=[chance_to_continue_path, chance_to_stop_path])[0]
    right_down = random.choices([True,False])
    map,current_position = create_first_path(minimum_len_of_path,map, position_to_start_the_path_from,path_row,map_size,max_path_length)
    current_path_length = path_leangth(current_position,path_row,map,map_size,max_path_length)
    if path_row:
        new_position = current_position.copy()
        if right_down:
            while check_bounds(map_size ,new_position.get_next_possiotn_y()) and continue_path and current_path_length < max_path_length:
                map[new_position.get_position_x()][new_position.get_position_y() + 1] = 1
                new_position.move_y(1)
                continue_path = random.choices([True, False], weights=[chance_to_continue_path, chance_to_stop_path])[0]
                current_path_length += 1
        else:
            while check_bounds(map_size ,new_position.get_next_possiotn_y(-1)) and continue_path and current_path_length < max_path_length:
                map[new_position.get_position_x()][new_position.get_position_y() - 1] = 1
                new_position.move_y(-1)
                continue_path = random.choices([True, False], weights=[chance_to_continue_path, chance_to_stop_path])[0]
                current_path_length += 1
    else:
        new_position = current_position.copy()
        if  right_down:
            while check_bounds(map_size ,new_position.get_next_possiotn_x()) and continue_path and current_path_length < max_path_length:
                map[new_position.get_position_x() + 1][new_position.get_position_y()] = 1 
                new_position.move_x(1)
                continue_path = random.choices([True, False], weights=[chance_to_continue_path, chance_to_stop_path])[0]
                current_path_length += 1
        else:
            while check_bounds(map_size ,new_position.get_next_possiotn_x(-1)) and continue_path and current_path_length < max_path_length:
                map[new_position.get_position_x() - 1][new_position.get_position_y()] = 1 
                new_position.move_x(-1)
                continue_path = random.choices([True, False], weights=[chance_to_continue_path, chance_to_stop_path])[0]
                current_path_length += 1
        
    current_position = new_position.copy()
    return map,current_position

def init_the_map(map_size): # create a new map with the size that you set up
    map = [[0 for j in range(map_size)] for i in range(map_size)]
    return map

def check_bounds(map_size: int ,next_current_position: Position): # check if you can move to the next position in case that you can return true
    if next_current_position.get_position_x() >= map_size or next_current_position.get_position_y() >= map_size or next_current_position.get_position_y() < 0 or next_current_position.get_position_x() < 0 :
        return False
    return True

def print_map(map):
    for row in map:
        print(row)

def random_path(map,current_position,path_row,map_size,max_path_length):
    current_path_leangth = path_leangth(current_position,path_row,map,map_size,max_path_length)
    next_position_start_point = current_position.copy() # need to give a defule value

    if check_bounds(map_size,current_position.get_next_possiotn_y(2)) and check_bounds(map_size,current_position.get_next_possiotn_y(-2)) and path_row:
        next_position_start_point = random.randint(current_position.get_position_y()  - current_path_leangth + 1 ,current_position.get_position_y() -2)
        next_position_start_point = Position(current_position.get_position_x(), next_position_start_point)

    elif check_bounds(map_size,current_position.get_next_possiotn_x(2)) and check_bounds(map_size,current_position.get_next_possiotn_x(-2)) and not path_row: 
        next_position_start_point = random.randint(current_position.get_position_x()  - current_path_leangth + 1 ,current_position.get_position_x() -2)
        next_position_start_point = Position(next_position_start_point, current_position.get_position_y())

    # map = create_path(minimum_len_of_path,map,next_position_start_point,not path_row)[0]
    return next_position_start_point

def create_map():
    min_path_length = 3
    position = Position(0,0)
    path_row = True
    map_size = int(input("Enter the number of map_size: "))
    max_path_length = map_size/2
    map = init_the_map(map_size)
    random_path_row = path_row
    for x in range(int(map_size)):
        map,position = create_path(min_path_length,map, position,path_row,map_size,max_path_length)
        for y in range(int(map_size/2)):
            random_path_row = not random_path_row
            new_rout_position = random_path(map,position,path_row,map_size,max_path_length)
            map,new_rout_position = create_path(3,map, new_rout_position,random_path_row,map_size,max_path_length)
        # map = random_path(3,map,position,path_row,map_size)
        path_row = not path_row
    return map

