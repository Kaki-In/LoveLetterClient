import settings as _settings

class LanguageSettings():
    def __init__(self, configuration: _settings.SettingsObject):
        self._configuration = configuration
        
        if not 'language' in configuration:
            configuration['language'] = "en_EN"
        
    def get_language_id(self) -> str:
        return self._configuration['language']
    
    def set_language_id(self, name: str) -> None:
        self._configuration['language'] = name
