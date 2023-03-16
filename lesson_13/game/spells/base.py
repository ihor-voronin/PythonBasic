class Spell:
    name: str

    def display_name(self):
        return f"[{self.name}]"

    def cast(self, target: 'BaseUnit') -> None:
        raise NotImplementedError
