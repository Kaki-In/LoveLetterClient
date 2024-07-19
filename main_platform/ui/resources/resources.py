from .images import *
from .fonts import *
from .layouts import *
from .translations import *

import os as _os

class Resources():
    def __init__(self):
        self._images = ImagesMapper(_os.path.dirname(__file__) + _os.sep + "images" + _os.sep)
        self._fonts = FontsMapper(_os.path.abspath(_os.path.dirname(__file__)) + _os.path.sep + "fonts")
        self._layouts = LayoutsMapper()
        self._translator = TranslationsMapper()
    
    def get_images_mapper(self) -> ImagesMapper:
        return self._images
    
    def get_fonts_mapper(self) -> FontsMapper:
        return self._fonts
    
    def get_layouts_mapper(self) -> LayoutsMapper:
        return self._layouts
    
    def get_translator(self) -> TranslationsMapper:
        return self._translator
    
    
