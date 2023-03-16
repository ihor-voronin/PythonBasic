from typing import Optional

from ..base_unit import BaseUnit
from ..spells.base import Spell


class Monster(BaseUnit):
    unit_type = "Monster"

    def __init__(self, name="Monster", spell: Optional[Spell] = None, spell_charges: int = 0):
        super().__init__(name, spell, spell_charges)
        self.defense = 2
        self.attack_damage = 30
        self.magic_defense = 2
        self.hp = 50

