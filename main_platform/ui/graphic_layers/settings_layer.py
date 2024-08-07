from .layer import *

from .graphics.icon_button import *
from .graphics.label import *
from .controllers.graphical_button import *

import resources as _resources
import events as _events

class SettingsLayer(GraphicLayer):
    def __init__(self, resources: _resources.Resources):
        super().__init__(resources)

        self._settings_label = LabelDisplayedElement(resources, "SETTINGS_TITLE", 100)

        self._back_button = IconButtonDisplayedElement(resources, "back")
        self._back_button.get_events()['mouse_release'].addEventFunction(self.on_back_release)

        self._back_button_controller = GraphicalButtonController(self._back_button)

        self._graphical_settings_button = IconButtonDisplayedElement(resources, "display")
        self._graphical_settings_button_controller = GraphicalButtonController(self._graphical_settings_button)
        self._graphical_settings_button.set_title("SETTINGS_GRAPHICAL")
        self._graphical_settings_button.get_events()['mouse_release'].addEventFunction(self.on_graphical_settings_release)

        self._language_settings_button = IconButtonDisplayedElement(resources, "language")
        self._language_settings_button_controller = GraphicalButtonController(self._language_settings_button)
        self._language_settings_button.set_title("SETTINGS_LANGUAGE")
        self._language_settings_button.get_events()['mouse_release'].addEventFunction(self.on_language_settings_release)

        self.get_events().create_events(
            'back',
            'open_graphical_settings',
            'open_language_settings'
        )
    
    def on_back_release(self, event: _events.Event) -> None:
        self.get_events()['back'].emit(event)
    
    def on_graphical_settings_release(self, event: _events.Event) -> None:
        self.get_events()['open_graphical_settings'].emit(event)
    
    def on_language_settings_release(self, event: _events.Event) -> None:
        self.get_events()['open_language_settings'].emit(event)
    
    def get_items(self) -> list[GameDisplayedElement]:
        return [self._back_button, self._settings_label, self._graphical_settings_button, self._language_settings_button]
    
    def background_variant(self) -> str:
        return "settings"
    
    def set_rect(self, x: int, y: int, w: int, h: int) -> None:
        self._back_button.set_position(x + 20 + 25, y + 20 + 25)
        self._back_button.set_size( 50 )

        self._settings_label.set_position(x + w/2, y + h/7)
        self._settings_label.set_size( w/14 )

        self._graphical_settings_button.set_position(x+w/2 - h/8, y+h/2 - h/8)
        self._graphical_settings_button.set_size(h/5)

        self._language_settings_button.set_position(x+w/2 + h/8, y+h/2 - h/8)
        self._language_settings_button.set_size(h/5)
