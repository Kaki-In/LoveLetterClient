from .layer import *

from .graphics.text_input import *
from .graphics.button import *
from .graphics.title import *

from .controllers.graphical_text_input import *
from .controllers.graphical_button import *

from PyQt5 import QtCore as _QtCore

class FirstGraphicLayer(GraphicLayer):
    signal_button_press = _QtCore.pyqtSignal()
    signal_button_release = _QtCore.pyqtSignal()
    
    signal_text_changed = _QtCore.pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        
        self._text_input = TextInputDisplayedElement("")
        self._text_input.set_text_hint("Veuillez entrer votre nom")
        self._text_input.set_size(0)
        self._text_input.signal_text_changed.connect(self.on_text_changed)
        
        self._text_controller = GraphicalTextInputController(self._text_input)
        
        self._button = ButtonDisplayedElement("Jouer")
        self._button.signal_mouse_press.connect(self.on_button_press)
        self._button.signal_mouse_release.connect(self.on_button_release)
        self._button.set_size(0)
        self._button.disable()
        
        self._button_controller = GraphicalButtonController(self._button)
        
        self._game_title = GameTitleDisplayedElement()
    
    def on_button_press(self, event):
        self.signal_button_press.emit()
    
    def on_button_release(self, event):
        self.signal_button_release.emit()
    
    def on_text_changed(self, text):
        self.signal_text_changed.emit(text)
    
    def get_text(self) -> TextInputDisplayedElement:
        return self._text_input
    
    def enable_button(self) -> None:
        self._button.enable()
    
    def disable_button(self) -> None:
        self._button.disable()
    
    def set_rect(self, x: int, y: int, w: int, h: int) -> None:
        
        self._text_input.go_to_size( h/12 )
        self._text_input.set_position(x + w/2, y + 7 * h / 12)
        
        self._button.go_to_size( h/6 )
        self._button.set_position(x + w/2, y + 5 * h/6)
        
        self._game_title.go_to_size( h/4 )
        self._game_title.set_position(x + w/2, y + 9*h/24)
    
    def get_items(self) -> list[ GameDisplayedElement ]:
        return [self._text_input, self._button, self._game_title]
    


