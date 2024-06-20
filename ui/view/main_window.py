from PyQt5 import QtWidgets as _QtWidgets, QtGui as _QtGui

from .game import *
from ..layouts import *

from ..resources.images import *
class MainWindow(_QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        LAYOUT_MAPPER.load_ui_to_widget(self, "layout_main_window")
        
        icon = _QtGui.QIcon(_QtGui.QPixmap(IMAGES_MAPPER.get_image_by_name("icon").get_variant("64")))
        
        self.setWindowIcon(icon)
        
        self.setCentralWidget(GameWidget())
        
        self.show()
    
    def set_title(self, title: str) -> None:
        self.setWindowTitle(title)
    
    def get_title(self) -> None:
        return self.windowTitle()
    
    def set_full_screen_mode(self, enabled: bool) -> None:
        if enabled:
            self.showFullScreen()
        else:
            self.show()
    
    
