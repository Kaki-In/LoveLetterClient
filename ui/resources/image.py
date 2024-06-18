from PyQt5 import QtGui as _QtGui

class Image():
    def __init__(self, name: str, image: _QtGui.QImage):
        self._default_image: _QtGui.QImage = image
        self._name: str = name
        
        self._variants: dict[str, _QtGui.QImage] = {}
    
    def add_variant(self, name, image):
        self._variants[ name ] = image
    
    def get_variant(self, name):
        if name in self._variants: 
            return self._variants[ name ]
        
        return self._default_image
    
    def get_name(self) -> str:
        return self._name
    
