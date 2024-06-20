from .layer import *

from .graphics.text_input import *
from .graphics.button import *
from .graphics.title import *

from .controllers.graphical_text_input import *
from .controllers.graphical_button import *

class FirstGraphicLayer(GraphicLayer):
    def __init__(self):
        super().__init__()
        
        self._text_input = TextInputDisplayedElement("")
        self._text_input.set_text_hint("Veuillez entrer votre nom")
        
        self._text_controller = GraphicalTextInputController(self._text_input)
        
        self._button = ButtonDisplayedElement("Jouer")
        self._button.disable()
        
        self._button_controller = GraphicalButtonController(self._button)
        
        self._game_title = GameTitleDisplayedElement()
    
    def set_rect(self, x: int, y: int, w: int, h: int) -> None:
        
        self._text_input.set_size( h/12 )
        self._text_input.set_position(x + w/2, y + 7 * h / 12)
        
        self._button.set_size( h/6 )
        self._button.set_position(x + w/2, y + 5 * h/6)
        
        self._game_title.set_size( h/4 )
        self._game_title.set_position(x + w/2, y + 9*h/24)
    
    def get_items(self) -> list[ GameDisplayedElement ]:
        return [self._text_input, self._button, self._game_title]
    


