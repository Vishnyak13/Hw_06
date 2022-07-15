import re

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for cyr, lat in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyr)] = lat
    TRANS[ord(cyr.upper())] = lat.upper()


def normalize(name: str) -> str:
    """
    1. Проводить транслітерацію кирилічного алфавіту на латинський.
    2. Замінює всі символи крім латинських літер, цифр на '_'.
    :param name:
    :return str:
    """
    t_name = name.translate(TRANS)
    t_name = re.sub(r"\W", "_", t_name)
    return t_name