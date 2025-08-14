#!/usr/bin/env python
import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities, player, game_map)

    with (tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="Rouge",
        vsync=True,
    ) as context):
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(root_console, context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()