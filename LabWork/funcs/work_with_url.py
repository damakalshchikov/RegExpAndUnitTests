import requests
from requests import Response


def get_content_from_url(url):
    """Ф-ия запроса к URL"""

    try:
        response: Response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка загрузки страницы: {e}")
        return ""
