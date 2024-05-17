from models.base import Base
from typing import List
from models.board_action import BoardAction
from models.game import Game
from models.game_config import GameConfig


class GameState:
    actions: List[BoardAction] = []
    bases: List[Base] = []
    config: GameConfig
    game: Game

    @classmethod
    def fromAttributes(cls, actions: list[BoardAction], bases: list[Base], config: GameConfig, game: Game):
        gameState = {
            'actions': actions,
            'bases': bases,
            'config': config,
            'game': game
        }
        return cls(gameState)


    def __init__(self, gameState: dict) -> None:
        self.actions: List[BoardAction] = []
        self.bases: List[Base] = []
        
        for action in gameState['actions']:
            self.actions.append(BoardAction(action))

        for base in gameState['bases']:
            self.bases.append(Base(base))

        self.config = GameConfig(gameState['config'])
        self.game = Game(gameState['game'])
