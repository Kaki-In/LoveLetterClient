import os as _os

from .translation_language import *

class TranslationsMapper():
    def __init__(self):
        self._languages: dict[str, TranslationLanguage] = {}
        self._actual_language = None

        dirname = _os.path.dirname(__file__) + _os.sep + "translations" + _os.sep

        for file_name in _os.listdir(dirname) or not file_name.endswith(".translate"):
            file_path = dirname + file_name

            if not _os.path.isfile(file_path):
                continue

            language_name = file_name[:-10]

            if self._actual_language is None:
                self._actual_language = language_name

            file = open(file_path, "r")
            raw = file.read()
            file.close()

            result = self.get_translation_data(raw)

            self._languages[language_name] = TranslationLanguage(language_name, result)
    
    def set_actual_language(self, language: str) -> None:
        self._actual_language = language

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

