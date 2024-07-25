import os as _os

from .images_theme import *

class ImagesMapper():
    def __init__(self, dirname: str):
        self._themes: dict[str, ImagesTheme] = {}

        self._actual_theme = None
        
        for entity_name in _os.listdir(dirname):
            if _os.path.isdir(dirname + _os.sep + entity_name):
                self._themes[entity_name] = ImagesTheme(dirname + _os.sep + entity_name)

                if self._actual_theme is None:
                    self._actual_theme = entity_name
        
    def get_theme(self, name: str) -> ImagesTheme:
        return self._themes[name]
    
    def get_image_by_name(self, name: str) -> Image:
        return self._themes[self._actual_theme].get_image_by_name(name)
    
    def get_theme_name(self) -> str:
        return self._actual_theme

    def set_theme_name(self, name: str) -> None:
        self._actual_theme = name
    
    def get_theme_names(self) -> list[str]:
        return list[self._themes]



