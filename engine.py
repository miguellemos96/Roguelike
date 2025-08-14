from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from entity import Entity
from game_map import GameMap
from input_handlers import handle_event

class Engine:
    def __init__(self, entities: Set[Entity], player: Entity, game_map: GameMap):
        self.entities = entities
        self.player = player
        self.game_map = game_map

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = handle_event(event)
            if action is None:
                continue

            action.perform(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()