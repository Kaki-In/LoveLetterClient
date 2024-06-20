from PyQt5 import QtCore as _QtCore
import time as _time

class GameThread(_QtCore.QObject):
    signal_stopped = _QtCore.pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
        self._thread = _QtCore.QThread()
        
        self.moveToThread(self._thread)
        self._thread.started.connect(self.run)
        self._thread.finished.connect(self.deleteLater)
        self.signal_stopped.connect(self._thread.quit)
        self.signal_stopped.connect(self.deleteLater)
        
        self._runs = False
        self._must_stop = False
        
    def stop(self):
        self._must_stop = True
        try:
            self._thread.wait()
        except:
            pass
    
    def run(self):
        ...
        print("Ended")
        self.signal_stopped.emit()
    
    def isRunning(self) -> bool:
        return self._runs
    
    def get_thread(self) -> _QtCore.QThread:
        return self._thread
    
    def __del__(self):
        self.stop()
    
