import re


class RegExpFinder:
    def __init__(self, pattern: str):
        self.pattern: str = pattern

    def find_regexp(self, source: str) -> list[str]:
        """Ф-ия поиска регулярного выражения"""

        matches: list[str] = re.findall(self.pattern, source)
        return matches
