from PyQt5 import QtCore as _QtCore
import time as _time

class Animation(_QtCore.QObject):
    signal_frame = _QtCore.pyqtSignal(float)
    signal_stopped = _QtCore.pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
        self._values = []
        self._thread = _QtCore.QThread()
        
        self._one_by_one = True
        self._must_stop = False
        self._infinite = False
        
        self.moveToThread(self._thread)
        self._thread.started.connect(self.run)
        self._thread.finished.connect(self.deleteLater)
        self.signal_stopped.connect(self._thread.quit)
        self.signal_stopped.connect(self.deleteLater)
        
        self._runs = False
        
        self._must_reset = False
        self._verbose = False
        
        self._waiting_transitions = []
    
    def stop(self):
        self._must_stop = True
        try:
            self._thread.wait()
        except:
            pass
    
    def setInfinite(self, enabled: bool) -> None:
        self._infinite = enabled
    
    def isInfinite(self) -> bool:
        return self._infinite
    
    def run(self):
        while not self._must_stop:
            if self._must_reset:
                self._values = self._waiting_transitions
                self._must_reset = False
                self._waiting_transitions = []
            
            if not self._values:
                self._runs = False
                _time.sleep(0.05)
                continue
            
            self._runs = True
            value = self._values.pop(0)
            
            t = _time.monotonic()
            
            while _time.monotonic() - t <= value[2] and (self._one_by_one or not self._values) and not self._must_stop:
                try:
                    self.signal_frame.emit(self.change(value[0], value[1], (_time.monotonic() - t) / value[2]))
                except:
                    pass
                _time.sleep(0.01)
            
            if self._one_by_one or not (self._values or self._must_stop):
                try:
                    self.signal_frame.emit(value[1])
                except:
                    pass
            
            if self.isInfinite() and not self._values:
                self._values.append(value)
            
        self._thread.quit()
    
    def reset(self):
        self._must_reset = True
    
    def isRunning(self) -> bool:
        return self._runs or self._values
    
    def set_one_by_one(self, mode):
        self._one_by_one = bool(mode)
    
    def start_transition(self, value_from, value_to, time):
        if self._must_reset:
            self._waiting_transitions.append((value_from, value_to, time))
        else:
            self._values.append((value_from, value_to, time))
    
    def change(self, value_from, value_to, percentage):
        if percentage > 0.5:
            return value_to
        else:
            return value_from
    
    def get_thread(self) -> _QtCore.QThread:
        return self._thread
    
    def __del__(self):
        self.stop()
    
