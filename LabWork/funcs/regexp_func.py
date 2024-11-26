import re


def find_credit_card_numbers(source: str) -> list[str]:
    """Ф-ия поиска номеров банковских карт"""

    pattern: str = r"\b(?:\d{4}[-\s]?){3}\d{4}\b"
    matches: list[str] = re.findall(pattern, source)
    return matches
