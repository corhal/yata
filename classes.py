class GameObject(object):
    def __init__(self, name):
        self.name = name

class Clue(object):
    def __init__(self, game_object, ident, is_main, priority, full_text):
        self.game_object = game_object
        self.ident = ident
        self.is_main = is_main
        self.priority = priority
        self.full_text = full_text

class Obj(GameObject):
    def __init__(self, name):
        GameObject.__init__(self, name)

class Item(GameObject):
    def __init__(self, name):
        GameObject.__init__(self, name)

class Creature(GameObject):
    def __init__(self, name):
        GameObject.__init__(self, name)
        self.hp = hp
        self.atk = atk

class Npc(Creature):
    def __init__(self, name, hp, atk, dialogues):
        Creature.__init__(self, name, hp, atk)
        self.dialogues = dialogues

class Location(GameObject):
    def __init__(self, name, game_objects=[]):
        GameObject.__init__(self, name)
        self.game_objects = game_objects

class Player(object):
    def __init__(self, current_location):
        self.clues_by_names = {}
        self.inventory = {}
        self.current_location = current_location

    def take(item, amount):
        self.inventory[item] = self.inventory.get(item, 0) + amount

    def give(item, amount):
        if inventory.get(item, 0) >= amount:
            self.inventory[item] -= amount
        else:
            print("I don't have enough " + item.name)

    def take_clue(self, clue):
        if clue.ident in self.clues_by_names.keys() and clue.priority < self.clues_by_names[clue.ident].priority:
            return
        self.clues_by_names[clue.ident] = clue

    def examine(self, game_object):
        if game_object.name not in self.clues_by_names:
            raise ValueError("Don't know anything about " + game_object.name)
        main_info = self.clues_by_names[game_object.name].full_text
        if game_object.name + " add" in self.clues_by_names:
            print(" " + self.clues_by_names[game_object.name + " add"].full_text)

dark_cave = Location("Dark Cave")
dark_cave_clues = [Clue(dark_cave, dark_cave.name, True, 0, "Вокруг полная темнота."),
                   Clue(dark_cave, dark_cave.name, True, 1, "Ты в темной пещере."),
                   Clue(dark_cave, dark_cave.name + " add", True, 2, "Ты в пещере Альгамбры."),
                   Clue(dark_cave, dark_cave.name + " add", False, 0, "Каждые три месяца здесь проходят собрания Ковена."),
                   Clue(dark_cave, dark_cave.name + " add", False, 1, "Говорят, где-то здесь спрятан клад.")]

player = Player(dark_cave)

for clue in dark_cave_clues:
    player.take_clue(clue)
    player.examine(dark_cave)
