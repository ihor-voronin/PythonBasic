from abc import ABC
from typing import Optional

from .spells.base import Spell


class BaseUnit(ABC):
    _name: str

    defense: float
    attack_damage: float
    magic_defense: float
    _spell: Optional[Spell]
    _spell_charges: int

    _hp: float

    unit_type: str

    def __init__(self, name: str, spell: Optional[Spell] = None, spell_charges: int = 0) -> None:
        self._hp = 100
        self._name = name
        self._spell = spell
        self._spell_charges = spell_charges

    def display_name(self):
        return f"[{self._name}] hp:{self._hp}"

    def attack(self, target: 'BaseUnit') -> None:
        applied_damage: float = target.damage(attack_damage=self.attack_damage)
        print(f"{self.unit_type} {self.display_name()} deal {applied_damage} damage to {target.display_name()}")

    def damage(self, attack_damage:float=0, magical_damage:float=0) -> float:
        applied_damage: float = max(attack_damage - self.defense, 0) \
                                + max(magical_damage - self.magic_defense, 0)
        self._hp -= applied_damage
        if self.is_dead():
            print(f"{self.display_name()} is dead!!!")
        return applied_damage

    def cast_spell(self, target: 'BaseUnit') -> None:
        print(f"{self.unit_type} {self.display_name()} cast {self._spell.display_name()} to {target.display_name()}")
        self._spell.cast(target)

    def can_cast_spell(self) -> bool:
        if not self._spell:
            return False
        return (self._spell_charges or 0) > 0

    def is_dead(self) -> bool:
        return self._hp <= 0
