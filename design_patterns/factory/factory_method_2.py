from typing import Dict, Protocol, Type


class Localizer(Protocol):
    def localize(self, msg: str) -> str:
        ...


class GreekLocalizer(Localizer):
    def __init__(self) -> None:
        self.translations = {
            'dog': 'greek dog',
            'cat': 'greek cat',
        }

    def localize(self, msg: str) -> str:
        return self.translations.get(msg, msg)


class EnglishLocalizer(Localizer):
    def localize(self, msg: str) -> str:
        return msg


def get_localizer(language: str = 'English') -> Localizer:
    '''Factory method to get a localizer for a given language'''
    # localizers = Dict[str, Type[Localizer]] = {
    #     'English': EnglishLocalizer,
    #     'Greek': GreekLocalizer,
    # }

    localizers = {
        'English': EnglishLocalizer,
        'Greek': GreekLocalizer,
    }

    return localizers[language]()


def main() -> None:
    e, g = get_localizer(language='English'), get_localizer(language='Greek')

    for msg in 'dog parrot cat bear'.split():
        # print(msg)
        print(e.localize(msg), g.localize(msg))


if __name__ == '__main__':
    main()
