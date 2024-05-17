from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction
from models.base import Base
import math

TEAM_ID : int = 7

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
    for base_id, distance in distances_to_bases:
        if distance < current_min:
            base_id_of_current_min = base_id
            current_min = distance

    return base_id_of_current_min

def decide(gameState: GameState) -> List[PlayerAction]:
    playeractions_list = []
    for base in gameState.bases:
        if base.player != 7:
            continue
        distances_to_bases = calc_distances_to_bases(gameState, base)
        nearest_enemy_base_id = get_nearest_enemy_base(gameState, distances_to_bases, base)

        playeractions_list.append(PlayerAction(base.uid, nearest_enemy_base_id, int(base.population/2)))

    

    return playeractions_list
