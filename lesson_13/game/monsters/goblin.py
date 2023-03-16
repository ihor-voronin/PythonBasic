from lesson_13.game.monsters.base import Monster


class Goblin(Monster):

    def __init__(self):
        super().__init__(name="Goblin", spell=None, spell_charges=0)
        self.defense = 2
        self.attack_damage = 30
        self.magic_defense = 2
        self.hp = 50
