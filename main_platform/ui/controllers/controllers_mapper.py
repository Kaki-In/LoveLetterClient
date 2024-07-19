from ..menus.menus import *
from ..menus.graphic_layers import *
from ..menus.controllers.controller import *

class ControllersMapper():
    def __init__(self):
        self._menus: dict[str, tuple[Menu, GraphicLayer, LayerController]] = {}
    
    def add_menu(self, name: str, menu: Menu, layer: GraphicLayer, controller: LayerController) -> None:
        self._menus[name] = (menu, layer, controller)
    
    def get_menu_layer_controller(self, name: str) -> Menu:
        return self._menus[name]

