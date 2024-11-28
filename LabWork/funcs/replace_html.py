from bs4 import BeautifulSoup

def extract_text_from_html(html_content: str) -> str:
    """
    Убирает HTML-разметку и возвращает чистый текст.
    """
    soup: BeautifulSoup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text()
