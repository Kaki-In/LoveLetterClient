from .app_state import *

import typing as _T
import events as _events

import resources as _resources

class LanguageSettingsApplicationState(ApplicationState):
    def __init__(self):
        super().__init__()

        self._language: int = None
        self._translator: list[tuple[str, _resources.TranslationLanguage]] = []

        self._events.create_events(
            'language_changed',
            'language_list_changed'
        )
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def get_languages(self) -> list[tuple[str, _resources.TranslationLanguage]]:
        return self._languages
    
    def add_language(self, id: str, name: _resources.TranslationLanguage) -> None:
        self._languages.append((id, name))
        self._events['language_list_changed'].emit()
    
    def clear_languages(self) -> None:
        self._languages = []
        self._events['language_list_changed'].emit()
    
    def get_language(self) -> int:
        return self._language
    
    def set_language(self, value: int) -> None:
        self._language = value
        self._events['language_changed'].emit(value)
