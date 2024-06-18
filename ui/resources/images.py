import pathlib as _pathlib
import os as _os
import io as _io
from PyQt5 import QtGui as _QtGui

from .image import *

class ImagesMapper():
    def __init__(self):
        dirname = _os.path.dirname(__file__) + _os.sep + "images/"
        
        directory = _pathlib.Path( dirname )
        
        self._images: dict[str, Image] = {}
        
        for directory_name in directory.rglob( "." ):
            directory_name = str(directory_name)
            dir_name = directory_name[ len(str(directory)) + 1 : ].replace(_os.path.sep, ".")
            
            for file_name in _os.listdir(directory_name):
                path = directory_name + _os.path.sep + file_name
                
                if _os.path.isdir(path) or not file_name.endswith(".png"):
                    continue
                
                image_name = file_name[ :-4 ]
                
                a = open(path, "rb")
                image = _QtGui.QImage.fromData(a.read())
                a.close()
                
                if not image_name in self._images:
                    self._images[ image_name ] = Image(image_name, image)
                
                if dir_name:
                    self._images[ image_name ].add_variant(dir_name, image)
                
    
    def get_image_by_name(self, name : str) -> Image:
        return self._images[name]
    
    

IMAGES_MAPPER = ImagesMapper()
