import settings as _settings

class GraphicalSettings():
    def __init__(self, configuration: _settings.SettingsObject):
        self._configuration = configuration
        
        if not 'theme' in configuration:
            configuration['theme'] = "cartoon"
        
    def get_theme_name(self) -> str:
        return self._configuration['theme']
    
    def set_theme_name(self, name: str) -> None:
        self._configuration['theme'] = name
