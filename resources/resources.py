from .themes import *
from .fonts import *
from .translations import *

import os as _os

class Resources():
    def __init__(self, directory):
        self._themes = ThemesMapper(directory + _os.sep + "themes")
        self._fonts = FontsMapper(directory + _os.sep + "fonts")
        self._translator = TranslationsMapper(directory + _os.path.sep + "translations")
    
    def get_themes_mapper(self) -> ThemesMapper:
        return self._themes
    
    def get_fonts_mapper(self) -> FontsMapper:
        return self._fonts
    
    def get_translator(self) -> TranslationsMapper:
        return self._translator
    
    
