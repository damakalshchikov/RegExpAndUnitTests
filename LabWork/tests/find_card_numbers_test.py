import unittest

from regexp_classes.regexp_class import RegExpFinder


class TestFindCardNumbers(unittest.TestCase):
    """
    Класс для тестирования регулярного выражения
    """

    def setUp(self):
        # Создаём атрибут у класса - объект RegExpFinder
        self.regexp_finder: RegExpFinder = RegExpFinder(r"\b(?:\d{4}[-\s]?){3}\d{4}\b")

    def test_find_card_numbers_success(self):
        # Тестируем, что все номера карт будут найдены
        self.assertEqual(
            self.regexp_finder.find_regexp(
                "1234 1234 1234 1234 1234-1234-1234-1234 1234123412341234"
            ),
            [
                "1234 1234 1234 1234",
                "1234-1234-1234-1234",
                "1234123412341234",
            ]
        )

    def test_find_card_numbers_failure(self):
        # Тестируем, что ничего найдено не будет
        self.assertEqual(
            self.regexp_finder.find_regexp("1234-1234-1234-123"),
            []
        )

    def test_find_card_numbers_with_some_text(self):
        # Тестируем, что среди текста найдутся номера карт
        text = """
                4111 1111 1111 1111 some random text
                5500-0000-0000-0004 not a number
                6011 0000-0000-0004
                3400 0000 0000 009 and something else
                """
        self.assertEqual(
            self.regexp_finder.find_regexp(text),
            [
                "4111 1111 1111 1111",
                "5500-0000-0000-0004",
                "6011 0000-0000-0004",
            ]
        )
