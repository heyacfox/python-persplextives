class GameObject:

    simpleName = ""
    adjectives = []
    
    def __init__(self, newSimpleName, newAdjectives):
        self.simpleName = newSimpleName
        self.adjectives = newAdjectives

class Active(GameObject):

    def walk(self):
        print(self.simpleName + " walked")


class Inactive(GameObject):

    def use(self):
        print(self.simpleName + " was used")
