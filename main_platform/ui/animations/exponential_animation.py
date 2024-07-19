from .animation import *

import time as _time
from PyQt5 import QtCore as _QtCore
import math as _maths

class ExponentialAnimation(Animation):
    def change(self, value_from, value_to, percentage):
        return (value_from - value_to) * _maths.exp( -percentage * 8 ) + value_to
        
    
