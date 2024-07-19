import os as _os
from PyQt5 import QtGui as _QtGui

class FontsMapper():
    def __init__(self, directory):
        self._fonts: dict[str, str] = {}
        
        path = directory
        
        for file_name in _os.listdir(path):
            if not (file_name.endswith(".ttf") or file_name.endswith(".woff")):
                continue
            
            font_name = file_name[ :file_name.index(".") ]
            self._fonts[ font_name ] = path + _os.path.sep + file_name
    
    def require_font(self, name: str) -> None:
        _QtGui.QFontDatabase.addApplicationFont(self._fonts[ name ])
            
    