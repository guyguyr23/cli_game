import time
from entity_modules.Player import Player
from entity_modules.Animals import Animal
def turn_enemy(player: Player):
    animal = Animal()
    print("You have found")
    animal.display_info()
    print("Do you want to:")
    print("1. Fight")
    print("2. Run")
    player_choice = int(input())
    match player_choice:
        case 1:
            return fight(animal,player)
        case 2:
            pass

def tame(enemy: Animal, player: Player) -> bool:
    if enemy.get_max_health() * 0.3 >= enemy.get_health():
        enemy.set_health(enemy.get_max_health())
        player.tame(enemy)
        print(" You have tamed ")
        return True
    else:
        print("couldent tame the enemy")
        return False

def fight(enemy ,player: Player):
        while not player.check_death() and not enemy.check_death():
            player.display_attacks()
            print("4. tame")
            player_attack = int(input())
            if player_attack == 4:
                if tame(enemy,player):
                    break

            elif player_attack == 3: # number to use an item
                attack_counter = 1
                for item in player.get_all_items():
                    item_name = item.get_useable_name()
                    print(f"{attack_counter}. {item_name}")
                    attack_counter += 1

                player_item = int(input())
                item_attacks = player.get_an_item(player_item - 1).get_attacks()
                item_name = player.get_an_item(player_item - 1).get_useable_name()
                attack_counter = 1
                for item_attack in item_attacks:
                    print(f"{attack_counter}. {item_name} --> {item_attack.get_attack_name()}, Damage: {item_attack.get_attack_damage() * player.get_damage()}")
                    attack_counter += 1
                player_item_attack = int(input())
                enemy.take_damage(player.get_an_item(player_item - 1).get_an_attack(player_item_attack - 1).get_attack_damage() * player.get_damage()) 
                player.get_an_item(player_item - 1).item_take_damage(player_item_attack - 1)
                if player.get_an_item(player_item - 1).get_durability() > 0:
                    print(f"You item has been taken a damage and its durability is now: {player.get_an_item(player_item - 1).get_durability()}")
                else:
                    print("You item has been broken and you lost it")
                    player.remove_item(player_item - 1)
            else:
                enemy.take_damage(player.get_attack_damage(player_attack))
            for tamed_entiry in player.get_tames():
                tame_attack = tamed_entiry.get_an_attack()
                print(f"Your: {tamed_entiry.get_name()} has attacked using: {tame_attack.get_attack_name()} and will be doing: {tame_attack.get_attack_damage()}")
                enemy.take_damage(tame_attack.get_attack_damage())
            print("The enemy health is: " + str(enemy.get_health()))
            enemy_attack = enemy.get_an_attack()
            print(f"The {enemy.get_name()} is attacking you using: {enemy_attack.get_attack_name()}, you will lose {enemy_attack.get_attack_damage()} HP")
            player.take_damage(enemy_attack.get_attack_damage())
            print("The player health is: " + str(player.get_health()))
        if enemy.check_death():
            print(f"You have killed the {enemy.get_name()}")
            player.add_xp(enemy.get_xp())
            if player.check_for_level_up():
                player.leavel_up()
            else:
                print(f"You got {enemy.get_xp()} XP")
        time.sleep(2)
