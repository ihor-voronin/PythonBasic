from typing import List

from lesson_13.game.monsters import Goblin, Monster
from lesson_13.game.player.base import Player
from lesson_13.game.player.fighter import Fighter
from lesson_13.game.player.ranger import Ranger

player: Player
monsters: List[Monster] = []


def generate_monsters(monster_list: List[Monster]):
    monster_classes = Monster.__subclasses__()
    for monster_class in monster_classes:
        monster_list.append(monster_class())


if __name__ == "__main__":
    player_name = input("Input player name: ")
    selected_class = 0
    while selected_class < 1 or selected_class > 2:
        print(
            """Select class:
        1 - Ranger
        2 - Fighter
        """
        )
        try:
            selected_class = int(input("select class: "))
        except ValueError as e:
            selected_class = 0
        if not selected_class:
            print("Incorrect class. Please select 1 or 2")

    if selected_class == 1:
        player = Ranger(name=player_name)
    elif selected_class == 2:
        player = Fighter(name=player_name)
    else:
        raise Exception("cannot find class for player")

    generate_monsters(monsters)

    not_dead_monsters = [monster for monster in monsters if not monster.is_dead()]
    while not player.is_dead() or all([not monster.is_dead() for monster in monsters]):
        print(f"Player turn!")
        select_action = 0
        while select_action < 1 or select_action > (
            2 - int(not player.can_cast_spell())
        ):
            print("Select action:")
            print("1 - attack damage")
            if player.can_cast_spell():
                print("2 - cast spell to first monster")

            try:
                select_action = int(input("select action: "))
            except ValueError:
                select_action = 0

            if not select_action:
                print("Incorrect action!!!")
        target = not_dead_monsters[0]

        if select_action == 1:
            player.attack(target)
        elif selected_class == 2 and player.can_cast_spell():
            player.cast_spell(target)
        else:
            raise Exception("cannot apply action!!!")

        not_dead_monsters = [monster for monster in monsters if not monster.is_dead()]
        for monster in monsters:
            if monster.can_cast_spell():
                monster.cast_spell(player)
                continue
            monster.attack(player)

        if player.is_dead():
            print("YOU DIED!")
            break
        elif len(not_dead_monsters) == 0:
            print("YOU WIN!!!")
            break
