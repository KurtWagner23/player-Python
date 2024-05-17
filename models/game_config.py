from models.base_level import BaseLevel
from typing import List

class PathsConfig:
    grace_period: int    # time until groups of bits take damage
    death_rate: int      # time until groups of bits take damage

    @classmethod
    def fromAttributes(cls, gracePeriod: int, deathRate: int):
        pathsconfig = {
            'grace_period': gracePeriod,
            'death_rate': deathRate
        }
        return cls(pathsconfig)

    def __init__(self, pathsconfig: dict):
        self.grace_period = pathsconfig['grace_period']
        self.death_rate = pathsconfig['death_rate']

class GameConfig:
    base_levels: list[BaseLevel] = []    # all available base levels
    paths: PathsConfig  # settings containing paths between bases

    @classmethod
    def fromAttributes(cls, base_levels: list[BaseLevel], paths: PathsConfig):
        gameconfig = {
            'base_levels': base_levels,
            'paths': paths
        }
        return cls(gameconfig)

    def __init__(self, gameconfig: dict) -> None:
        for base_level in gameconfig['base_levels']:
            self.base_levels.append(BaseLevel(base_level))
        self.paths = PathsConfig(gameconfig['paths'])
