from .controllers import *
from .threads import *
from .ui import *

class MainActivity():
    def __init__(self):
        self._window = MainWindow()
        self._thread = MenusThread()
        self._controller = MenusController(self._thread, self._window.get_game_widget())
    
    def main(self):
        self._window.showFullScreen()
        self._thread.start()
        self._window.main()



