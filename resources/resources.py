from .images import *
from .fonts import *
from .translations import *

import os as _os

class Resources():
    def __init__(self, directory):
        self._images = ImagesMapper(directory + _os.sep + "images")
        self._fonts = FontsMapper(directory + _os.sep + "fonts")
        self._translator = TranslationsMapper(directory + _os.path.sep + "translations")
    
    def get_images_mapper(self) -> ImagesMapper:
        return self._images
    
    def get_fonts_mapper(self) -> FontsMapper:
        return self._fonts
    
    def get_translator(self) -> TranslationsMapper:
        return self._translator
    
    
