from .animation import *
import time as _time
from PyQt5 import QtCore as _QtCore

class LinearAnimation(Animation):
    def change(self, value_from, value_to, percentage):
        return value_from + percentage * (value_to - value_from)
        
    
