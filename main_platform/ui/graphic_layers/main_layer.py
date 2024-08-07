from .layer import *

from .graphics.text_input import *
from .graphics.button import *
from .graphics.title import *
from .graphics.icon_button import *

from .controllers.graphical_text_input import *
from .controllers.graphical_button import *

import resources as _resources
import events as _events

class MainGraphicLayer(GraphicLayer):
    def __init__(self, resources: _resources.Resources):
        super().__init__(resources)

        self._game_title = GameTitleDisplayedElement(resources)

        self._play_local = ButtonDisplayedElement(resources, "UI_MAIN_MENU_PLAY_LOCAL")
        self._play_local_controller = GraphicalButtonController(self._play_local)

        self._play_local.get_events()["mouse_press"].addEventFunction(self.on_local_press)
        self._play_local.get_events()["mouse_release"].addEventFunction(self.on_local_release)

        self._play_online = ButtonDisplayedElement(resources, "UI_MAIN_MENU_PLAY_ONLINE")
        self._play_online_controller = GraphicalButtonController(self._play_online)

        self._play_online.get_events()["mouse_press"].addEventFunction(self.on_online_press)
        self._play_online.get_events()["mouse_release"].addEventFunction(self.on_online_release)

        self._back_button = IconButtonDisplayedElement(resources, "back")
        self._back_button.get_events()['mouse_release'].addEventFunction(self.on_back_release)

        self._back_button_controller = GraphicalButtonController(self._back_button)

        self.get_events().create_events(
            "back",
            "play_local_press",
            "play_local_release",
            "play_online_press",
            "play_online_release"
        )
    
    def on_local_press(self, event: _events.Event) -> None:
        self._events["play_local_press"].emit()

    def on_local_release(self, event: _events.Event) -> None:
        self._events["play_local_release"].emit()

    def on_online_press(self, event: _events.Event) -> None:
        self._events["play_online_press"].emit()

    def on_online_release(self, event: _events.Event) -> None:
        self._events["play_online_release"].emit()

    def on_back_release(self, event: _events.Event) -> None:
        self.get_events()['back'].emit(event)
    
    def set_rect(self, x: int, y: int, w: int, h: int) -> None:
        
        self._game_title.set_size( h/4 )
        self._game_title.set_position(x + w/2, y + h/5)

        self._play_local.set_size(h/10)
        self._play_local.set_position(x + w/3, y + h * 2/3)

        self._play_online.set_size(h/10)
        self._play_online.set_position(x + w * 2/3, y + h * 2/3)
    
        self._back_button.set_position(x + 20 + 25, y + 20 + 25)
        self._back_button.set_size(50)

    def get_items(self) -> list[ GameDisplayedElement ]:
        return [self._game_title, self._play_online, self._play_local, self._back_button]
    
