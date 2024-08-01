import settings as _settings
import events as _events
import typing as _T

class GeometrySettings():
    def __init__(self, configuration: _settings.SettingsObject):
        self._configuration = configuration
        
        if not 'x' in configuration:
            configuration['x'] = 0

        if not 'y' in configuration:
            configuration['y'] = 0

        if not 'width' in configuration:
            configuration['width'] = 320

        if not 'height' in configuration:
            configuration['height'] = 222

        self._events = _events.EventObject(
            'x',
            'y',
            'width',
            'height'
        )
    
    def add_event_listener(self, name: str, func: _T.Callable) -> None:
        self._events[name].addEventFunction(func)
        
    def get_x(self) -> int:
        return self._configuration['x']
    
    def get_y(self) -> int:
        return self._configuration['y']
    
    def get_width(self) -> int:
        return self._configuration['width']
    
    def get_height(self) -> int:
        return self._configuration['height']
    
    def set_x(self, x: int) -> None:
        self._configuration['x'] = x
        self._events['x'].emit(x)
    
    def set_y(self, y: int) -> None:
        self._configuration['y'] = y
        self._events['y'].emit(y)
    
    def set_width(self, width: int) -> None:
        self._configuration['width'] = width
        self._events['width'].emit(width)
    
    def set_height(self, height: int) -> None:
        self._configuration['height'] = height
        self._events['height'].emit(height)
