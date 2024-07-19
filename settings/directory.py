from .file import *

import os as _os

class SettingsDirectory():
    def __init__(self, directory_path: str):
        self._path = directory_path
        self._files: dict[str, SettingsFile] = []
        self._dirs: dict[str, SettingsDirectory] = {}

        if not _os.path.exists(self._path):
            _os.makedirs(self._path)

        for sub_item in _os.listdir(self._path):
            abs_item = self._path + _os.sep + sub_item

            if _os.path.isdir(abs_item) or _os.path.islink(abs_item):
                self._dirs[sub_item] = SettingsDirectory(abs_item)

            elif _os.path.isfile(abs_item) and abs_item.endswith('.settings'):
                self._files[sub_item] = SettingsFile(abs_item)
    
    def get_settings_file(self, name: str) -> SettingsFile:
        if "." in name:
            return self.get_settings_directory(name[:name.index('.')]).get_settings_file(name[name.index(".") + 1:])
        
        return self._files[name]
    
    def get_settings_directory(self, name: str) -> 'SettingsDirectory':
        if "." in name:
            return self.get_settings_directory(name[:name.index('.')]).get_settings_directory(name[name.index(".") + 1:])
        
        return self._dirs[name]
    
    def add_settings_directory(self, name: str) -> 'SettingsDirectory':
        if "." in name:
            return self.get_settings_directory(name[:name.index('.')]).add_settings_directory(name[name.index(".") + 1:])
        
        self._dirs[name] = SettingsDirectory(self._path + _os.sep + name)
        return self._dirs[name]
    
    def add_settings_file(self, name: str) -> SettingsFile:
        if not _os.path.exists(self._path):
            pass


