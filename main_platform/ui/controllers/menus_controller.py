from .controllers_mapper import *

from ..menus.menus_thread import *
from ..menus.menus import *

from ..game import *

from ..menus.controllers import *
from ...settings import *

import events as _events

class MenusController():
    def __init__(self, thread: MenusThread, display: GameWidget, settings: MainSettings):
        super().__init__()

        self._thread = thread
        self._display = display
        self._settings = settings

        thread.get_events()["menu_open"].addEventFunction(self.open_menu)
        thread.get_events()["menu_close"].addEventFunction(self.close_menu)

        self._controllers = []
        self._map = ControllersMapper()
        self._layers: list[GraphicLayer] = []

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
        
        elif menu_name == "settings":
            menu = SettingsMenu()
        
        elif menu_name == "settings.language":
            menu = LanguageSettingsMenu()

        elif menu_name == "settings.graphical":
            menu = GraphicalSettingsMenu()

        else:
            raise ValueError("couldn't find any menu named " + repr(menu_name))
        
        self._thread.open_menu(menu)
    
    def on_close_menu(self) -> None:
        self._thread.close_menu()

    def open_menu(self, event: _events.Event) -> None:
        menu = event.values()[0]

        if type(menu) is FirstMenu:
            layer = FirstGraphicLayer(self._display.get_resources())
            controller = FirstGraphicLayerController(layer, menu, self._settings)

        elif type(menu) is MainMenu:
            layer = MainMenuGraphicLayer(self._display.get_resources())
            controller = MainGraphicLayerController(layer, menu, self._settings)

        elif type(menu) is SettingsMenu:
            layer = SettingsLayer(self._display.get_resources())
            controller = SettingsGraphicLayerController(layer, menu, self._settings)

        elif type(menu) is LanguageSettingsMenu:
            layer = LanguageSettingsLayer(self._display.get_resources())
            controller = LanguageSettingsGraphicLayerController(layer, menu, self._settings)

        elif type(menu) is GraphicalSettingsMenu:
            layer = GraphicalSettingsLayer(self._display.get_resources())
            controller = GraphicalSettingsGraphicLayerController(layer, menu, self._settings)

        else:
            raise ValueError("Unknown menu " + type(menu).__name__)
        
        self._display.displayLayer(layer, True)

        for item in layer.get_items():
            item.start_threads()
            
        self._layers.append(layer)

        controller.get_events()["open_menu"].addEventFunction(self.on_open_menu)
        controller.get_events()["close_menu"].addEventFunction(self.on_close_menu)
        self._controllers.append(controller)
    
    def close_menu(self) -> None:
        for item in self._layers[-1].get_items():
            item.stop_threads()

        self._layers.pop(-1)
        self._controllers.pop(-1)

        self._display.displayLayer(self._layers[-1], False)
