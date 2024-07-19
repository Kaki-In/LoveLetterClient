import settings as _settings

class UserSettings():
    def __init__(self, configuration: _settings.SettingsObject):
        self._configuration = configuration
        
        if not 'name' in configuration:
            configuration['name'] = ""
    
    def get_name(self) -> str:
        return self._configuration['name']
    
    def set_name(self, value: str) -> None:
        self._configuration['name'] = value
