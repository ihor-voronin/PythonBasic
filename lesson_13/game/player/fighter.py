from .base import Player


class Fighter(Player):
    class_name = "Fighter"

    def __init__(self, name):
        super().__init__(name, spell=None, spell_charges=0)
        self.defense = 24
        self.attack_damage = 16
        self.magic_defense = 12
