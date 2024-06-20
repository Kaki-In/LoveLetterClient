from PyQt5 import QtGui as _QtGui

import darkdetect as _dark_detect

class CustomPalette(_QtGui.QPalette):
    def __init__(self):
        super().__init__()
        
        self._dark_mode = _dark_detect.isDark()
    
    def dark_mode_is_enabled(self) -> bool:
        return self._dark_mode
    
    def set_dark_mode(self, enabled: bool) -> None:
        self._dark_mode = enabled

