import os as _os
import pathlib as _pathlib
from PyQt5 import QtGui as _QtGui, QtWidgets as _QtWidgets, QtCore as _QtCore
from .image import *

class ImagesTheme():
    def __init__(self, dirname: str):
        self._dirname = dirname

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
                effect = _QtWidgets.QGraphicsBlurEffect()
                effect.setBlurRadius(2)
                image = self.applyEffectToImage(_QtGui.QImage.fromData(a.read()), effect)
                a.close()
                
                if not image_name in self._images:
                    self._images[ image_name ] = Image(image_name, image)
                
                if dir_name:
                    self._images[ image_name ].add_variant(dir_name, image)
    
    def get_image_by_name(self, name : str) -> Image:
        return self._images[name]
    
    def applyEffectToImage(self, src: _QtGui.QImage, effect: _QtWidgets.QGraphicsEffect, extent: int = 0) -> _QtGui.QImage:
        scene = _QtWidgets.QGraphicsScene()
        item = _QtWidgets.QGraphicsPixmapItem()
        item.setPixmap(_QtGui.QPixmap.fromImage(src))
        item.setGraphicsEffect(effect)
        scene.addItem(item)
        res = _QtGui.QImage(src.size() + _QtCore.QSize(extent*2, extent*2), _QtGui.QImage.Format.Format_ARGB32)
        res.fill(_QtCore.Qt.GlobalColor.transparent)
        ptr = _QtGui.QPainter(res)
        scene.render(ptr, _QtCore.QRectF(), _QtCore.QRectF( -extent, -extent, src.width()+extent*2, src.height()+extent*2 ) )
        ptr.end()
        return res
    
    def get_name(self) -> str:
        return self._name
    