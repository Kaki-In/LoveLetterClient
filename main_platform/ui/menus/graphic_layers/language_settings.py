from .layer import *

from .graphics.icon_button import *
from .graphics.label import *
from .graphics.dlist import *

from .controllers.graphical_button import *
from .controllers.graphical_list import *

import resources as _resources
import events as _events

class LanguageSettingsLayer(GraphicLayer):
    def __init__(self, resources: _resources.Resources):
        super().__init__(resources)

        self._settings_label = LabelDisplayedElement(resources, "SETTINGS_LANGUAGE_TITLE", 100)

        self._back_button = IconButtonDisplayedElement(resources, "back")
        self._back_button.get_events()['mouse_release'].addEventFunction(self.on_back_release)

        self._back_button_controller = GraphicalButtonController(self._back_button)

        self._list = ListDisplayedElement(resources, [], 20)
        self._list_controller = GraphicalListController(self._list)

        self._list_controller.get_events()['item_selected'].addEventFunction(self.on_item_selected)

        self.get_events().create_events(
            'back',
            'language_change'
        )
    
    def set_position(self, position: int ) -> None:
        self._list.set_selected_position(position)
    
    def set_languages_list(self, list: list[str]) -> None:
        self._list.set_elements(list)
    
    def on_item_selected(self, event: _events.Event) -> None:
        item = event.values()[0]
        self._events['language_change'].emit(item)

    def on_back_release(self, event: _events.Event) -> None:
        self.get_events()['back'].emit(event)
    
    def get_items(self) -> list[GameDisplayedElement]:
        return [self._back_button, self._settings_label, self._list]
    
    def background_variant(self) -> str:
        return "settings"
    
    def set_rect(self, x: int, y: int, w: int, h: int) -> None:
        self._back_button.set_position(x + 20 + 25, y + 20 + 25)
        self._back_button.set_size( 50 )

        self._settings_label.set_position(x + w/2, y + h/7)
        self._settings_label.set_size( w/14 )

        self._list.set_font_size( w/50 )
        self._list.set_position(x + w/2, y + h * 5/8)
        self._list.set_width(w * 9/20)
        self._list.set_height(h /2)
