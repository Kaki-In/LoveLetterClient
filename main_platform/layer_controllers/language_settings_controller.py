from .controller import *

from ..ui.graphic_layers.language_settings import *
from ..platform.apps.state.language_settings import *
from ..settings import *

import events as _events

class LanguageSettingsGraphicLayerController(LayerController):
    def __init__(self, graphic_layer: LanguageSettingsLayer, application: LanguageSettingsApplicationState, settings: MainSettings):
        super().__init__(graphic_layer, application, settings)

        self.add_layer_event('back', self.on_back_pressed)
        self.add_layer_event('language_change', self.on_language_requested)

        translator = graphic_layer.get_resources().get_translator()

        application.clear_languages()
        for language_id in translator.get_languages():
            language = translator.get_language(language_id)
            application.add_language(language_id, language)
        
        graphic_layer.set_languages_list([language[1].get_name() for language in application.get_languages()])

        language_id = translator.get_actual_language()
        languages = [tup[0] for tup in application.get_languages()]

        application.set_language(languages.index(language_id))
        graphic_layer.set_position(languages.index(language_id))

    def get_layer(self) -> LanguageSettingsLayer:
        return super().get_layer()
    
    def get_application_state(self) -> LanguageSettingsApplicationState:
        return super().get_application_state()
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def on_back_pressed(self, event: _events.Event) -> None:
        self.close_application()
    
    def on_graphical_settings_pressed(self, event: _events.Event) -> None:
        return
        self.open_application('settings.graphical')
    
    def on_language_settings_pressed(self, event: _events.Event) -> None:
        self.open_application('settings.language')
    
    def on_language_requested(self, event: _events.Event) -> None:
        item = event.values()[0]
        language = self.get_application_state().get_languages()[item]

        self.get_application_state().set_language(language)

        self._settings.get_language_settings().set_language_id(language[0])

        self.on_back_pressed(event)
