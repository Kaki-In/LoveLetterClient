from .layer import *

from .graphics.text_input import *
from .graphics.button import *
from .graphics.title import *
from .graphics.icon_button import *

from .controllers.graphical_text_input import *
from .controllers.graphical_button import *

import events as _events

class FirstGraphicLayer(GraphicLayer):
    def __init__(self, resources):
        super().__init__(resources)
        
        self._text_input = TextInputDisplayedElement(resources, "")
        self._text_input.set_text_hint(resources.get_translator().translate("UI_FIRST_GRAPHIC_HINT_ENTER_NAME"))
        self._text_input.set_size(0)
        self._text_input.get_events()["text_changed"].addEventFunction(self.on_text_changed)
        
        self._text_controller = GraphicalTextInputController(self._text_input)
        
        self._button = ButtonDisplayedElement(resources, resources.get_translator().translate("UI_FIRST_GRAPHIC_BUTTON_PLAY"))
        self._button.get_events()["mouse_press"].addEventFunction(self.on_button_press)
        self._button.get_events()["mouse_release"].addEventFunction(self.on_button_release)
        self._button.set_size(0)
        self._button.disable()
        
        self._button_controller = GraphicalButtonController(self._button)
        
        self._game_title = GameTitleDisplayedElement(resources)

        self._settings_button = IconButtonDisplayedElement(resources, "settings")
        self._settings_button.get_events()['mouse_release'].addEventFunction(self.on_settings_button_release)

        self._settings_button_controller = GraphicalButtonController(self._settings_button)

        self._events.create_events(
            "button_press",
            "button_release",
            "text_changed",
            "open_settings_released"
        )
    
    def on_button_press(self, event: _events.Event) -> None:
        self._events["button_press"].emit()
    
    def on_button_release(self, event: _events.Event) -> None:
        self._events["button_release"].emit()
    
    def on_settings_button_release(self, event: _events.Event) -> None:
        self._events['open_settings_released'].emit()
    
    def on_text_changed(self, text: _events.Event) -> None:
        text = text.values()[0]
        self._events["text_changed"].emit(text)
    
    def get_text(self) -> TextInputDisplayedElement:
        return self._text_input
    
    def enable_button(self) -> None:
        self._button.enable()
    
    def disable_button(self) -> None:
        self._button.disable()
    
    def set_rect(self, x: int, y: int, w: int, h: int) -> None:
        
        self._text_input.set_size( h/12 )
        self._text_input.set_position(x + w/2, y + 7 * h / 12)
        
        self._button.set_size( h/10 )
        self._button.set_position(x + w/2, y + 5 * h/6)
        
        self._game_title.set_size( h/4 )
        self._game_title.set_position(x + w/2, y + h/5)

        self._settings_button.set_position(x + w - 20 - w/100, y + 20 + w/100)
        self._settings_button.set_size(w/50)
    
    def get_items(self) -> list[ GameDisplayedElement ]:
        return [self._text_input, self._button, self._game_title, self._settings_button]
    


