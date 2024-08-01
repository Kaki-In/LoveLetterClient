from ..settings import *
from ..ui.game import *

import events as _events
from PyQt5 import QtCore as _QtCore

class UiController():
    def __init__(self, widget: GameWidget, settings: MainSettings) -> None:
        self._widget = widget
        self._settings = settings

        resources = widget.get_resources()

        self._settings.get_graphical_settings().add_event_listener('theme', self.on_graphical_settings_theme_change)
        self._settings.get_graphical_settings().add_event_listener('fullscreen', self.on_graphical_settings_fullscreen_change)

        self._settings.get_language_settings().add_event_listener('language', self.on_language_settings_language_change)

        resources.get_themes_mapper().add_event_listener('theme', self.on_widget_theme_change)
        resources.get_translator().add_event_listener('language', self.on_widget_language_change)

        resources.get_themes_mapper().set_theme_name(settings.get_graphical_settings().get_theme_name())
        resources.get_translator().set_actual_language(settings.get_language_settings().get_language_id())
        widget.set_full_screen_mode(settings.get_graphical_settings().get_fullscreen_mode())

        widget.get_events()['geometry_change'].addEventFunction(self.on_window_geometry_change)

        geometry_settings = self._settings.get_graphical_settings().get_window_geometry_settings()
        widget.setGeometry(geometry_settings.get_x(), geometry_settings.get_y(), geometry_settings.get_width(), geometry_settings.get_height())
    
    def on_window_geometry_change(self, event: _events.Event) -> None:
        rect: _QtCore.QRect = event.values()[0]

        self._settings.get_graphical_settings().get_window_geometry_settings().set_x(rect.x())
        self._settings.get_graphical_settings().get_window_geometry_settings().set_y(rect.y())
        self._settings.get_graphical_settings().get_window_geometry_settings().set_width(rect.width())
        self._settings.get_graphical_settings().get_window_geometry_settings().set_height(rect.height())

    def on_graphical_settings_theme_change(self, event: _events.Event) -> None:
        theme_name = event.values()[0]

        if self._widget.get_resources().get_themes_mapper().get_theme_name() != theme_name:
            self._widget.get_resources().get_themes_mapper().set_theme_name(theme_name)
    
    def on_graphical_settings_fullscreen_change(self, event: _events.Event) -> None:
        enabled = event.values()[0]

        if enabled != self._widget.isFullScreen():
            self._widget.set_full_screen_mode(enabled)
    
    def on_language_settings_language_change(self, event: _events.Event) -> None:
        language = event.values()[0]

        if language != self._widget.get_resources().get_translator().get_actual_language():
            self._widget.get_resources().get_translator().set_actual_language(language)

    def on_widget_theme_change(self, event: _events.Event) -> None:
        theme_name = event.values()[0]
        
        if theme_name != self._settings.get_graphical_settings().get_theme_name():
            self._settings.get_graphical_settings().set_theme_name(theme_name)
    
    def on_widget_language_change(self, event: _events.Event) -> None:
        language = event.values()[0]

        if language != self._settings.get_language_settings().get_language_id():
            self._settings.get_language_settings().set_language_id(language)
