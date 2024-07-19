from .ui import *
from .objects.settings import *

class MainActivity():
    def __init__(self):
        self._window = MainWindow()
        self._thread = MenusThread()

        self._settings = MainSettings()
        self._controller = MenusController(self._thread, self._window.get_game_widget(), self._settings)
    
    def main(self):
        self._window.showFullScreen()
        self._thread.start()
        self._window.main()



