from ..graphic_layers.first_layer import *

class FirstGraphicLayerController():
    def __init__(self, graphic_layer: FirstGraphicLayer):
        self._layer = graphic_layer
        self._layer.signal_button_press.connect(self.on_button_press)
        self._layer.signal_button_release.connect(self.on_button_release)
        self._layer.signal_text_changed.connect(self.on_text_changed)
    
    def on_button_press(self):
        pass
    
    def on_button_release(self):
        pass
    
    def on_text_changed(self, value):
        if value:
            self._layer.enable_button()
        else:
            self._layer.disable_button()
    
    def layer(self):
        return self._layer
    


