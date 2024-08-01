from ..platform import *
from ..ui import *
from ..settings import *
from ..layer_controllers import *

import events as _events

class ActivityAppsController():
    def __init__(self, context: ActivityContext, display: GameWidget, settings: MainSettings):
        self._context = context
        self._display = display
        self._settings = settings

        context.get_events()["application_open"].addEventFunction(self.on_open_application)
        context.get_events()["application_close"].addEventFunction(self.on_close_application)

        self._controllers: list[LayerController] = []
        self._layers: list[GraphicLayer] = []

        self.open_application(self._context.get_active_application())
    
    def get_context(self) -> ActivityContext:
        return self._context
    
    def get_display(self) -> GameWidget:
        return self._display
    
    def on_request_open_application(self, event: _events.Event) -> None:
        application = event.values()[0]

        self._context.open_application(application)
    
    def on_request_close_application(self) -> None:
        self._context.close_application()

    def on_open_application(self, event: _events.Event) -> None:
        application: Application = event.values()[0]
        self.open_application(application)
    
    def open_application(self, application: Application) -> None:
        application_state = application.get_state()

        if type(application_state) is FirstApplicationState:
            layer = FirstGraphicLayer(self._display.get_resources())
            controller = FirstGraphicLayerController(layer, application_state, self._settings)

        elif type(application_state) is MainApplicationState:
            layer = MainGraphicLayer(self._display.get_resources())
            controller = MainGraphicLayerController(layer, application_state, self._settings)

        elif type(application_state) is SettingsApplicationState:
            layer = SettingsLayer(self._display.get_resources())
            controller = SettingsGraphicLayerController(layer, application_state, self._settings)

        elif type(application_state) is LanguageSettingsApplicationState:
            layer = LanguageSettingsLayer(self._display.get_resources())
            controller = LanguageSettingsGraphicLayerController(layer, application_state, self._settings)

        elif type(application_state) is GraphicalSettingsApplicationState:
            layer = GraphicalSettingsLayer(self._display.get_resources())
            controller = GraphicalSettingsGraphicLayerController(layer, application_state, self._settings)

        else:
            raise ValueError("Unknown application " + type(application_state).__name__)
        
        self._display.displayLayer(layer, True)

        for item in layer.get_items():
            item.start_threads()
            
        self._layers.append(layer)

        controller.get_events()["open_application"].addEventFunction(self.on_request_open_application)
        controller.get_events()["close_application"].addEventFunction(self.on_request_close_application)
        self._controllers.append(controller)
    
    def on_close_application(self) -> None:
        for item in self._layers[-1].get_items():
            item.stop_threads()

        self._layers.pop(-1)
        self._controllers.pop(-1)

        self._display.displayLayer(self._layers[-1], False)
