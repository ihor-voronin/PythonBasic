class Spell:
    name: str

    def display_name(self):
        return f"[{self.name}]"

    def cast(self, target) -> None:
        raise NotImplementedError
