from enum import Enum

class GameObject:

    simpleName = ""
    adjectives = []
    location = ""
    
    def __init__(self, newSimpleName, newAdjectives, newLocation):
        self.simpleName = newSimpleName
        self.adjectives = newAdjectives
        self.location = newLocation

class Active(GameObject):

    def move(self, toDirection, toSimpleName = ""):
        for potentialConnection in self.location.connectionList:
            listOfConnections = []
            if potentialConnection.direction == toDirection:
                listOfConnections.append(potentialConnection)
        if len(listOfConnections) > 1:
            if toSimpleName != "":
                return moveToRoom(listOfConnections, toSimpleName)
            else:
                return "You will have to be more specific as to where you want to go"
        else if len(listOfConnections) == 1:
            self.location = listOfConnections[0]
            return "You have moved to a new location"
        else:
            return "You can't go that way."
                
        print(self.simpleName + " went " + direction.name + " to " )

    def moveToRoom(self, listOfConnections, toSimpleName):
        

class Inactive(GameObject):

    def use(self):
        print(self.simpleName + " was used")

class Location:

    connectionList = []
    
    def __init__(self):
        print("X")

class Room(Location):

    simpleName = ""
    prefix = ""
    descriptions = {}

    def __init__(self, newSimpleName, newDescriptions, newPrefix):
        self.simpleName = newSimpleName
        self.descriptions = newDescriptions
        self.prefix = newPrefix

    def addConnection(self, direction, room):
        self.connectionList.append(Connection(direction, room))

class Connection:
    direction = ""
    location = ""

    def __init__(self, toDirection, toRoom):
        self.direction = toDirection
        self.location = toRoom

class Direction(Enum):
    north = "north"
    south = "south"
    west = "west"
    east = "east"
    up = "up"
    down = "down"
    inside = "in"
    outside = "out"

class Perspectives(Enum):
    human = "human"
    dog = "dog"
    bird = "bird"

class GameMap():
    listOfLocations = []
    listOfObjectsForReference = []

    def __init__(self):
        self.listOfLocations = []
        self.listOfObjectsForReference = []

    def findToRoom(self, toSimpleName, activeLocation):
        for 
