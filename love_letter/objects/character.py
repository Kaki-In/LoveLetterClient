class LoveLetterCharacter():
    def __init__(self, value: int, name: str, description: str):
        self._name: str = name
        self._description: str = description
        self._value: int = value
        
    def get_name(self) -> str:
        return self._name
    
    def get_description(self) -> str:
        return self._description
    
    def get_value(self) -> int:
        return self._value
    
    def __lt__(self, second_character: 'LoveLetterCharacter') -> bool:
        return self.get_value() < second_character.get_value()

    def __gt__(self, second_character: 'LoveLetterCharacter') -> bool:
        return self.get_value() > second_character.get_value()

    def __eq__(self, second_character: 'LoveLetterCharacter') -> bool:
        return self.get_value() == second_character.get_value()

LOVE_LETTER_CHARACTER_GUARD     = LoveLetterCharacter(1, "Garde"    , "Deviner la carte d'un joueur")
LOVE_LETTER_CHARACTER_PRIEST    = LoveLetterCharacter(2, "Prêtre"   , "Regarder la carte d'un joueur")
LOVE_LETTER_CHARACTER_BARON     = LoveLetterCharacter(3, "Baron"    , "Comparer sa carte avec celle d'un autre joueur")
LOVE_LETTER_CHARACTER_HANDMAID  = LoveLetterCharacter(4, "Servante" , "Se protéger pendant un tour")
LOVE_LETTER_CHARACTER_PRINCE    = LoveLetterCharacter(5, "Prince"   , "Faire défausser une carte")
LOVE_LETTER_CHARACTER_KING      = LoveLetterCharacter(6, "Roi"      , "Échanger sa carte avec un autre joueur")
LOVE_LETTER_CHARACTER_COUNTESS  = LoveLetterCharacter(7, "Comtesse" , "Doit être défausser en présence d'un roi ou d'un prince")
LOVE_LETTER_CHARACTER_PRINCESS  = LoveLetterCharacter(8, "Princesse", "Celui qui défausse cette carte est immédiatement éliminé")

