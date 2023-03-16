from ..base_unit import BaseUnit


class Player(BaseUnit):
    class_name: str
    unit_type = "Player"

    def display_name(self) -> str:
        return f"[{self.class_name}] {self._name} hp:{self._hp}"
