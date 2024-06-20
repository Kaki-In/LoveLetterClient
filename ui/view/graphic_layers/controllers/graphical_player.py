from ....background_threads.linear_animation import *
from ..graphics.player import *

from PyQt5 import QtCore as _QtCore
import love_letter as _love_letter
import random as _random

class GraphicalPlayerController():
    def __init__(self, player: _love_letter.LoveLetterPlayer, view: PlayerDisplayedElement):
        self._player = player
        
        self._cards = []
        
        self._element: PlayerDisplayedElement = view
        
