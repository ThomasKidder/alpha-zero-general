from enum import Enum
import random

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

def is_coastal(self, land):
    return land.num <= 3


class Land():
    # Tokens: 
    def __init__(self, terrain, num, adj):
        self.tokens = {}
        self.terrain = Terrain
        self.num = num
        self.adj = adj
    
    def changeTokens(self, Token, amount):
        self.tokens[Token] = self.tokens.get(Token, 0) + amount

    def get_tokens(self, Token):
        return self.tokens.get(Token, 0)

    def addToken(self, Token):
        self.changeTokens(Token, 1)
    
    # Returns true if a token was removed successfully
    def remove_token(self, Token):
        if (self.tokens[Token] > 0):
            self.changeTokens(Token, -1)   
            return True
        else:
            return False     

class Board():
    # TODO: Allow for other board initializations
    def __init__(self):
        # TODO: Write a unit test for adjacency, maybe other things
        #         self.adj = [
        #     [2, 4, 5, 6],
        #     [1, 3, 4],
        #     [2, 4],
        #     [1, 2, 3, 5],
        #     [1, 4, 6, 7, 8],
        #     [1, 5, 8],
        #     [5, 8],
        #     [5, 6, 7],
        # ]
        self.lands = [
            Land(Terrain.MOUNTAIN, 1, [2, 4, 5, 6]),
            Land(Terrain.WETLAND, 2, [1, 3, 4]),
            Land(Terrain.JUNGLE, 3, [2, 4]),
            Land(Terrain.SANDS, 4, [1, 2, 3, 5]),
            Land(Terrain.WETLAND,5, [1, 4, 6, 7, 8]),
            Land(Terrain.MOUNTAIN, 6, [1, 5, 8]),
            Land(Terrain.SANDS, 7, [5, 8]),
            Land(Terrain.JUNGLE, 8, [5, 6, 7]),
        ]
        # Add board A starting tokens
        self.land(2).addToken(Token.CITY)
        self.land(2).addToken(Token.DAHAN)
        self.land(3).changeTokens(Token.DAHAN, 2)
        self.land(4).addToken(Token.BLIGHT)
        self.land(6).addToken(Token.DAHAN)
        self.land(7).changeTokens(Token.DAHAN, 2)
        self.land(8).addToken(Token.TOWN)
                
    # Index of land on map
    def get_land(self, num):
        return self.lands[num-1]
    
    def land_match(self, terrain):
        if terrain == Terrain.COASTAL:
            return [self.land(1), self.land(2), self.land(3)]
        terrains = [terrain]
        match terrain:
            case Terrain.JUNGLE_SANDS:
                terrains = [Terrain.SANDS, Terrain.JUNGLE]
            case Terrain.MOUNTAIN_SANDS:
                terrains = [Terrain.SANDS, Terrain.MOUNTAIN]
            case Terrain.SANDS_WETLAND:
                terrains = [Terrain.SANDS, Terrain.WETLAND]
            case Terrain.JUNGLE_MOUNTAIN:
                terrains = [Terrain.JUNGLE, Terrain.MOUNTAIN]
            case Terrain.JUNGLE_WETLAND:
                terrains = [Terrain.JUNGLE, Terrain.WETLAND]
            case Terrain.MOUNTAIN_WETLAND:
                terrains = [Terrain.MOUNTAIN, Terrain.WETLAND]
            case Terrain.SANDS_ESC:
                terrains = [Terrain.SANDS]
            case Terrain.JUNGLE_ESC:
                terrains = [Terrain.JUNGLE]
            case Terrain.MOUNTAIN_ESC:
                terrains = [Terrain.MOUNTAIN]
            case Terrain.WETLAND_ESC:
                terrains = [Terrain.WETLAND]
        matches = []
        for land in self.lands:
            if land.terrain in terrains:
                matches.append(land)
        return matches

    # Takes list of land objects and returns list of 
    # land objects within that range.
    def lands_from_dist(self, lands, dist):
        # Contains land numbers
        current = {}
        for land in lands:
            current.add(land.num)
        
        for i in range(dist):
            added = {}
            for land in current:
                for adj in land.adj:
                    added.add(adj)
            current.update(added)
        result = []
        # Convert land numbers back to lands
        for num in current:
            result.append(self.get_land(id))
        return result

class Power():
    def __init__(self):
        pass

    def type():
        pass
    
class InnatePower(Power):
    def __init__(self):
        pass

class Spirit():
    def __init__(self):
        pass
        

class VitalStrength(Spirit):
    def __init__(self):
        self.energy_track = [2, 3, 4, 6, 7, 8]
        self.plays_track = [1, 2, 2, 3, 4]
        self.energy_idx = 0
        self.play_idx = 0
        # TODO: Ignoring destroyed for the purpose of
        # placing presence for now. 
        self.destroyed_presence = 0

def makeStage(cards):
    random.shuffle(cards)
    cards.pop()
    return cards

class InvaderDeck():
    def __init__(self):
        phase1 = [Terrain.SANDS, Terrain.JUNGLE, Terrain. MOUNTAIN,
                  Terrain.WETLAND]
        phase2 = [Terrain.SANDS_ESC, Terrain.JUNGLE_ESC, Terrain.MOUNTAIN_ESC,
                  Terrain.WETLAND_ESC, Terrain.COASTAL]
        phase3 = [Terrain.JUNGLE_SANDS, Terrain.MOUNTAIN_SANDS, Terrain.SANDS_WETLAND,
                  Terrain.JUNGLE_MOUNTAIN, Terrain.JUNGLE_WETLAND, Terrain.MOUNTAIN_WETLAND]
        self.deck = makeStage(phase1) + makeStage(phase2) + makeStage(phase3)
        self.build = Terrain.NONE
        self.ravage = Terrain.NONE

    # Returns none if nothing left to explore, meaning game over.
    # def explore():
    #     if not deck:
    #         return Terrain.NONE
    #     explored = deck.pop(0)
    #     self.ravage = self.build
    #     self.build = explored
    #     return explored
    
    # def build():
    #     return self.build
    
    # def ravage():
    #     return self.ravage
        
        




        

class SpiritIslandState():
    """
    Game state structure:
    
    
    List<Board>
        List<Land>
            Tokens
            -presence, invaders, dahan, etc
    List<Spirits>
        Presence(destroyed)
        Amount of energy
        Energy Track
        Cards Played Track
        List<Cards> hand
        List<Cards> discard
    Fear Cards - Skip for now
    Invader Deck - 
        
            
        
    """
    def __init__(self):
        # Setup
        self.invader_deck = InvaderDeck()
        self.board = Board()
        self.spirit = VitalStrength()
        # Do initial explore
        
    # Returns true if game is over
    def do_explore(self):
        terrain = self.board.explore()
        if terrain == Terrain.NONE:
            return True
        matches = self.board.land_match(terrain)
        for match in matches:
            needs_explore = False
            if is_coastal(match):
                needs_explore = True
            else:
                adj_lands = self.board.lands_from_dist([match], 1)
                for land in adj_lands:
                    if land.get_tokens(Token.TOWN) > 0 or land.get_tokens(Token.CITY) > 0:
                        needs_explore = True
                        break
            if needs_explore:
                if not match.remove_token(Token.WILDS):
                    match.add_token(Token.EXPLORER)         
        return False

    # def do_build(self):
        
        