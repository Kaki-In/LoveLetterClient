import settings as _settings
import os as _os

from .language import *
from .graphics import *
from .user import *

class MainSettings():
    def __init__(self):
        home_path = _os.environ["HOME"]
        self._directory = _settings.SettingsDirectory(home_path + _os.sep + ".love_letter")

        if not self._directory.has_file("language"):
            self._directory.add_settings_file("language")
        
        if not self._directory.has_file("graphics"):
            self._directory.add_settings_file("graphics")

        if not self._directory.has_file("user"):
            self._directory.add_settings_file("user")

        self._language_settings = LanguageSettings(self._directory.get_settings_file('language').get_settings())
        self._graphical_settings = GraphicalSettings(self._directory.get_settings_file('graphics').get_settings())
        self._user_settings = UserSettings(self._directory.get_settings_file('user').get_settings())
    
    def get_language_settings(self) -> LanguageSettings:
        return self._language_settings
    
    def get_graphical_settings(self) -> GraphicalSettings:
        return self._graphical_settings
    
    def get_user_settings(self) -> UserSettings:
        return self._user_settings
    
