from .base import Player


class Ranger(Player):
    class_name = "Ranger"

    def __init__(self, name):
        super().__init__(name, spell=None, spell_charges=0)
        self.defense = 18
        self.attack_damage = 22
        self.magic_defense = 10
