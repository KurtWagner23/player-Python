from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction
from models.base import Base
from models.game_state import GameState
import math

TEAM_ID : int = 7

def is_our_base_id(gameState : GameState, id : int) -> bool:
    for base in gameState.bases:
        if base.uid == id:
            return base.player == TEAM_ID
        
def get_base_from_id(gameState : GameState, id) -> Base:
    for base in gameState.bases:
        if base.uid == id:
            return base

def calc_distance(base1 : Base, base2 : Base) -> int:
    return int(math.sqrt((base1.position.x - base2.position.x)**2 + (base1.position.y - base2.position.y)**2 + (base1.position.z - base2.position.z)**2))

def calc_distances_to_bases(gameState : GameState, selected_base : Base) -> dict[int, int]:
    results = {}
    for base in gameState.bases:
        results[base.uid] = calc_distance(base, selected_base)
    return results

def get_nearest_enemy_base(gameState : GameState, distances_to_bases : dict[int,int], selected_base : Base) -> int:
    base_id_of_current_min = 0
    current_min = 100000
    for base_id, distance in distances_to_bases.values():
        if distance < current_min:
            base_id_of_current_min = base_id
            current_min = distance
    return base_id_of_current_min

def check_for_enemy_attack(gameState:GameState) -> dict[int, tuple[int,int]]:
    attack_on_base_dict : dict[int, tuple[int,int]] = {}
    for action in gameState.actions:
        if not is_our_base_id(action.dest):
            continue
        base : Base = get_base_from_id(action.dest)
        time_until_attack = action.progress.distance - action.progress.traveled
        attack_on_base_dict[base.uid] = (action.amount, time_until_attack)
    return attack_on_base_dict

def help_bits_needed(gamestate: GameState, attack_on_bases_dict:dict, baseuid: int) -> int:
    base :Base = get_base_from_id(baseuid)
    amount = -base.population
    for attacked_base_id, values in attack_on_bases_dict.values():
        if attacked_base_id == baseuid:
            amount += values[0]
    return amount

def get_list_of_bases_how_need_help(gameState : GameState) -> list[int]:
    for base in gameState.bases:
        if base.player != 7:
            continue
        

def decide(gameState: GameState) -> List[PlayerAction]:
    playeractions_list = []
    for base in gameState.bases:
        if base.player != 7:
            continue
        distances_to_bases = calc_distances_to_bases(gameState, base)
        nearest_enemy_base_id = get_nearest_enemy_base(gameState, distances_to_bases, base)

<<<<<<< Updated upstream
<<<<<<< Updated upstream
        playeractions_list.append(PlayerAction(base.uid, nearest_enemy_base_id, int(base.population/2)))

    
=======
        playeractions_list.append(PlayerAction(base.uid, nearest_enemy_base_id, int(base.population/6)))
>>>>>>> Stashed changes
=======
        playeractions_list.append(PlayerAction(base.uid, nearest_enemy_base_id, int(base.population/6)))
>>>>>>> Stashed changes

    return playeractions_list
