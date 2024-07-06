from ..threads.menus_thread import *
from ..ui.view.game import *
from .first_controller import *
from .main_controller import *
from ..threads.menus import *

import events as _events

class MenusController():
    def __init__(self, thread: MenusThread, display: GameWidget):
        super().__init__()

        self._thread = thread
        self._display = display

        thread.get_events()["menu_open"].addEventFunction(self.open_menu)
        thread.get_events()["menu_close"].addEventFunction(self.close_menu)

        self._controllers = []
        self._layers = []

    def get_thread(self) -> MenusThread:
        return self._thread
    
    def get_display(self) -> GameWidget:
        return self._display
    
    def on_open_menu(self, event: _events.Event) -> None:
        menu_name = event.values()[0]

        if   menu_name == "first":
            menu = FirstMenu()

        elif menu_name == "main":
            menu = MainMenu()

        else:
            raise ValueError("couldn't find any menu named " + repr(menu_name))
        
        self._thread.open_menu(menu)
    
    def on_close_menu(self) -> None:
        self._thread.close_menu()

    def open_menu(self, event: _events.Event) -> None:
        menu = event.values()[0]

        if type(menu) == FirstMenu:
            layer = FirstGraphicLayer(self._display.get_resources())
            controller = FirstGraphicLayerController(layer, menu)

            controller.get_events()["open_menu"].addEventFunction(self.on_open_menu)
            controller.get_events()["close_menu"].addEventFunction(self.on_close_menu)

        elif type(menu) == MainMenu:
            layer = MainMenuGraphicLayer(self._display.get_resources())
            controller = MainGraphicLayerController(layer, menu)

            controller.get_events()["open_menu"].addEventFunction(self.on_open_menu)
            controller.get_events()["close_menu"].addEventFunction(self.on_close_menu)
        else:
            raise ValueError("Unknown menu " + type(menu).__name__)
        
        self._display.displayLayer(layer)
        self._layers.append(layer)
        self._controllers.append(controller)
    
    def close_menu(self) -> None:
        self._layers.pop(-1)
        self._controllers.pop(-1)

        self._display.displayLayer(self._layers[-1])
