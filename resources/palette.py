from PyQt5 import QtGui as _QtGui
import os as _os

class Palette():
    def __init__(self, path: str):
        self._path = path
        self._colors: dict[str, _QtGui.QColor] = {}

        file = open(path, "r")
        self.load_data(file.read())
        file.close()
    
    def get_color(self, name: str) -> _QtGui.QColor:
        if not name in self._colors:
            raise ValueError('palette ' + self._path + ' does not contain any color named ' + name)

        return self._colors[name]
    
    def load_data(self, data: str) -> None:
        lines = data.split('\n')

        for line in lines:
            while line.startswith(' '):line = line[1:]
            while line.endswith(' '): line = line[:-1]
            while '\t' in line:line = line.replace('\t', ' ')
            while '  ' in line:line = line.replace('  ', ' ')

            if not line:
                continue

            name, value = line.split(' ')
            self._colors[name] = _QtGui.QColor.fromRgba(convert_str_to_int(value))

def convert_str_to_int(str_value) -> int:
    if str_value[0] == "#":
        str_value = str_value[1:]
    else:
        return int(str_value, 16)
    
    l = len(str_value)

    if not l in (3, 4, 6, 8):
        raise ValueError('unknown color ' + repr(str_value))
    
    if l == 3:
        str_value = str_value[0] * 2 + str_value[1] * 2 + str_value[2] * 2
        l = 6

    if l == 4:
        str_value = str_value[0] * 2 + str_value[1] * 2 + str_value[2] * 2 + str_value[3] * 2
        l = 8

    result = int(str_value, 16)

    if l == 6:
        result = result + 0xFF000000

    return result

