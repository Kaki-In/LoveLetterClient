from .controller import *

from ..graphic_layers.graphical_settings import *
from ..menus.settings_menu import *
from ....settings import *

import events as _events

class GraphicalSettingsGraphicLayerController(LayerController):
    def __init__(self, graphic_layer: GraphicalSettingsLayer, menu: GraphicalSettingsMenu, settings: MainSettings):
        super().__init__(graphic_layer, menu, settings)

        self.add_layer_event('back', self.on_back_pressed)
        self.add_layer_event('theme_change', self.on_theme_requested)
        self.add_layer_event('fullscreen_change', self.on_fullscreen_requested)

        themes = graphic_layer.get_resources().get_themes_mapper()

        menu.clear_themes()
        for theme_id in themes.get_theme_names():
            theme = themes.get_theme(theme_id)
            menu.add_theme(theme_id, theme)
        
        graphic_layer.set_themes_list([theme[0] for theme in menu.get_themes()])

        theme_id = themes.get_theme_name()
        themes = [tup[0] for tup in menu.get_themes()]

        menu.set_theme(themes.index(theme_id))
        graphic_layer.set_position(themes.index(theme_id))

        graphic_layer.set_fullscreen(settings.get_graphical_settings().get_fullscreen_mode())

    def get_layer(self) -> GraphicalSettingsLayer:
        return super().get_layer()
    
    def get_menu(self) -> GraphicalSettingsMenu:
        return super().get_menu()
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def on_back_pressed(self, event: _events.Event) -> None:
        self.close_menu()
    
    def on_theme_requested(self, event: _events.Event) -> None:
        item = event.values()[0]
        theme = self.get_menu().get_themes()[item]

        self.get_menu().set_theme(theme)

        self._settings.get_graphical_settings().set_theme_name(theme[0])

        self.on_back_pressed(event)
    
    def on_fullscreen_requested(self, event: _events.Event) -> None:
        value = event.values()[0]
        self._settings.get_graphical_settings().set_fullscreen_mode(value)
