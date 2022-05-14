from enum import Enum

class Phase(Enum):
    GROWTH_UPGRADE = 1
    GROWTH_PLAY = 2
    FAST_POWER = 3
    SLOW_POWER = 4

class Terrain(Enum):
    NONE = 0
    SANDS = 1
    JUNGLE = 2
    MOUNTAIN = 3
    WETLAND = 4
    COASTAL = 5
    JUNGLE_SANDS = 6
    JUNGLE_MOUNTAIN = 7
    JUNGLE_WETLAND = 8
    MOUNTAIN_SANDS = 9
    MOUNTAIN_WETLAND = 10
    SANDS_WETLAND = 11
    JUNGLE_ESC = 12
    MOUNTAIN_ESC = 13
    SANDS_ESC = 14
    WETLAND_ESC = 15
    

class Token(Enum):
    # Invaders/Dahan
    EXPLORER = 1
    TOWN = 2
    CITY = 3
    DAHAN = 4
    PRESENCE = 5
    BLIGHT = 6
    # TODO(add other tokens)
    WILDS = 7
    PLAGUE = 8
    FIST = 9
    BADLANDS = 10
    
class Elements(Enum):
    FIRE = 1
    EARTH = 2
    AIR = 3
    WATER = 4
    SUN = 5
    MOON = 6
    ANIMAL = 7
    PLANT = 8