import unittest
from unittest.mock import patch

from funcs.work_with_url import get_content_from_url


class TestGetContentFromURL(unittest.TestCase):
    """
    Класс для тестирования запроса к URL
    """

    @patch("requests.get")
    def test_get_content_from_url_success(self, mock_get):
        # Настраиваем mock объект
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "<html><body>Тестовый текст</body></html>"

        # Вызываем ф-ию
        result = get_content_from_url("https://www.google.com")

        # Проверка
        self.assertEqual(result, "<html><body>Тестовый текст</body></html>")
        mock_get.assert_called_once_with("https://www.google.com")

    @patch("requests.get")
    def test_get_content_from_url_failure(self, mock_get):
        # Настраиваем mock объект
        mock_get.return_value.status_code = 404
        mock_get.return_value.text = ""

        # Вызываем ф-ию
        result = get_content_from_url("https://www.google.com")

        # Проверка
        self.assertEqual(result, "")
        mock_get.assert_called_once_with("https://www.google.com")
