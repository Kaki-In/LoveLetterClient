import os as _os

from .palette import *

class PalettesMapper():
    def __init__(self, dirname: str):
        self._dirname = dirname
        self._sub_palettes: dict[str, PalettesMapper] = {}

        self._palettes: dict[str, Palette] = {}

        for sub_path in _os.listdir(self._dirname):
            next_path = self._dirname + _os.sep + sub_path
            
            if _os.path.isdir(next_path):
                palette = PalettesMapper(next_path)
                self._sub_palettes[sub_path] = palette
            elif sub_path.endswith('.palette'):
                palette = Palette(next_path)
                self._palettes[sub_path[:-len('.palette')]] = palette
    
    def get_sub_palette(self, name: str) -> 'PalettesMapper':
        return self._sub_palettes[name]
    
    def get_palette(self, name: str) -> Palette:
        return self._palettes[name]

