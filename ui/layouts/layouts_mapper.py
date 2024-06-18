import os as _os
import io as _io
from PyQt5 import uic as _uic

class LayoutsMapper():
    def __init__(self):
        self._layouts: dict[str, str] = {}
        
        path = _os.path.abspath(_os.path.dirname(__file__))
        
        for file_name in _os.listdir(path):
            if not file_name.endswith(".ui"):
                continue
            
            ui_name = file_name[ :-3 ]
            
            a = open(path + _os.path.sep + file_name, "r")
            ui_content = a.read()
            a.close()
            
            self._layouts[ui_name] = ui_content
    
    def get_ui_by_id(self, id : str) -> str:
        return self._layouts[id]
    
    def load_ui_to_widget(self, widget, id: str) -> None:
        f = _io.StringIO(self.get_ui_by_id(id))
        _uic.loadUi(f, widget)
    

LAYOUT_MAPPER = LayoutsMapper()
