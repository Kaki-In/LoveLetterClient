import os as _os
import events as _events
import typing as _T

from .translation_language import *

class TranslationsMapper():
    def __init__(self, directory: str):
        self._languages: dict[str, TranslationLanguage] = {}
        self._actual_language = None

        dirname = directory

        for file_name in _os.listdir(dirname):
            file_path = dirname + _os.sep + file_name

            if not (_os.path.isfile(file_path) and file_name.endswith(".translate")):
                continue

            language_name = file_name[:-10]

            if self._actual_language is None:
                self._actual_language = language_name

            file = open(file_path, "r")
            raw = file.read()
            file.close()

            try:
                result = self.get_translation_data(raw)
            except Exception as exc:
                raise ValueError("could not parse the translation file " + repr(file_path))

            self._languages[language_name] = TranslationLanguage(language_name, result)
        
        self._events = _events.EventObject(
            'language'
        )

    def add_event_listener(self, name: str, function: _T.Callable) -> None:
        self._events[name].addEventFunction(function)
    
    def get_languages(self) -> list[str]:
        return list(self._languages)
    
    def get_language(self, name: str) -> TranslationLanguage:
        return self._languages[name]
    
    def set_actual_language(self, language: str) -> None:
        self._actual_language = language
        self._events['language'].emit(language)

    def get_actual_language(self) -> str:
        return self._actual_language
    
    def get_translation_data(self, raw: str) -> dict[str, str]:
        data = {}

        last_name = None

        for line in raw.split("\n"):
            if line == " "*len(line) or line.replace(" ", "").startswith("#"):
                continue

            if not ":" in line:
                raise SyntaxError("malformed language raw")

            separation_index = line.index(":")

            translation_id = line[:separation_index]
            message = line[separation_index + 1:]

            while translation_id.startswith(" "):
                translation_id = translation_id[1:]
            while translation_id.endswith(" "):
                translation_id = translation_id[:-1]
            
            while message.startswith(" "):
                message = message[1:]
            while message.endswith(" "):
                message = message[:-1]

            if translation_id:
                last_name = translation_id
                data[last_name] = message

            elif last_name:
                data[last_name] += "\n" + message

            else:
                raise SyntaxError("malformed language raw")
        
        return data
    
    def translate(self, translation_id: str, **data) -> str:
        return self._languages[self._actual_language].translate(translation_id, **data)

