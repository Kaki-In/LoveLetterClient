from PyQt5 import QtWidgets as _QtWidgets, QtGui as _QtGui

from .game import *
from .resources import *

from ..objects.settings.main_settings import *

APP = _QtWidgets.QApplication([''])

class MainWindow(_QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self._resources = Resources()
        
        self._resources.get_layouts_mapper().load_ui_to_widget(self, "layout_main_window")
        
        icon = _QtGui.QIcon(_QtGui.QPixmap(self._resources.get_images_mapper().get_image_by_name("icon").get_variant("64")))
        
        self.setWindowIcon(icon)
        
        w = GameWidget(self._resources)
        self.setCentralWidget(w)

        self._game_widget = w
        
        self.show()
    
    def get_game_widget(self) -> GameWidget:
        return self._game_widget
    
    def set_title(self, title: str) -> None:
        self.setWindowTitle(title)
    
    def get_title(self) -> None:
        return self.windowTitle()
    
    def set_full_screen_mode(self, enabled: bool) -> None:
        if enabled:
            self.showFullScreen()
        else:
            self.show()
    
    def main(self):
        APP.exec()
    
    
