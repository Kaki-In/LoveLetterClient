class TranslationLanguage():
    def __init__(self, name: str, data: dict[str, str]):
        self._name = name
        self._translations = data

    def translate(self, translation_id: str, **data) -> str:
        if translation_id in self._translations:
            return self._translations[translation_id].format(data)
        
        else:
            print("WARNING : No such translation found for language " + self._name + ": " + repr(translation_id))
            return translation_id
    
    def get_name(self) -> str:
        return self.translate('_name')



