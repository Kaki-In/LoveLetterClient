from .images import *
from .fonts import *
from .layouts import *
from .translations import *

class Resources():
    def __init__(self):
        self._images = ImagesMapper()
        self._fonts = FontsMapper()
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
    
    
